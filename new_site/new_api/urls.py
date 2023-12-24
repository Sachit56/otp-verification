from django.urls import path
from . import views

app_name='new_api'

urlpatterns = [
    path('',views.apiView,name='api'),
    path('post/',views.Post_View,name='post')
]
