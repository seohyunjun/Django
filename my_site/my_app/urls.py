from django.urls import path # 
from . import views # . 현재 디렉토리에서 view import

urlpatterns = [
    path('', views.index, name='index') # /my_apps -->PROJECT urls.py
]
