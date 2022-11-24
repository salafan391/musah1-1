from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TaskStatus(models.Model):
    state = models.CharField(max_length=10,null=True,blank=True)
    reason = models.CharField(max_length=200,null=True,blank=True)
        
class TaskAssighn(models.Model):
    task_desc = models.CharField(max_length=200,null=True)
    author = models.ManyToManyField(User, related_name='author')
    status = models.ForeignKey(TaskStatus,null=True,blank=True,on_delete=models.SET_NULL)
    url = models.URLField(null=True, blank=True,
                          verbose_name='رابط الملفات على الدرايف')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    time_start = models.DateTimeField(null=True)
    time_end = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.task_desc}'