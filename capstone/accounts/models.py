from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

##Extension of the User Object
#lass UserProfile(models.Model):
#	user = models.OneToOneField(User, on_delete=models.CASCADE)
#	student_id = models.IntegerField(default=0000)
#	GPA = models.FloatField(default=0.00)
# more fields will go here
#	def __str__(self):
#		return self.user.username

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = Student.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

class Faculty(models.Model):
	faculty_id = models.IntegerField()
	faculty_name_first = models.CharField(max_length=50)
	faculty_name_last = models.CharField(max_length=50)
	faculty_email = models.CharField(max_length=50)
	def __str__(self):
		return self.faculty_name_last

class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	student_id = models.IntegerField(default=0000)
	student_name_first = models.CharField(max_length=50)
	student_name_last = models.CharField(max_length=50)
	student_email = models.CharField(max_length=50)
	def __str__(self):
		return self.user.username
