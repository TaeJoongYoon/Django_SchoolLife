from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Department(models.Model):
    dept_name = models.CharField(primary_key=True, max_length=10)

    def __str__(self):
        return self.dept_name

class Instructor(models.Model):
    name = models.CharField(primary_key=True, max_length=4)
    dept_name = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.dept_name, self.name)

class Course(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    title = models.CharField(max_length=10)
    name = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s교수" % (self.title, self.name)

class Category(models.Model):
    category = models.CharField(primary_key=True, max_length=12)

    def __str__(self):
        return self.category

class LecturePost(models.Model):
    title = models.CharField(max_length=25)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.title, self.author)

class MarketPost(models.Model):
    title = models.CharField(max_length=25)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="market/%Y/%m/%d")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s" % (self.title, self.author)

class FreePost(models.Model):
    title = models.CharField(max_length=25)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s" % (self.title, self.author)


class LectureComment(models.Model):
    post = models.ForeignKey(LecturePost, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s - %s" % (self.post, self.author, self.content)

class MarketComment(models.Model):
    post = models.ForeignKey(MarketPost, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s - %s" % (self.post, self.author, self.content)

class FreeComment(models.Model):
    post = models.ForeignKey(FreePost, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s - %s" % (self.post, self.author, self.content)

