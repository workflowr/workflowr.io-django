from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("workflowr - organized + reproducible + shareable data science in R")
