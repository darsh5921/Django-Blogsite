from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title= models.CharField(max_length=100)
    content = models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    post_date=models.DateTimeField(blank=True,null=True)
    upvote = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def publish(self):
        self.post_date=timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'username':self.author,'pk':self.pk})