from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

app_name='new_api'

urlpatterns = [
    # path('<int:id>/',views.StudentView.as_view(),name='api-id'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('book/',views.BookView,name='book'),
    path('',views.StudentView.as_view(),name='api'),
    path('user/',views.UserView.as_view(),name='user'),
    path('generic/',views.StudentGeneric.as_view(),name='generic'),
    path('generic/<int:id>',views.StudentIdGeneric.as_view(),name='generic_id')
]
