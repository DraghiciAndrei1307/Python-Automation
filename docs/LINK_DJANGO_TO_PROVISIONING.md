# Link the Django package to the Ansible provisioning

## Introduction

The other days I managed to create a functional Django Rest API Python package that allowed me to run a 
Django API server that had 2 models (User and Group), and the corresponding serializers and views for them.

How I managed to do that? I simply followed the 
[Django Rest Framework Quickstart](https://www.django-rest-framework.org/tutorial/quickstart/).  

After I managed to do that, I simply thought that I need to customize the solution by creating myself something similar
to the User/Group logic. And so, I created myself the `PostgreSQLVM` model. For that model, I also created the 
serializer named `PostgreSQLVMSerializer` and also the viewset `PostgreSQLVMViewSet`. 

## Implementation

In order to finish this layout, I needed to wrap these 3 components by creating a router in `urls.py`and also define a 
url pattern: 

```commandline
from django.urls import include, path
from rest_framework import routers

from provisioner_api import views


router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r'vms', views.PostgreSQLVMViewSet) # This line was added

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('api/', include(router.urls) ), # and also this line was added
]
```
### Observation

Have a look over this line `router.register(r'vms', views.PostgreSQLVMViewSet)`. Here I defined a new 
router based on the `PostgreSQLVMViewSet`. By doing so, an extensive set of urls (for checking details, create,
delete, etc.) will be generated automatically.   

Without the ViewSet, we should have created a separate set of views and routes in `urls.py` which was a redundant 
operation.    

The ViewSet groups all logic of a single resource inside a single class. The ViewSet does not define HTTP methods 
(GET, POST), but actions (list, create, retrieve, update, destroy).

The DefaultRouter acts as a translator. You just give it a simple prefix like `vms` and it defines 5 standard routes:

| HTTP Method | URL         | Action                      |
|-------------|-------------|-----------------------------|  
| GET         | /vms/       | list()                      |
| POST        | /vms/       | create() / perform_create() |
| GET         | /vms/{id}   | retrieve()                  |
| PUT / PATCH | /vms/{id}   | update()                    |
| DELETE      | /vms/{id}   | destroy()                   |  

How does the DRF thinks? It basically receives the request and checks the URL. Does it have the `/vms/` prefix ? Yes. 
Then, it looks at the type of request (POST, GET, DELETE...) and looks into the table and chooses a specific action. 

If the request was something like a `GET` to the `/vms/5/`, then that router would get the `ID`, which is `5` and would 
send the request to the `retrieve(self, request, pk=5)` action.

Another interesting thing that I found out is that in order to create a new action, you can use something like this:

```commandline
@action(detail=True, methods=['post'])
def restart(self, request, pk=None):
    # your logic here
    pass
```

The router will check this function and will generate this url: `POST /vms/{id}/restart/`

Now that we finished with this aspect, I think that is important to document the entire process of how DRF processes a 
request, and also how we can override the logic of that. 

There are 6 steps that constitute the DRF lifecycle:

1) WSGI / ASGI Server & Django Middleware
- The HTTP request (raw data sent through the network) is received by the server.
- Django gets the request and transforms it into a Python object named `WSGIRequest`
- This object gets through Middlewares (security layers, sessions, CSRF)

2) URL Routing(Router DRF)
- Django gets through `urls.py` and wears the URL `/vms/` to the `POST` method
- It determines that the final destination is the `PostgreSQLVMViewSet` and the `create/perform_create` action.
- The WSGIRequest object is converted into a `rest_framework.request.Request` object

3) The ViewSet's security layers and control

Before the perform_create() method is executed, usually there are 3 essential checks to be performed:
- Authentication: the token/session is checked
- Permissions: it checks if the user has the necessary privileges (`IsAuthenticated`, `IsAdminUser`). If not, the \
request is rejected `403 Forbidden`
- Throttling: it checks if you are sending too many requests per second (DDOS prevention)

4) Serializer (Data validation)

- If the request passed the 3 checks, then the ViewSet uses the serializer `PostgreSQLVMSerializer` in order to convert 
the data you sent (usually a JSON) into Python data types
- The serializer also checks the data. If the data is not valid, then if throws `400 Bad Request`.

5) Logic Execution

If the data is consistent, the serializer saves the instance into the database `serializer.save()` and inside that 
method or the `perform_create()` you can execute your desired logic (in our case, the VM provisioning)

6) The Response

- The serializer transforms the recently saved into the DB object back into the JSON format.
- The ViewSet returns an object `Response(serializer.data, status=status.HTTP_201_CREATED)`
- The response gets back through middlewares and back to the client.

The next thing I would like to talk here is how I managed to insert the provisioning logic into the equation. I managed 
to do that by reading this article 
[Cleanly Override Django REST Framework Defaults](https://unwiredlearning.com/blog/override-drf-defaults) 
where I found out that the best place to insert my provisioning logic was into the `perform_create` method.


```python
class PostgreSQLVMViewSet(viewsets.ModelViewSet):

    queryset = PostgreSQLVM.objects.all().order_by("-created_at")
    serializer_class = PostgreSQLVMSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):

        instance = serializer.save(status="Queued")

        # send the task to the Celery and Redis

        from .tasks import run_ansible_provisioning_task
        run_ansible_provisioning_task.delay(instance.id)
```

### Celery + Redis

Another thing that I want to mention is the Celery and Redis. 

The logic of creating a POST request to the Django server and start the provisioning flow works perfectly without 
Celery and Redis. You send a POST request, trigger the procedure and then wait until the Ansible playbooks finish their
execution. This means that also the POST request remains stuck until the provisioning is done or it will return 
`Timeout` even though the provisioning is in progress.

In order to avoid this situation, we can implement a system that uses Celery and Redis.

Redis is a in-memory ultra-fast database which plays the role of the intermediary. It just saves the task and forwards 
it. In the perform_create() method, where we executed the `delay()`, we not execute the code, we just wrote a note 
(JSON message) in Redis that says that someone needs to start the provisioning.  

Redis is extremely fast and can deal with thousands of messages per second without effort.

Celery is the worker. It s a queue-based system which runs independent of Django. Its role is to listen to Redis to see 
if there are any messages received from it. If a messages is received, it starts executing it. Celery starts the 
process of PostgreSQL VM provisioning and decides if it was a success or not.

## Resources:

https://unwiredlearning.com/blog/override-drf-defaults
