# Django Celery example
**All tasks are contains inside myapp/tasks.py**

```python
    
python -m venv venv

venv\Scripts\activate

pip install requirements.txt

celery -A django_celery_example worker -l info -P gevent
celery -A proj beat -l INFO
```
