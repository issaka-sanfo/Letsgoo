from django.db import models
from django.contrib.auth.models import User
import uuid
import random
import datetime
import os
from datetime import datetime
# Create your models here.
#from letsgo.models import 

#ContactUs********************************************************************************************************************
class ContactUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username

#Purchage***********************************************************************************************************
class Purchage(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    purchage_date = models.DateField(auto_now_add=True)
    pack = models.IntegerField()
    activated = models.BooleanField(default=True)


#AccessTuto***********************************************************************************************************
class AccessTuto(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    access_date = models.DateField(auto_now_add=True)
    creator_name = models.CharField(max_length=50)


#Category********************************************************************************************************************
class Category(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='categories/', default='none')
    order = models.IntegerField(default=None, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        # assuming that you use same storage for all files in this model:
        storage = self.thumbnail.storage

        if storage.exists(self.thumbnail.name):
            storage.delete(self.thumbnail.name)
        
        super().delete()

    def __str__(self):
        return self.title


def user_directory_path(instance, filename):
    # Get Current Date
    todays_date = datetime.now()

    path = "videos/{}/{}/{}/".format(todays_date.year, todays_date.month, todays_date.day)
    extension = "." + filename.split('.')[-1]
    stringId = str(uuid.uuid4())
    randInt = str(random.randint(10, 99))

    # Filename reformat
    filename_reformat = stringId + randInt + extension

    return os.path.join(path, filename_reformat)


class VideoPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    video_file = models.FileField(upload_to=user_directory_path)
    thumbnail = models.ImageField(upload_to='videos/thumbnail/', null=True, blank=True)
    category = models.CharField(max_length=50, default='none')
    pub_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes')
    video_views = models.ManyToManyField(User, related_name='video_views')
    any_views = models.IntegerField(default=0)

    def delete(self, using=None, keep_parents=False):
        # assuming that you use same storage for all files in this model:
        storage = self.video_file.storage
        store = self.thumbnail.storage

        if storage.exists(self.video_file.name):
            storage.delete(self.video_file.name)

        if store.exists(self.thumbnail.name):
            storage.delete(self.thumbnail.name)

        super().delete()

    def __str__(self):
        return self.title


#Steper********************************************************************************************************************
class StepPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(VideoPost, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    video_file = models.FileField(upload_to='videos/steps')
    pub_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='like')
    video_views = models.ManyToManyField(User, related_name='video_view')

    def delete(self, using=None, keep_parents=False):
        # assuming that you use same storage for all files in this model:
        storage = self.video_file.storage

        if storage.exists(self.video_file.name):
            storage.delete(self.video_file.name)

        super().delete()

    def __str__(self):
        return self.title

#UserData*******************************************************************************************************************
class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()
    profile_pic = models.ImageField(upload_to='pic/', default='pic/default.jpg')
    subscribers = models.ManyToManyField(User, related_name='subscribers')



#Comment********************************************************************************************************************
class Comment(models.Model):
    post = models.ForeignKey(VideoPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username



#Report********************************************************************************************************************
class Report(models.Model):
    post = models.ForeignKey(VideoPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username