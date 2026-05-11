# Page 1

# date: 11.05.2026
# time: 16:17 EET

Today I come back to this solution in order to refactor it and try linking it to the other solution I am working on: 
[PostgreSQL-Ansible-Automation](https://github.com/DraghiciAndrei1307/PostgreSQL-Ansible-Automation)

The purpose is to make this Python solution act as a wrapper around the Ansible solution in order to extend the Ansible
capabilities. 

In order to have a better understanding of what I am trying to achieve, consult this diagram: 
[structural diagram](../docs/diagrams/PostgreSQL_provisioning_platform.png)

Update1: I managed to link the pg_provisioner_cli to the ansible playbook that executes the VM provisioning.

Update2: Managed to set up the basic configuration for the Django REST Framework and run the server on port 9001.

# Plans for next development session

I want to link the Django Rest API to the pg_provisioner_cli and trigger the provisioning procedure. 

Also, in parallel with the Django Rest API, I will implement Celery+Redis so that I can launch async provisioning
tasks via API calls.

In the end, after I manage to implement the things above, we will move on to making this solution more robust and 
start documenting it. I plan to finish all of this until the end of this week.
