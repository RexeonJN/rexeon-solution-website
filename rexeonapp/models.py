from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    STATUS_CHOICES = {('draft','Draft'),('published','Published')}
    title = models.CharField(max_length=265, unique = True)
    slug = models.SlugField(max_length=265,unique = True)
    body = models.TextField()
    author = models.ForeignKey(User,related_name = 'blog_posts',on_delete=models.CASCADE,) 
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to ='uploads/', default= None)

    class Meta:
        ordering = ('-created_on',)
    
    # def  __init__(self):
    #         super().__init__(self)
    #         return self.title

    def get_absolute_url(self):
           return reverse('blog_detail',args=[self.created_on.year,
                   self.created_on.strftime('%m'),self.created_on.strftime('%d'),self.slug])

class Get_in_touch(models.Model):
     Name = models.CharField(max_length=100)
     Email = models.CharField(max_length=50)     
     Contact_no = models.IntegerField()
     Queries = models.CharField(max_length=500) 

class Apply(models.Model):
    First_name = models.CharField(max_length = 100)
    Last_name = models.CharField(max_length = 100)
    Email = models.CharField(max_length = 100)
    Contact_no = models.IntegerField()
    Resume = models.FileField(upload_to ='uploads/', default= None)

