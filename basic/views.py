from django.shortcuts import render, redirect
from django.http import HttpResponse
from experience.models import Experience
from category.models import Category


def home(request):
    categories = Category.objects.all()
    education_experiences = Experience.objects.filter(is_working=0)
    working_experiences = Experience.objects.filter(is_working=1)
    data = {
        'categories': categories,
        'education_experiences': education_experiences,
        'working_experiences': working_experiences,
    }
    return render(request, 'home.html', context=data)

