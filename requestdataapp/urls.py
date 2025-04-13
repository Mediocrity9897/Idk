from django.urls import path

from .views import procces_get_view

app_name = "requestdataapp"

urlpatterns = [
    path("get/", procces_get_view, name="get-view"),
    
]
