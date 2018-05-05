from django.urls import path
from . import views
from django.contrib import admin
from best_path.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index')
]