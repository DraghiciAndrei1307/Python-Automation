# Django Config and Requirements

## Introduction 

This page was created so that I can explain how I managed to integrate the Django Rest Framework (DRF) into this
solution. This solution contains all Python packages required by my architecture to work as expected. One of these
packages is `django_rest_api` which basically has the purpose of running the Django server on the VM (and in the future
on a Docker container) so that we have an API interface for our provisioning Python-Ansible-PostgreSQL platform. 

## Steps performed

1) First, I needed to `set up` the repo so that I can have a package for the DRF. 

I created this structure: 

```commandline
django_rest_api
 - setup.py
 - README.md
```

After, I installed the `djangorestframework` package (also included inside the `requirements.txt`), using:

```commandline
pip install djangorestframework
```

After, inside the `django_rest_api` folder I executed the following command in order to set up the project:

```commandline
django-admin startproject api_config .
python manage.py startapp provisioner_api 
```

The first command, `django-admin startproject api_config` creates the `api_config` folder in the current path. 
The `api_config` folder contains the configuration files (e.g. `settings.py`, `urls.py`, etc.). This means that we 
created a Django REST project.

The next command, `python manage.py startapp provisioner_api` creates the app (basically a folder which contains
the models, serializers and views) named `provisioner_api`. We can create multiple apps for one project (the 
relationship is one-to-many). We just execute the `python manage.py startapp` command as many times we like/need. 
For our purposes, the `provisioner_api` app is more than enough at the moment. 

2) Second, we need to `configure` the Django `app` and `project` (in our case `api_config`). This configuration is 
pretty much the same as the [DRF Quickstart](https://www.django-rest-framework.org/tutorial/quickstart/). 
I will still comment here what I've done.

For the app `provisioner_api` configuration, I created the `serializers.py` (and pasted the contents from the DRF Quickstart) inside the `provisioner_api` folder

```commandline
from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]
```

Next, I copy-pasted the contents of the `views.py` from the DRF Quickstart code snippet: 

```commandline
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from .serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
```

With the mention that I replaced this line: 

```commandline
from tutorial.quickstart.serializers import GroupSerializer, UserSerializer
```

With this line: 

```commandline
from .serializers import GroupSerializer, UserSerializer
```

Now for the project `api_config`:

- Performed the same thing also for the `urls.py` as for the `views.py` and `serializers.py`

```commandline
from django.urls import include, path
from rest_framework import routers

from provisioner_api import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
```

Also with the mention that I needed to change the way I from where import the views.

```commandline
from provisioner_api import views
```

- updated the `setting.py` like this:

```commandline

...

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'provisioner_api',
]

...

```

The `ALLOWED_HOSTS = ['*']` means that there is `no restriction` on the hosts that can use our API.

The last 2 entries (e.g. rest_framework and provisioner_api) from the `INSTALLED_APPS` list were added because:
- we are using the `rest_framework` because it contains all the prerequisites we need
- we are using the `provisioner_api` because it contains pretty much our Django solution

If we do not include those 2 inside the `INSTALLED_APPS`, Django simply will ignore them. 


3) In the end, we need to configure (check the `setup.py`) the `django_rest_api` package which contains our project and app. To do that, 
I've done the following: 

- mentioned that the package needs `djangorestframework` installed: 

```commandline
    install_requires=[
        'click',
        'pg_provisioner_cli_draghici_andrei',
        'djangorestframework',
    ],
```

- ensured that all files that do not have the `.py` extension (e.g. db.sqlite3), basically everything which is `NOT 
Python code` are not taken into consideration when we build the package. 

```commandline
include_package_data=True,
```

- created an entrypoint so that we can start the server

```commandline
    entry_points={
        'console_scripts': [
            'run-pg-api=api_config.manage_launcher:main'
        ]
    }
```

We are using the `run-pg-api` alias to execute this `api_config.manage_launcher:main` function. We are executing the 
`main` function of the `manage_launcher.py` script which can be found inside the `api_config` folder

One last thing that I need to mention here is that you need to open the port 9001. To do that, I performed
the following:

```commandline
sudo firewall-cmd --permanent --add-port=9001/tcp
sudo firewall-cmd --reload
sudo firewall-cmd --list-ports
```

To install the package, just go to the releases of this repo on GitHub and copy the address off the file `.whl`. 
To install the package, just `pip install <link_of_the_whl_file>`

To run the Django server:

```commandline
run-pg-api runserver 0.0.0.0:9001
```
