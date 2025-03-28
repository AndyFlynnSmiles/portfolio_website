from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name=''),
    path('projects/', views.project_list, name='projects'),
    path('career/', views.career, name='career'),
    path('hobbies/', views.hobbies, name='hobbies'),
    path('profile/', views.profile, name='profile'),
    path('OpenGL_2_Alien_World/', views.alien_world_details, name='OpenGL 2 Alien World'),
    path('test_name_here/', views.project_list, name='test name here'),
    path('upload_project/', views.upload_project, name='upload_project'),
    path('upload_success/', views.upload_success, name='upload_success'),
]