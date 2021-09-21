from django.shortcuts import render,redirect
from rexeonapp.models import Blog
from rexeonapp.forms import Get_in_touchForm
from rexeonapp.forms import ApplyForm
from django.views import generic
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def home(request):
    return render(request,'rexeonapp/home.html')

def about(request):
    return render(request,'rexeonapp/about.html')

def group(request):
    return render(request,'rexeonapp/group.html')

def service(request):
    return render(request,'rexeonapp/services.html')

def career(request):
    return render(request,'rexeonapp/career.html')

def contact(request):
    form = Get_in_touchForm()
    if request.method == 'POST':
        form = Get_in_touchForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/contact')
    return render(request,'rexeonapp/contact.html',{'form':form})

def apply_form(request):
    form = ApplyForm()
    if request.method == "POST":
        form = ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/career')
    return render(request,'rexeonapp/apply.html',{'form':form})

class blog(generic.ListView):
    model = Blog
    blog_list = Blog.objects.all()
    # img = Blog.objects.filter(image='image')
    # print(img)
    paginate_by=6
    template_name = 'rexeonapp/blog.html'

class blog_detail(generic.DetailView):
    model = Blog
    blog_list = Blog.objects.all()
    template_name = 'rexeonapp/blog_detail.html'


#id - rexeonsolutions
#password - rexeon123
#email - rexeon@gmail.com




