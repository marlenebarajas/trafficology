from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]

'''
I would use paths to form queries to Planisphere. 
'''