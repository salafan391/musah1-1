from django.forms import *
from .models import TaskAssighn,TaskStatus
from django.contrib.auth.models import User



class TaskForm(ModelForm):
    class Meta:
        model = TaskAssighn
        exclude = ['status','reason']
        labels = {
            'task_desc': 'وصف المهمة',
            'author': 'الموظف',
            'created_at': "تم الإنشاء بتاريخ",
            'updated_at': "تم الإنشاء بتاريخ",
            'time_start': "بدء المهمة",
            'time_end': "نهاية المهمة",
            

        }
        widgets = {
            'task_desc': TextInput(attrs={'class': "form-label", 'class': "form-control"}),
            'time_start': DateTimeInput(attrs={'type': 'datetime-local', 'class': "form-label", 'class': "form-control"}),
            'time_end': DateTimeInput(attrs={'type': 'datetime-local', 'class': "form-label", 'class': "form-control"}),
            'url':URLInput(attrs={'class': "form-label", 'class': "form-control"})


        }


class AddUserForm(ModelForm):
    class Meta:
        model = User
        fields= '__all__'
        exclude = [
            'user_permissions',
            'last_login',
            'is_superuser',
            'groups',
            'date_joined',
            'is_active',
            'is_staff']
        labels = {
            'username': 'اسم المستخدم',
            'password': 'كلمة المرور',
            'email': 'البريد الإلكتروني',
            'first_name':'الاسم الأول',
            'last_name':'اللقب'

        }
        widgets = {
            'first_name': TextInput(attrs={'class': "form-label", 'class': "form-control"}),
            'username': TextInput(attrs={'class': "form-label", 'class': "form-control"}),
            'email': EmailInput(attrs={'class': "form-label", 'class': "form-control"}),
            'password':PasswordInput(attrs={'class': "form-label", 'class': "form-control"}),
            'last_name':TextInput(attrs={'class': "form-label", 'class': "form-control"})
        }   
class UpdateForm(ModelForm):
    class Meta:
        model = TaskStatus
        fields ='__all__'
        widgets={
            'reason':Textarea(attrs={'class': "form-label", 'class': "form-control",'pleceholder':'في حال عدم الإنجاز يرجى ذكر السبب'})
        }
