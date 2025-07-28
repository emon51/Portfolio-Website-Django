

from django.forms import ModelForm
from . models import About, Skills

class AboutForm(ModelForm):
    class Meta:
        model = About
        fields = '__all__'

class SkillForm(ModelForm):
    class Meta:
        model = Skills 
        fields = '__all__'