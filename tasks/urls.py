from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('task_add/',views.TaskAddView.as_view(),name='task_add'),
    path('list_task',views.list_task,name='list'),
    path('task_detail/<int:pk>/',views.task_detail,name='task_detail'),
    path('task_add/<int:pk>/update',views.UpdateStatus.as_view(),name='update_status'),
    path('task_add/finished',views.completed,name='completed'),
    path('add_user/',views.AddUserView.as_view(),name='user'),
    path('thank_you/',views.thank_you,name='thank_you'),
    path('add_user/<int:pk>/update',views.UpdateUserView.as_view(),name='update_user'),
    path('add_user/delete/<int:pk>',views.delete_task,name='delete'),
    path('status/',views.CreateStatusView.as_view(),name='status'),
]
