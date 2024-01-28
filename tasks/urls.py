from django.urls import path 

from . import views

app_name = "tasks"

urlpatterns = [
    path('', views.home, name='home'),
    path('create/project/', views.create_project, name='create_project'),
    path('projects/<int:pk>', views.get_project, name='project_detail'),
    path('projects/', views.get_all_projects, name='list_projects'),
    path('update/project/<int:pk>/', views.update_project, name='update_article')
]

# path('delete/article/<int:pk>/', views.delete_article, name='delete_article')