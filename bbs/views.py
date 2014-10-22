from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.contrib.auth.forms import *
# Create your views here.
def index(request):
    return render_to_response('index.html')

def home(request):
    return render_to_response('home.html')

def signup(request):
    form = UserCreationForm()
    if request.method == 'GET':
        return render_to_response('register.html',{'form':form},context_instance=RequestContext(request))
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return redirect("/index")
        return render_to_response('register.html',{'form':form},context_instance=RequestContext(request))

#def signin(request):
