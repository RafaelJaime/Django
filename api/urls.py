from django.urls import include, path
from . import views

app_name='api'
urlpatterns = [
    path('clients', views.Users_APIView.as_view()),
    path('clients/<pk>', views.Users_APIView_Detail.as_view()),
    path('token', views.TestView.as_view()),
]