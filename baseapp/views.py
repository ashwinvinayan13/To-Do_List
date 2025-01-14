from django.shortcuts import render, redirect
from django.http import HttpResponse
from baseapp.models import Taskdb, RegisterDB
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.


def demo(request):
    return HttpResponse('demo')

def task(request):
    if request.user.is_authenticated:
        task = Taskdb.objects.filter(user=request.user)
        return render(request, 'todo/tasks.html', {'task': task})
    else:
        return redirect(log_in)

def save_task(request):
    if request.method == 'POST':
        tas = request.POST.get('task')
        dec = request.POST.get('des')
        Taskdb.objects.create(user=request.user, title=tas, description=dec)
        return redirect(task)

def update_task(request, t_id):
    data = Taskdb.objects.get(id=t_id)
    if request.method == 'POST':
        tas = request.POST.get('task')
        dec = request.POST.get('des')
        com = 'complete' in request.POST
        Taskdb.objects.filter(id=t_id).update(title=tas, description=dec, complete=com)
        return redirect(task)
    return render(request, 'todo/update_task.html', {'data': data})

def delete(request, t_id):
    tas = Taskdb.objects.get(id=t_id)
    tas.delete()
    return render(request, 'todo/delete.html', {'tas': tas, 'delet': tas})

def register_user(request):
    if request.method == 'POST':
        nam = request.POST.get('name')
        pas = request.POST.get('pass')
        cpa = request.POST.get('cpass')
        ema = request.POST.get('email')

        if pas == cpa:
            user = User.objects.create_user(username=nam, email=ema, password=pas)
            user.save()
            return redirect(log_in)
        else:
            return render(request, 'todo/Register_user.html')
    return render(request, 'todo/Register_user.html')


def log_in(request):
    return render(request, 'todo/Login.html')

def logu(request):
    if request.method == 'POST':
        use = request.POST.get('username')
        pas = request.POST.get('password')
        user = authenticate(request, username=use, password=pas )

        if user is not None:
            login(request, user)
            return redirect(task)
        else:
            return render(request, 'todo/Login.html', {'error': 'Invalid Username or Password'})
    return render(request, 'todo/Login.html')



def register_user(request):
    return render(request, 'todo/Register_user.html')

def logout(request):
    logout(request)
    return redirect(log_in)
