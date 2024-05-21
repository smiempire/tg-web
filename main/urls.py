from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from main import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
