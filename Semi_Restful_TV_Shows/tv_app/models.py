from django.db import models
from time import strftime, localtime
from datetime import datetime

# Create your models here.
class ShowManager(models.Manager):
    # EDIT
    def validate(self, postData):
        errors = {}
        today = datetime.now()
        user = datetime.strptime(postData['date'], "%Y-%m-%d")
        print(today, user)
        if Show.objects.filter(title=postData['title']):
            errors['unique'] = "Show title already exist!"
        if len(postData['title']) < 2:
            errors['title'] = "Show tile should be at least 2 characters!"
            print('title error')
        if len(postData['network']) < 3:
            errors['network'] = "Show network should be at least 3 characters!"
            print('network error')
        if user.date() >= today.date():
            print('date error')
            if user.date() == today.date():
                errors['date'] = "The show's release date can't be Today!"
            elif user.date() > today.date():
                errors['date'] = "The show's release date can't be the Future!"
        if postData['desc']:
            if len(postData['desc']) < 10:
                errors['desc'] = "Show description should be at least 10 characters!"
                print('description error')
        return errors

# Database Table for Shows
class Show(models.Model):
    title = models.CharField(max_length=30)
    network = models.CharField(max_length=30)
    release = models.DateField(auto_now=False, auto_now_add=False, null=True)
    desc = models.TextField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()