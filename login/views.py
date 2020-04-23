import hashlib

from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.http import StreamingHttpResponse, JsonResponse
from django.urls import reverse
from . import models as login_models
from . import forms

def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()

def ins(request):
    return redirect(reverse('login'))

def login(request):
    login_form = forms.UserForm()
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        if login_form.is_valid():
            try:
                username = login_form.cleaned_data['username']
            except:
                message = "账号无效"
                return render(request, 'login/login.html', locals())
            password = login_form.cleaned_data['password']
            try:
                user = login_models.User.objects.get(username=username)
                if user.password == password:
                    try:
                        request.session['is_login'] = True
                        request.session['username'] = user.username # 之后可以通过session的username查询获取user的information
                        return redirect(reverse('index'))
                    except:
                        message="session wrong"
                else:
                    message = "密码错误"
            except:
                message = "用户不存在"
    return render(request,'login/login.html',locals())

def register(request):
    register_form = forms.RegisterForm()
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写内容"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            if password1 != password2:
                message = "两次输入密码不同"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = login_models.User.objects.filter(username=username)
                if same_name_user:
                    message = "用户已经存在，请重新选择用户名"
                    return render(request, 'login/register.html', locals())
                same_email_user = login_models.User.objects.filter(email=email)
                if same_email_user:
                    message = "该邮箱地址已被注册，请使用别的邮箱"
                    return render(request, 'login/register.html', locals())

                # everything ok,then creat new account

                new_user = login_models.User()
                new_user.username = username
                new_user.password = password1
                new_user.email = email
                new_user.save()
                return redirect(reverse('login'))
    return render(request, 'login/register.html', locals())

def index(request):
    message=request.session.get('username',"abc")
    return render(request,'login/index.html',locals())