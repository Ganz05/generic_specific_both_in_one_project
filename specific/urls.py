from specific.views import *
from django.urls import path

app_name='anything'

urlpatterns=[
    path('page3',page3,name='page3'),
    path('page4',page4,name='page4')
]