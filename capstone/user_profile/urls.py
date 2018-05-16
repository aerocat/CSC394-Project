from django.conf.urls import url
from . import views

app_name = 'user_profile'

urlpatterns = [
    # url(r'^profile/(?P<username>[a-zA-Z0-9]+)$', views.get_profile, name = "profile"),
    url(r'^/$', views.get_profile, name="profile")
    url(r'edit/$', views.edit_profile, name="edit_profile")
]
