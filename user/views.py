from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
def signup(request):
    if request.method == 'POST':


        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            usr = User.objects.get(username=username, email=email)
            usr.email = email
            usr.first_name = first_name
            usr.last_name = last_name
            usr.save()
            return redirect('todo')
            # return render(request, 'user/signup.html', {'form':form})

    else:
        form = SignUpForm()

    return render(request, 'user/signup.html', {'form': form})






def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    valuenext =  request.POST.get('next')
    if request.method == 'POST':

        usrname = request.POST['username']
        passwd = request.POST['password']

        user = authenticate(request, username=usrname, password=passwd)  # None
        if user is not None and valuenext=='':
            login(request, user)
            context= {
                      'valuenext': valuenext}
            return redirect('todo')
        elif user is not None and valuenext !='':
        	login(request, user)
        	context = {
        	'valuenext': valuenext}
        	return redirect(valuenext)

        elif not User.objects.filter(username=usrname).exists():
            messages.warning(
                request, f'Please enter a correct username and password. Note that both fields may be case-sensitive.')
            return redirect('login')
        else:
            messages.warning(
                request, f'Please enter a correct username and password. Note that both fields may be case-sensitive.')
            return redirect('login')

    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})