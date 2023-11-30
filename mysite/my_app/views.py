from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template("my_app/index.html")
    return HttpResponse(template.render({}, request))