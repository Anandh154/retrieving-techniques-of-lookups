from django.urls import path
from app.views import *
app_name='app'
urlpatterns=[
    path('dis_topic/',dis_topic,name='dis_topic'),
    path('dis_webpages/',dis_webpages,name='dis_webpages'),
    path('dis_access/',dis_access,name='dis_access'),
]