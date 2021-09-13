from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'rexeonapp/home.html')

def about(request):
    return render(request,'rexeonapp/about.html')

def blog(request):
    return render(request,'rexeonapp/blog.html')
