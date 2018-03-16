from django.db import models


class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)


class Tweet(models.Model):
    content = models.CharField(max_length=140)
    creation_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

