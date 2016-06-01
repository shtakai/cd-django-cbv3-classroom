from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey('Subject')

    class Meta:
        db_table = 'teachers'


class Student(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey('Teacher')

    class Meta:
        db_table = 'students'


class Subject(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'subjects'
