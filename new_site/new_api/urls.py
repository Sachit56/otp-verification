from django.urls import path
from . import views

app_name='new_api'

urlpatterns = [
    path('',views.apiView,name='api'),
    path('post/',views.Post_View,name='post'),
    path('update/<int:id>',views.Update_View,name='patch'),
    path('delete/<int:id>',views.Delete_View,name='delete')
]
