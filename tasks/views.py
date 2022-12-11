from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView
from django.db.models import Q
# Create your views here.


def index(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    tasks = TaskAssighn.objects.filter(
        Q(task_desc__icontains=q)|
        Q(employee__job_status__icontains=q)|
        Q(status__state__icontains=q)|
        Q(reason__icontains=q)
    )
    complete = TaskStatus.objects.get(pk=5)
    incomplete = TaskStatus.objects.get(pk=3)
    return render(request, 'tasks/index.html', {
        'tasks': tasks,
        'complete':complete,
        'incomplete':incomplete
    })


class TaskAddView(CreateView):
    model = TaskAssighn
    form_class = TaskForm
    success_url = reverse_lazy('index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = TaskAssighn.objects.all().order_by('-id')[0]
        return context
        


def completed(request):
    complete = TaskStatus.objects.get(pk=5)
    acc = complete.taskassighn_set.all()
    return render(request, 'tasks/finished_tasks.html', {'complete':acc})

def incompleted(request):
    incomplete = TaskStatus.objects.get(pk=3)
    acc = incomplete.taskassighn_set.all()
    return render(request, 'tasks/unfinished_tasks.html', {'incomplete':acc})


class AddUserView(CreateView):
    form_class = AddUserForm
    success_url = 'index'
    template_name = 'tasks/add_user.html'


def thank_you(request):
    return render(request, 'tasks/thank_you.html')


class UpdateUserView(UpdateView):
    model = User
    form_class = AddUserForm
    success_url = reverse_lazy('index')
    template_name = 'tasks/add_user.html'



def delete_task(request, pk):
    task = TaskAssighn.objects.get(pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request, 'tasks/delete.html', {'task': task})


def update_task(request, pk):
    upadte_form = TaskAssighn.objects.get(pk=pk)
    form = TaskFormUpdate(instance=upadte_form)
    if request.method == 'POST':
        form = TaskFormUpdate(request.POST,instance=upadte_form )
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'tasks/taskassighn_form.html',{'form':form})


class AddEmployeeView(CreateView):
    model = EmployeeAdd
    form_class = AddEmployeeForm
    success_url = reverse_lazy('index')
    template_name = 'tasks/add_employee.html'



