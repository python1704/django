from django.db import models
#zidai de moxing lei
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
#leibie
class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
 #biaoqian
class Tag(models.Model):
    name = models.CharField(max_length=64)

#wenzhang
class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    #zhaiyao
    excerpt = models.CharField(max_length=256,blank=True)
    #guanxi
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag,blank=True)

    author = models.ForeignKey(User)
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})
    def __str__(self):
        return self.title