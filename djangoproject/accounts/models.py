
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


class UserProfile (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=False)
    about = models.CharField(default="",max_length=255)
    image = models.ImageField(default="default.png",upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'




class Signal():
    @receiver(post_save,sender=User)
    def create_userprofile(sender,instance,created,**kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save,sender=User)
    def save_userprofile(sender, instance, **kwargs):
        instance.userprofile.save()


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title #this will display title
		 #as retrun for object in query
