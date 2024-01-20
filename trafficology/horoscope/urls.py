from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("daily/", views.daily, name="daily"),
    # path("freeways/", views.FreewayListView.as_view(), name="freeways"),
    path("freeways/", views.freeways, name="freeways"),
]

'''
I would use paths to form queries to Planisphere. 
'''