# Page 2

# date: 13.05.2026
# time: 23:26 EET

Today marks an important achievement of my PostgreSQL provisioning architecture. Today I managed to perform the first 
API call which created a PostgreSQL provisioned VM.

Today I can say that I have a functional MVP of the application I am developing for almost 1 year. 

The flow is as follows:

API POST request -> Celery (worker) + Redis (persistence in case API or worker were restarted) -> 
pg_provisioner (Python package wrapped around Ansible) -> ansible playbooks (the logic of PostgreSQL VM provisioning)


# TO DO

I need to make the solution more robust. Firstly, I need to set up the logging system for the provisioning workflow. 
Also, the PostgreSQLVM status attribute needs to be precise (the status needs to reflect the reality of the 
provisioning workflow).

The provisioning status:

- Queued = the task (API request) was not taken into consideration by the worker
- Started = the procedure started (the first 1 minute)
- In progress: Storage provisioning, Registering, subscription attach, PostgreSQL config ans install, pgbackrest config
- Finished with status SUCCESS/FAILED

Also, what I need to do is to test the idempotency of the provisioning playbooks and roles. 

Write an in-depth documentation of the Django API flow, how you managed to override the `perform_create` method.

I need to have a detailed and extremely detailed logging system. 

Also, I heard that Flower is pretty good as an addition to Celery. Maybe I will implement that. Why not?

# Priority

The first thing tomorrow: document the logic of the Django request and also the logic behind the Celery 
worker and Redis. Basically, document everything I performed today. This needs to be performed before I move on to 
other tasks.

Also, write a LinkedIn post where to showcase the logs and results of everything you've done so far. Make sure you 
include the commands used, the logs and also the flow diagram. Maybe a video will be a great addition. 