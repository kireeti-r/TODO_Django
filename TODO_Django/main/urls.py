from django.urls import path
from . import views
urlpatterns=[
    path("<str:name>",views.index,name="name"),
    path("",views.home,name="home")
    
]