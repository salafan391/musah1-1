from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import TaskForm,AddUserForm,UpdateForm,CreateStatus
from .models import TaskAssighn,TaskStatus
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView
# Create your views here.


def index(request):
    task = TaskAssighn.objects.all().order_by('-created_at')
    return render(request, 'tasks/index.html', {
        'tasks': task,
    })


class TaskAddView(CreateView):
    model = TaskAssighn
    form_class = TaskForm
    success_url = reverse_lazy('index')


def list_task(request):
    tasks = TaskAssighn.objects.all()
    return render(request, 'tasks/list_tasks.html', {'tasks': tasks})


def task_detail(request, pk):
    task = TaskAssighn.objects.get(pk=pk)
    return render(request, 'tasks/detail.html', {
        'task': task,
    }
        )
class CreateStatusView(CreateView):
    template_name = 'tasks/task_status.html'
    model = TaskStatus
    form_class = CreateStatus
    success_url = reverse_lazy('thank_you')




def completed(request):
    acc = TaskAssighn.objects.filter(status=acc)
    return render(request, 'tasks/finished_tasks.html', {'accs': acc})



class AddUserView(CreateView):
    form_class = AddUserForm
    success_url = 'index'
    template_name = 'tasks/add_user.html'

def thank_you(request):
    return render(request,'tasks/thank_you.html')


class UpdateUserView(UpdateView):
    model = User
    form_class = AddUserForm
    success_url = '/thank_you'
    template_name = 'tasks/add_user.html'

class UpdateStatus(UpdateView):
    model = TaskAssighn
    form_class = UpdateForm
    template_name = 'tasks/taskassighn_form.html'
    success_url = '/thank_you'

def delete_task(request,pk):
    task = TaskAssighn.objects.get(pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('thank_you')
    return render(request,'tasks/delete.html',{'task':task})