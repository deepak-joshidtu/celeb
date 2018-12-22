from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Users(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    passwd = models.CharField(max_length=100)
# Create your models here.

class Userrequests(models.Model):
    fanuname = models.CharField(max_length=100)
    celuname = models.CharField(max_length=100)
    fcontent = models.CharField(max_length=300)
