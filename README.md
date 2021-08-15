# Django Celery example
**All tasks are contains inside myapp/tasks.py**

```python
    
python -m venv venv

venv\Scripts\activate

pip install requirements.txt

''' The following command  will start one worker and worker will spawn multiple child proceses that are equal to number of cpu cores your system has(default->prefork[multi-processing]) '''
celery -A django_celery_example worker -l info

''' The following command will not create multiple child proceses, and it will start only one worker and all the tasks are performed by that worker'''
celery -A django_celery_example worker --pool=solo -l -info

''' The following command will create one main worker with 5 worker processes/child processes with autoscale of min:3 and max:10 (prefork is default)'''
celery -A django_celery_example worker --pool=prefork --concurrency=5 --autoscale=10,3 -l -info

''' Eventlet and gevent is for multi-threading, used for I/O bound operations. E.g, execute thousands of HTTP GET requests to fetch data from external APIs.'''
celery -A django_celery_example worker -l info -P gevent
or
celery -A django_celery_example worker --pool=[gevent/eventlet] -l -info

''' The following command will start the celery-beat'''
celery -A proj beat -l INFO
```
