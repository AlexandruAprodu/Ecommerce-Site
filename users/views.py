from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib.messages import success, info
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse


@csrf_exempt
def register(request):
    if request.method == 'POST':
        user = RegistrationForm(request.POST)
        if user.is_valid():
            user.save()
            success(request, 'Te-ai inregistrat cu succes! Acum te poti loga !')
            return redirect(reverse('users:login'))
    else:
        user = RegistrationForm()
    return render(request, 'users/register.html', {'user': user})


