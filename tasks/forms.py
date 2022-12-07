from django.forms import *
from .models import TaskAssighn,TaskStatus
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
            'url':'',
            'task_number':''
        }
        error_messages={
            'enter a number':'يجب أن تدخل رقما'
        }
        widgets = {
            'task_number':NumberInput(attrs={'class': "form-label", 'class': "form-control",'placeholder':'رقم المهمة'}),
            'task_desc': TextInput(attrs={'class': "form-label", 'class': "form-control",'placeholder':'وصف المهمة'}),
            'url':URLInput(attrs={'class': "form-label", 'class': "form-control",'placeholder':
            'رابط الملفات على الدرايف'}),
        }

class TaskFormUpdate(ModelForm):
    class Meta:
        model = TaskAssighn
        fields='__all__'
        labels = {
            'task_desc': '',
            'created_at': "تم الإنشاء بتاريخ",
            'updated_at': "تم الإنشاء بتاريخ",
            'url':'',
            'task_number':'',
            'status':'الحالة',
            'reason':'ملاحظات'
        }
        
        widgets = {
            'task_number':NumberInput(attrs={'class': "form-label", 'class': "form-control",'placeholder':'رقم المهمة'}),
            'task_desc': TextInput(attrs={'class': "form-label", 'class': "form-control",'placeholder':'وصف المهمة'}),
            'url':URLInput(attrs={'class': "form-label", 'class': "form-control",'placeholder':
            'رابط الملفات على الدرايف'}),
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
class UpdateForm(ModelForm):
    class Meta:
        model = TaskAssighn
        fields = ['status','reason']
        labels={
            'status':'الحالة',
            'reason':'ملاحظات إضافية'
        }
        widgets={
            'reason':Textarea(attrs={'class': "form-label", 'class': "form-control"})
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
            'state':SelectMultiple(attrs={'class': "form-label", 'class': "form-control",'placeholder':'حالة الانجاز'}),
            'reason':Textarea(attrs={'class': "form-label", 'class': "form-control",'placeholder':'ملاحظات إضافية'}),

        }
class UpdateUrl(ModelForm):
    class Meta:
        model = TaskAssighn
        fields = ['url']
        labels = {
            'url':''
        }
        widgets={
            'url':URLInput(attrs={
                'class': "form-label",
                 'class': "form-control",'placeholder':'رابط الملف'})

            
        }