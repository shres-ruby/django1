from django.urls import path
from .views import index,details,read


urlpatterns = [
    path('', index),
    path('details/', details),
    path('read/<int:id>', read)
]