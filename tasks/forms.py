from django.forms import *
from .models import TaskAssighn,TaskStatus
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'hi',
        }
))

class TaskForm(ModelForm):
    class Meta:
        model = TaskAssighn
        exclude=['status','reason']
        labels = {
            'task_desc': '',
            'author': '',
            'created_at': "تم الإنشاء بتاريخ",
            'updated_at': "تم الإنشاء بتاريخ",
            'time_start': "بدء المهمة",
            'time_end': "نهاية المهمة",
        }
        widgets = {
            'task_desc': TextInput(attrs={'class': "form-label", 'class': "form-control",'placeholder':'وصف المهمة'}),
            'time_start': DateTimeInput(attrs={'type': 'datetime-local', 'class': "form-label", 'class': "form-control",'placeholder':'بدء المهمة'}),
            'time_end': DateTimeInput(attrs={'type': 'datetime-local', 'class': "form-label", 'class': "form-control",'placeholder':'نهاية المهمة'}),
            'url':URLInput(attrs={'class': "form-label", 'class': "form-control",'placeholder':
            'رابط الملفات على الدرايف'}),

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
        widgets={
            'reason':Textarea(attrs={'class': "form-label", 'class': "form-control",'pleceholder':'في حال عدم الإنجاز يرجى ذكر السبب','helptext':'اذكر السبب'})
        }

class CreateStatus(ModelForm):
    class Meta:
        model = TaskStatus
        fields = '__all__'
        widgets={
            'state':TextInput(attrs={'class': "form-label", 'class': "form-control",'placeholder':'حالة الانجاز'}),
        }
