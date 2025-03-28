from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

def project_list(request):
    project_data = Project.objects.all()
    for i in range(len(project_data)):
        project_data[i].skills = project_data[i].skills.splitlines()

    context = {
        'page_name': 'projects',
        'project_data': project_data
    }
    return render(request, 'browse.html', context)

def career(request):
    page_name = 'career'
    return render(request, 'career.html', locals())

def profile(request):
    page_name = 'profile'
    return render(request, 'profile.html', locals())

def hobbies(request):
    page_name = 'hobbies'
    return render(request, 'hobbies.html', locals())

@login_required(login_url='/admin/login/')
def upload_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = ProjectForm()
    return render(request, 'upload.html', {'form': form})

def upload_success(request):
    return HttpResponse('successfully uploaded')

def alien_world_details(request):
    page_name = 'alien_world_details'
    return render(request, 'alien_world_details.html', locals())