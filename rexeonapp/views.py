from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'rexeonapp/home.html')

def about(request):
    return render(request,'rexeonapp/about.html')

def blog(request):
    return render(request,'rexeonapp/blog.html')

def group(request):
    return render(request,'rexeonapp/group.html')

def service(request):
    return render(request,'rexeonapp/services.html')

def career(request):
    return render(request,'rexeonapp/career.html')

def contact(request):
    return render(request,'rexeonapp/contact.html')
