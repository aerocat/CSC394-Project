from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

# # Extension of the User Object
# class UserProfile(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	student_id = models.IntegerField(default=0000)
# 	GPA = models.FloatField(default=0.00)
# 	# more fields will go here
# 	def __str__(self):
# 		return self.user.username
#
# def create_profile(sender, **kwargs):
# 	if kwargs['created']:
# 		user_profile = UserProfile.objects.create(user=kwargs['instance'])
#
# post_save.connect(create_profile, sender=User)

class myUserManager(BaseUserManager):
	def create_user(self, email, first_name, last_name, password=None, is_staff=False, is_admin=False):
		if not email:
			raise ValueError("You need to enter a valid email to sign up")
		user_object = self.model(
			email = self.normalize_email(email),
			first_name = first_name,
			last_name = last_name
		)
		user_object.set_password(password)
		user_object.faculty = is_staff
		user_object.admin = is_admin
		user_object.save(using=self._db)
		return user_object

	def create_staffuser(self, email, first_name, last_name, password=None):
		user = self.create_user(
					email = email,
					first_name = first_name,
					last_name = last_name,
					password=password,
					is_staff=True,
					is_admin=False
				)
		return user

	def create_superuser(self, email, first_name, last_name, password=None):
		user = self.create_user(
					email = email,
					password=password,
					first_name = first_name,
					last_name = last_name,
					is_staff=True,
					is_admin=True
				)
		return user



# This defines a Custom User Model for our website
class myCustomUser(AbstractBaseUser):
	# important fields
	email = models.EmailField(max_length=255, unique=True)
	active = models.BooleanField(default=True) # can login (not banned)
	staff = models.BooleanField(default=False) # faculty/staff
	admin = models.BooleanField(default=False) # superuser

	# other fields
	first_name = models.CharField(max_length=50, blank=True, null=True)
	last_name = models.CharField(max_length=50, blank=True, null=True)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name'] # can add here more req. fields

	def __str__(self):
		return self.email

	@property
	def is_active(self):
		return self.active
	@property
	def is_staff(self):
		return self.staff
	@property
	def is_admin(self):
		return self.admin

# # If needed we can extend the custom user model with this model
# class Profile(models.Model):
# 	user = models.OneToOneField(myCustomUser)
