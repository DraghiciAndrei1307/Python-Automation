# Monitoring

For monitoring I use this approach: 


1) Start the DRF server using:

```python
run-pg-api
```

2) In a different terminal window, execute the following:

```python
celery -A provisioner_api.tasks worker --loglevel=info
```

3) In yet another terminal window, execute: 

```python
tail -f ~/PostgreSQL-Ansible-Automation/ansible/provisioning_logs/provisioning.log
```
