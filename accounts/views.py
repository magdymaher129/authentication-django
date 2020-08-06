from django.contrib.auth.forms import UserCreationForm 
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth  import login as auth_login
from.forms import SignupForm,loginForm
from django.contrib.auth import authenticate, login,logout as logout_user
def signup(request):
   form= SignupForm()

   if request.method == "POST" :
      form=SignupForm(request.POST)

      if form.is_valid():
         user=form.save()
         auth_login(request,user)

         return redirect('home')
        
   context =      {
    'form':form
    }
   template='signup.html'
   return render(request,template,context)


def login (request):
    form= loginForm()
    template='login.html'
    context =      {
    'form':form
    }
    return render(request,template,context)
        # Return an 'invalid login' error message.
  
def loginBackend(request):
    template='home.html'
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login( request)
        context =      {
       'user':user
       }
        return render(request,template,context)
        # Redirect to a success page.
        ...
    else:
         return redirect('signup')

def logout(request):
   logout_user(request)
   return redirect('login')
