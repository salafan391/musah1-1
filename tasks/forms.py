from django.forms import *
from .models import TaskAssighn,TaskStatus,EmployeeAdd
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TaskForm(ModelForm):
    class Meta:
        model = TaskAssighn
        exclude=['status','reason']
        labels = {
            'task_desc': '',
            'created_at': "تم الإنشاء بتاريخ",
            'updated_at': "تم الإنشاء بتاريخ",
            'task_number':'',
            'employee':'الموظف'
        }
        widgets = {
            'task_number':NumberInput(attrs={'class': "form-label", 'class': "form-control",'placeholder':'رقم المهمة'}),
            'task_desc': TextInput(attrs={'class': "form-label", 'class': "form-control",'placeholder':'وصف المهمة'}),
            'employee': Select(attrs={'class': "form-label", 'class': "form-control"}),

        }

class TaskFormUpdate(ModelForm):
    class Meta:
        model = TaskAssighn
        fields='__all__'
        labels = {
            'employee':'الموظف',
            'task_desc': '',
            'created_at': "تم الإنشاء بتاريخ",
            'updated_at': "تم الإنشاء بتاريخ",
            'task_number':'',
            'status':'الحالة',
            'reason':'ملاحظات'
        }
        
        widgets = {
            'task_number':NumberInput(attrs={'class': "form-label", 'class': "form-control",'placeholder':'رقم المهمة'}),
            'task_desc': TextInput(attrs={'class': "form-label", 'class': "form-control",'placeholder':'وصف المهمة'}),
            'resaon': Textarea(attrs={'class': "form-label", 'class': "form-control"})
        }


class AddUserForm(UserCreationForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'placeholder':'كلمة المرور',
            'class':'form-label',
            'class':'form-control',

        })
        self.fields['password2'].widget.attrs.update({
            'placeholder':'تأكيد كلمة المرور',
            'class':'form-label',
            'class':'form-control',
            
        })
    class Meta:
        model = User
        fields= ['username','email','first_name','last_name']
        widgets = {
            'first_name': TextInput(attrs={'class': "form-label", 'class': "form-control",'placeholder':'الاسم الأول'}),
            'username': TextInput(attrs={'class': "form-label", 'class': "form-control",'placeholder':'اسم المستخدم'}),
            'email': EmailInput(attrs={'class': "form-label", 'class': "form-control",'placeholder':'البريد الإلكتروني'}),
            'last_name':TextInput(attrs={'class': "form-label", 'class': "form-control",'placeholder':'اللقب'})
        }   

class CreateStatus(ModelForm):
    class Meta:
        model = TaskStatus
        fields = '__all__'
        labels={
            'state':'الحالة',
            'task':'المهمة',
            'reason':''
        }
        widgets={
            'state':Select(attrs={'class': "form-label", 'class': "form-control",'placeholder':'حالة الانجاز'}),
            'reason':Textarea(attrs={'class': "form-label", 'class': "form-control",'placeholder':'ملاحظات إضافية'}),

        }
class AddEmployeeForm(ModelForm):
    class Meta:
        model = EmployeeAdd
        fields = '__all__'
        widgets = {
            'full_name':TextInput(attrs={'class': "form-label", 'class': "form-control",'placeholder':'الاسم الكامل'}),
            'job_status':TextInput(attrs={'class': "form-label", 'class': "form-control",'placeholder':'المسمى الوظيفي'})
        }





