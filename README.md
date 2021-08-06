# Django Celery example

```python
    
python -m venv venv

venv\Scripts\activate

pip install requirements.txt

celery -A django_celery_example worker -l info -P gevent
```