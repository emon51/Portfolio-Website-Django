
from django.urls import path
from about_me_app import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('home/', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('education/', views.education, name = 'education'),
    path('contact/', views.contact, name = 'contact'),
    path('skill/', views.skill, name = 'skill'), 
    path('project/', views.project, name = 'project'),
    
    path('signup/', views.signup, name = 'signup'), 
    path('add-data/', views.add_data, name = 'add-data'),
    path('update-data/', views.update_data, name = 'update-data'),
    path('delete-all-data/', views.delete_all_data, name = 'delete-all-data'),
]