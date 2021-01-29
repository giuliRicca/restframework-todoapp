from django.urls import path, include
from django.contrib import admin
from todos import views

urlpatterns = [
    path('', include('todos.urls')),
    path('admin/', admin.site.urls)
]
