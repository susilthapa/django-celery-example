from os import name
from django.urls import path


from .views import index, doc_to_pdf ,check_status

app_name = 'myapp'
urlpatterns = [
    path('send-mail/', index, name="index"),
    path('doc-to-pdf/', doc_to_pdf, name="doc_to_pdf"),
    path('check-status/<task_id>', check_status, name="check_status")

]