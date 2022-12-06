from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import TaskForm,AddUserForm,UpdateForm
from .models import TaskAssighn
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










def completed(request):
    return render(request, 'tasks/finished_tasks.html', {})



class AddUserView(CreateView):
    form_class = AddUserForm
    success_url = 'index'
    template_name = 'tasks/add_user.html'

def thank_you(request):
    return render(request,'tasks/thank_you.html')


class UpdateUserView(UpdateView):
    model = User
    form_class = AddUserForm
    success_url = reverse_lazy('index')
    template_name = 'tasks/add_user.html'

class UpdateStatus(UpdateView):
    model = TaskAssighn
    form_class = UpdateForm
    template_name = 'tasks/taskassighn_form.html'
    success_url = reverse_lazy('index')

def delete_task(request,pk):
    task = TaskAssighn.objects.get(pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request,'tasks/delete.html',{'task':task})


def update_task(request,pk):
    upadte_form = TaskAssighn.objects.get(pk=pk)
    form = TaskForm(instance=upadte_form)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=upadte_form )
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'tasks/taskassighn_form.html',{'form':form})