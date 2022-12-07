from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('task_add/',views.TaskAddView.as_view(),name='task_add'),
    path('task_add/<int:pk>/update',views.UpdateStatus.as_view(),name='update_status'),
    path('task_add/<int:pk>/update_task',views.update_task,name='update_task'),
    path('task_add/<int:pk>/update_url',views.update_url,name='update_url'),
    path('task_add/finished',views.completed,name='completed'),
    path('add_user/',views.AddUserView.as_view(),name='user'),
    path('thank_you/',views.thank_you,name='thank_you'),
    path('add_user/<int:pk>/update',views.UpdateUserView.as_view(),name='update_user'),
    path('add_user/delete/<int:pk>',views.delete_task,name='delete'),  
]
