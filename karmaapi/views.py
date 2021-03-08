from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignUpForm
from django.views import View
from. models import Profile
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ProfileForm

# Create your views here.


def book(request):
    queryset=Profile.objects.all()
    context={
        "form":queryset
    }
    return render(request,"abc.html",context)
class index(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request,self.template_name)

# class login(View):
#     template_name='login.html'
#
#     def get(self,request):
#         return render(request,self.template_name)

class blog(View):
    template_name='blog.html'
    def get(self,request):
        return render(request,self.template_name)

class cart(View):
    template_name='cart.html'

    def get(self,request):
        return render(request,self.template_name)

class category(View):
    template_name='category.html'

    def get(self,request):
        return render(request,self.template_name)

class checkout(View):
    template_name='checkout.html'

    def get(self,request):
        return render(request,self.template_name)

class confirm(View):
    template_name='confirmation.html'

    def get(self,request):
        return render(request,self.template_name)

class contact(View):
    template_name='contact.html'

    def get(self,request):
        return render(request,self.template_name)

class elements(View):
    template_name='elements.html'

    def get(self,request):
        return render(request,self.template_name)

class singleblog(View):
    template_name='single-blog.html'

    def get(self,request):
        return render(request,self.template_name)

class singleproduct(View):
    template_name='single-product.html'

    def get(self,request):
        return render(request,self.template_name)

class tracking(View):
    template_name='tracking.html'

    def get(self,request):
        return render(request,self.template_name)

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html',{'form': form})

    
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)