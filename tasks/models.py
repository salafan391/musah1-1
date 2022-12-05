from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings
# Create your models here.

class TaskStatus(models.Model):
    TASK_STATUS=[
        ('تحت الإجراء','تحت الإجراء'),
        ('منجزة','منجزة'),
        ('غير منجزة','غير منجزة'),
        ]
    task = models.ForeignKey('taskassighn',on_delete=models.CASCADE,null=True)
    state = models.CharField(max_length=20,null=True,blank=True,choices=TASK_STATUS,default='تحت الإجراء')
    reason = models.CharField(max_length=200,null=True,blank=True)
    
    def __str__(self):
        return str(self.state)    
class TaskAssighn(models.Model):
    task_number = models.PositiveIntegerField(unique=True,null=True)
    task_desc = models.CharField(max_length=200,null=True)
    status = models.ForeignKey(TaskStatus,null=True,blank=True,on_delete=models.SET_NULL)
    url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.task_desc}'

    