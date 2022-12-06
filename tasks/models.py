from django.db import models
# Create your models here.

class TaskStatus(models.Model):
    state = models.CharField(max_length=20,null=True,blank=True)
    
    def __str__(self):
        return str(self.state)    
class TaskAssighn(models.Model):
    task_number = models.PositiveIntegerField(unique=True,null=True)
    task_desc = models.CharField(max_length=200,null=True)
    status = models.ForeignKey(TaskStatus,null=True,blank=True,on_delete=models.SET_NULL)
    reason = models.CharField(max_length=400,null=True,blank=True)
    url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.task_desc}'

    