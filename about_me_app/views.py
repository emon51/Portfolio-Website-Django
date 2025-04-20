from django.shortcuts import render, HttpResponse, redirect
from . models import About, Skills
from django.contrib.auth.forms import UserCreationForm as user_form 
from . forms import AboutForm, SkillForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'html/index.html', context = {})


def home(request):
    try:
        objects = About.objects.first()
    except:
        objects = None 
    return render(request, 'html/home.html', context = {'objects': objects})


def about(request):
    try:
        objects = About.objects.first()
    except:
        objects = None 
    return render(request, 'html/about_me.html', context = {'objects': objects})


def education(request):
    try:
        objects = About.objects.first()
    except:
        objects = None 
    return render(request, 'html/education.html', context = {'objects': objects})


def contact(request):
    try:
        objects = About.objects.first()
    except:
        objects = None 
    return render(request, 'html/contact.html', context = {'objects': objects})


def skill(request):
    try:
        objects = Skills.objects.first()
    except:
        objects = None 
    return render(request, 'html/skills.html', context = {'objects': objects})


def project(request):
    try:
        projects = Skills.objects.first().projects 
    except:
        projects = []
    return render(request, 'html/project.html', context = {'projects': projects})


def signup(request):
    if request.method == 'POST':
        form = user_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = user_form()
    return render(request, 'registration/signup.html', context = {'form': form})



@login_required
def add_data(request):
    if request.method == 'POST':
        about_form = AboutForm(request.POST)
        skill_form = SkillForm(request.POST)
        if about_form.is_valid() and skill_form.is_valid():
            about_form.save()
            skill_form.save()
            return redirect('home')

    else:
        about_form = AboutForm()
        skill_form = SkillForm()
    return render(request, 'html/add_data.html', context = {'about_form': about_form, 'skill_form': skill_form})



@login_required
def update_data(request):
    try:
        about_instance = About.objects.first()
        skill_instance = Skills.objects.first()
    except:
        return HttpResponse("No data found to update.")

    if request.method == 'POST':
        about_form = AboutForm(request.POST, instance=about_instance)
        skill_form = SkillForm(request.POST, instance=skill_instance)
        if about_form.is_valid() and skill_form.is_valid():
            about_form.save()
            skill_form.save()
            return redirect('home')
    else:
        about_form = AboutForm(instance = about_instance)
        skill_form = SkillForm(instance = skill_instance)

    return render(request, 'html/update_data.html', context={'about_form': about_form, 'skill_form': skill_form})


@login_required
def delete_all_data(request):
    try:
        About.objects.all().delete()
        Skills.objects.all().delete()
        return redirect('home')
    except:
        return HttpResponse("No data found to Delete.")