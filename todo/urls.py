from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('todo/', TodoView.as_view()),
    path('todo/<int:pk>/', TodoDetail.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)