from django.urls import path 
from . views import index_main 

urlpatterns = [
    path('', index_main, name='main')
]