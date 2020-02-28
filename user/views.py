from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username = username , password = password)
        if user is not None:
            auth.login(request,user)
            print("giriş başarılı")
            return redirect('index')
        else:
            print("Kullanıcı adı veya şifre yanlış")
            return redirect('login')
    else:
        return render(request,'user/login.html')

def register(request):
    if request.method == "POST":
        print("Onaylandı")
        #formdan bilgileri alma
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            #username kontrol
            if User.objects.filter(username = username).exists():
                print("Kullanıcı adı alınmış")
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    print("e posta adresi kullanılıyor")
                    return redirect('register')
                else:
                    #kayıt işlemi
                    user = User.objects.create_user(username=username,password = password,email = email)
                    user.save
                    print('Kullanıcı oluşturuldu')
                    return redirect('login')
        else:
            print("Parolalar eşleşmiyor")
        return redirect('register')
    else:
        return render(request, 'user/register.html')


def logout(request):
    return render(request,'user/logout.html')