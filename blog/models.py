from distutils import text_file
from operator import truediv
from traceback import StackSummary
from turtle import title
from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL

class Tag(models.Model):
    # id = models.AutoField(primary_key=)
    value = models.CharField(max_length=100)
    

    def __str__(self):
        return self.value

class Post(models.Model):
    STATUS_CHOICES = (
        ('DRAFT','Draft'),
        ('PUBLISHED','Published'),
        ('ARCHIEVED','Archieved')
    )


    title = models.TextField(max_length=125)
    content = models.TextField()
    summary = models.TextField(max_length=500, blank=True, null=True )
    slug = models.SlugField(max_length=125)
    auther = models.ForeignKey(User,on_delete= models.PROTECT)
    tags = models.ManyToManyField(Tag,related_name="posts")
    status = models.CharField(max_length=12 , choices=STATUS_CHOICES, default='DRAFT')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-modified_at"]       