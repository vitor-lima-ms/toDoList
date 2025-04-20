from django.urls import path

from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TaskListView, name='taskList'),

    path('create/', views.TaskCreateView, name='taskCreate'),

    path('search-not-completed/', views.searchTaskNotCompleted, name='taskSearchNotCompleted'),

    path('complete/<int:task_id>/', views.completeTask, name='completeTask'),

    path('delete/<int:task_id>/', views.deleteTaskList, name='deleteTaskList'),

    path('delete/<int:task_id>/', views.deleteTaskCompleted, name='deleteTaskCompleted'),

    path('work/', views.workTasks, name='workTasks'),

    path('studies/', views.studiesTasks, name='studiesTasks'),
    
    path('personal/', views.personalTasks, name='personalTasks'),
    
    path('shopping/', views.shoppingTasks, name='shoppingTasks'),

    path('other/', views.otherTasks, name='otherTasks'),

    path('completed/', views.completedTasks, name='completedTasks'),

    path('search-completed/', views.searchTaskCompleted, name='taskSearchCompleted'),
]
