from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
    
def index(request):
    template = loader.get_template('home/tools.html')
    return HttpResponse(template.render())
