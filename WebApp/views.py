from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegisterForm #UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

#create your views here

app_name = 'WebApp'


def index(request):
    return render(request, 'webapp/home.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}, Please login")
            login(request, user)
            return redirect('login')

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request=request,
                          template_name="registration/registration.html",
                          context={"form": form})

    form = UserRegisterForm()

    return render(request = request,
                  template_name = "registration/registration.html",
                  context={"form":form})

@login_required
def profile(request):
 #   u_form = UserUpdateForm()
  #  p_form = ProfileUpdateForm()

   # context = {
    #    'u_form': u_form,
     #   'p_form' : p_form
    #}
    return render(request = request,
                  template_name= "registration/profile.html",
                  )

