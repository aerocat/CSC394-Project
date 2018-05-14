from django.conf.urls import url
from . import views

app_name = 'user_profile'

urlpatterns = [
    url(r'^profile/$', views.signup, name = "profile"),
]
