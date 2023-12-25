from django.urls import path
from . import views

app_name='new_api'

urlpatterns = [
    path('<int:id>/',views.StudentView.as_view(),name='api-id'),
    path('book/',views.BookView,name='book'),
    path('',views.StudentView.as_view(),name='api')
]
