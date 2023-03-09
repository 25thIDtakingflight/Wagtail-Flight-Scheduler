from django.shortcuts import render

# Create your views here.
# in views.py

from django.shortcuts import render
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard') # replace 'dashboard' with your desired redirect URL
        else:
            error_msg = 'Incorrect username or password'
            return render(request, 'login.html', {'error_msg': error_msg})
    else:
        return render(request, 'login.html')
