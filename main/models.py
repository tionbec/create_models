from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile:
    name = models.CharField(max_length=100)
    photo = models.ImageField()
    user = models.ForeignKey()


class User:
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    course = models.ManyToOneRel()


class Course:
    title = models.CharField(max_length=200)
    description = models.TextField()
    preview_video = models.FileField()


class Progress:
    user = models.ForeignKey()
    course = models.ForeignKey()
    opened_lessons = models.ManyToOneRel()
    passed_lessons = models.ManyToOneRel()


class CheckHomework:
    user = models.ForeignKey()
    lesson = models.ForeignKey()


class Lesson:
    name = models.CharField(max_length=200)
    description = models.TextField()
    body = models.TextField()
    video = models.FileField()
    course = models.ForeignKey()