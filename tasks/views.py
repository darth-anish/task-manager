from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ProjectForm, TaskForm
from .models import Project, Task
from pdb import set_trace

@login_required(login_url='accounts/login')
def home(request):
    return render(request, 'tasks/home.html')

@login_required(login_url='accounts/login')
def get_project(request, pk):
    project = get_object_or_404(Project, id=pk)
    return render(request, 'tasks/project_detail.html', {'project': project})

@login_required(login_url='accounts/login')
def create_project(request):
 
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save(user=request.user)  # Pass the current user to the model
            form.save_m2m() 
            return redirect('tasks:project_detail', project.id)
    else:
        form = ProjectForm()
    users = User.objects.all()

    return render(request, 'tasks/create_project.html',{'form':form, 'users':users})

@login_required(login_url='accounts/login')
def get_all_projects(request):
    user = request.user
    projects = Project.objects.filter(members=user)
    return render(request, 'tasks/all_projects.html', {'projects':projects})

@login_required(login_url='accounts/login')
def update_project(request, pk):
    project = get_object_or_404(Project, id=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save()
            messages.success(request,'Project updated successfully')
            # redirect_url = 
            return render(request, 'tasks/project_detail.html', {'project': project})
        else:
            messages.error(request, 'Invalid form data')
            return render(request, f'tasks:projects/{pk}', {'form': form, 'project': project})
    else:
        form = ProjectForm(instance=project)

    return render(request,'tasks/edit_project.html', {'form': form, 'project': project})