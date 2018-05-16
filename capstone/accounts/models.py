from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Extension of the User Object
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	student_id = models.IntegerField(default=0000)
	GPA = models.FloatField(default=0.00)
	# more fields will go here
	def __str__(self):
		return self.user.username

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
