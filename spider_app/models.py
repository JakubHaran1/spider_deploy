from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
import os


def perform_upload_img(instance, filename):
    return f"spider_imgs/{instance.spider.author.username}/{instance.spider.name}/{filename}"


class User(AbstractUser):
    pass


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag


class Spider(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="spiders")
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    date_created = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.name} | {self.type} | {self.author}'


class Spider_img(models.Model):
    img = models.ImageField(upload_to=perform_upload_img)
    date = models.DateField(auto_now_add=True)
    spider = models.ForeignKey(
        Spider, related_name="spiders_img", on_delete=models.CASCADE)
