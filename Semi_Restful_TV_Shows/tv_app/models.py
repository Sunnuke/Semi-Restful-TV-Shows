from django.db import models
from time import strftime, localtime

# Create your models here.
class ShowManager(models.Model):
    def validate(self, postData):
        errors = {}
        today = strftime(" %Y-%m-%d", localtime())
        if len(postData['title']):
            errors['title'] = "Show tile should be at least 2 characters"
        if len(postData['network']):
            errors['network'] = "Show network should be at least 3 characters"
        if postData['date'] == today:
            errors['date'] = "The show's release date can't be the present"
        if postData['desc']:
            if len(postData['desc']):
                errors['desc'] = "Show description should be at least 10 characters"
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