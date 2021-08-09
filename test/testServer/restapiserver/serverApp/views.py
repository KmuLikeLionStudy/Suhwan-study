from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import User

# Create your views here.

def register(request):
    if request.methed == "GET":
        return render(request, 'register.html')

    elif request.method == "POST":
        username = request.POST.get['username', None]
        password = request.POST.get['password', None]
        re_password = request.POST.get['re_password', None]
        res_data = {}
        if not (username and password and re_password):
            res_data['error'] = "값을 다 채우십시오"
        if password != re_password:
            res_data['error'] = "비밀번호가 다릅니다."
        else :
            user = User(username = username, password = make_password(password))
            user.save()
        return render(request, 'register.html', res_data)

def login(request):
    response_data = {}

    if request.method == "GET":
        return render(request, 'login.html')

    elif request.method == "POST":
        login_username = request.POST.get('username',None)
        login_password = request.POST.get('password',None)

        if not (login_username and login_password):
            response_data['error']="아이디와 비번 둘다 입력하셈"
        else:
            User = User.objects.get(username = login_username)
            if check_password(login_password, User.password):
                request.session['user'] = User.id
                return redirect('/')
            else :
                response_data['error'] = "비번이 틀렸습니다"
        return render(request, 'login.html', response_data)

def home(request):
    user_id = request.session.get('User')
    if user_id :
        User_info = User.objects.get(pk=user_id)
        return HttpResponse(User_info.username)
    return HttpResponse('로그인 해주세요')

def logout(request):
    request.session.pop('User')
    return redirect('/')