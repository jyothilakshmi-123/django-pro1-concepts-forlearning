from django.shortcuts import render
# from django.http import HttpResponse

def index(request):
    return render(request,'home.html',{'name':'jyothi'})


# Create your views here.
