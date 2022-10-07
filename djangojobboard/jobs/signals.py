from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.conf import settings
from .models import Job


# def CreateJob(sender, instance, created, **kwargs):
#   job = instance
#  user = job.available
# if created == True:
#    user.username = profile.username
#   user.first_name = profile.first_name
#  user.last_name = profile.last_name
# user.email = profile.email
# user.save()
