from django.shortcuts import render, redirect, HttpResponseRedirect, render_to_response
from django.contrib.auth import authenticate, login, logout     # 登入和登出
from django.contrib.auth.decorators import login_required       # 验证用户是否登录
from django.contrib.auth.models import User
from online.models import UserProfile


# Create your views here.
def acc_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print('收到的信息')
        print(username)
        print(password)

        # 类型为<class 'django.contrib.auth.models.User'>
        user = authenticate(username=username, password=password)

        print('打印user')

        print(user)

        # print(type(models.Customer.objects.get(name="赵凡")))
        # print(user,type(user))
        if user:
            print('验证成功')
            login(request, user)  # 验证成功之后登录\
            print('设置cookie')

            # 设置session-----------------------------------------------------
            # request.session['username'] = username
            # return HttpResponseRedirect('/index')

            # 设置cookie------------------------------------------------------
            response = HttpResponseRedirect('/index')
            response.set_cookie('username', username, 600)
            flag = 'success'
            response.set_cookie('flag', flag)
            return response

        else:

            print('登录错误')
            return HttpResponseRedirect('/page_error')

    return render(request, "login.html")


def acc_logout(request):

    print('注销用户')

    # 设置cookie-------------------------------------------------------------
    response = HttpResponseRedirect('/login')
    response.delete_cookie('username')
    response.delete_cookie('flag')
    logout(request)  # 登出
    return response
    # session---------------------------------------------------------------
    # username = request.session.get('username', 'anybody')
    # return render_to_response('/login/', {'username': username})


def add_user(request):

    # user = authenticate(username='liyong', password='123456')
    user = User.objects.create_user(username='han', email='han@163.com', password='123456')

    # if user:
    #     print('用户存在')
    #     return HttpResponseRedirect('/add_user_url')
    # else:
    #     print('新建原始用户')
    #     user = User.objects.create_user(username='liyong', email='liyonglovely@qq.com', password='123456')

    # print('打印用户名')
    # print(user[0].username)
    # print('打印用户密码')
    # print(user[0].password)
    # print('打印用户邮箱')
    # print(user[0].email)
    # 到这里，user 这一个User对象已经保存于数据库中了。
    # 你可以继续修改它的属性。
    # 例如修改user的last_name
    # user_list = User.objects.all()
    user.last_name = 'li'
    user.save()
    # return render(request, 'add_user.html', {'name_list': user_list})
    return render(request, 'page5.html')


def register(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        flag = authenticate(username=username, password=password)
        print('打印用户名')
        print(username)
        print('打印用户密码')
        print(password)
        if flag:
            print('用户存在')
            print('打印flag')
            print(flag)
            return HttpResponseRedirect('/page2')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            UserProfile.objects.create(user=user, name='李勇', tel='13334454355', adds='a', city='s',postCode=100876)
            user.save()
            print('注册成功')
            return HttpResponseRedirect('/page3')
        # 到这里，user 这一个User对象已经保存于数据库中了。
        # 你可以继续修改它的属性。
        # 例如修改user的last_name
        # user_list = User.objects.all()
        # user.last_name = 'Lennon'
        # user.save()
    # return render(request, 'register.html', {'name_list': user_list})
    return render(request, 'register.html')


def page_error(request):
    return render(request, "page_error.html")


@login_required  # 加上这个装饰器就是限制必须登录才能执行这个函数
def index(request):
    username = request.COOKIES.get('username', '')
    # show_name = User.objects.get(username='z').userprofile.name
    return render_to_response("index.html", {'username': username})


@login_required  # 加上这个装饰器就是限制必须登录才能执行这个函数
def page1(request):
    return render(request, "page1.html")


@login_required
def page2(request):
    return render(request, "page2.html")


@login_required
def page3(request):
    return render(request, "page3.html")


@login_required
def page4(request):
    return render(request, "page4.html")


@login_required
def page5(request):
    return render(request, "page5.html")
