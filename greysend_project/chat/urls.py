from chat import views
from django.urls import path

urlpatterns = [
    path('', views.landing_page, name='index'),
]