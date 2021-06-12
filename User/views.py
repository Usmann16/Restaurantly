# -*- coding: utf-8 -*-
from __future__ import unicode_literals



from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.template.defaultfilters import safe
from vendor.models import addDeal , restuarantInformation
from .models import review, reply,contacts
from django.views.generic import ListView
from .templatetags import extra




def logout(request):
    auth.logout(request)
    return render(request, 'index.html')

def index(request):
    if request.method == 'POST':
        foodtype = request.POST['foodtype']


        if restuarantInformation.objects.all().filter(FoodType__icontains=foodtype).exists():
            obj = restuarantInformation.objects.all().get(FoodType__icontains=foodtype)
            print(obj.Name)
            return redirect('restaurantList.html', {'obj': obj})

        else:
            message = "*No restuarant information exit related to"+foodtype
            return render(request, 'index.html', {'message': message})
    else:
        return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(request, username=email, password=password)
        # print(user.is_active)
        # print(user.is_staff)
        if user is not None:
            auth.login(request,user)
            if user.is_staff == True:
                if restuarantInformation.objects.filter(Email=request.user.email).exists():
                    obj = restuarantInformation.objects.get(Email=request.user.email)
                    return render(request, 'informationForms.html', {'context':obj})
                return render(request,'informationForms.html')
            else:
                return render(request, 'index.html')
        else:
            message = "*Invalid Credentials"
            return render(request, 'login.html', {'message': message})

    else:

        return render(request, 'login.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        obj = contacts.objects.create(name=name, email=email, subject=subject, message=message)
        obj.save()
        alert = "Your message is send to Admin."
        return render(request, 'contactUs.html', {'alert':alert})
    return render(request, 'contactUs.html')

def restaurantList(request):
    if request.POST.get('filter') == 'Apply Filter':
        event = request.POST.getlist('event')
        payment = request.POST.getlist('payment')
        if not event and not payment:
            return render(request,'restaurantList.html')

        if event is not None:
            for i in event:
                counter = 0
                obj = restuarantInformation.objects.all().filter(Event__icontains=event[counter])
                counter = counter+1
        if payment is not None:
            for i in payment:
                counter = 0
                obj = restuarantInformation.objects.all().filter(PaymentMethod__icontains=payment[counter])
                counter = counter+1
        return render(request, 'restaurantList.html', {'obj': obj})
    else:
        foodtype = request.POST.get('foodtype')
        print(foodtype)
        obj = restuarantInformation.objects.all().filter(FoodType__icontains=foodtype)
        return render(request, 'restaurantList.html', {'obj': obj})









def reviews(request):
    if request.method == 'POST':
        name = request.POST['res_name']
        username = request.user.username
        subject = request.POST['subject']
        message = request.POST['message']

        user_obj = User.objects.get(username=username)
        res_obj = restuarantInformation.objects.get(Name=name)

        user = review.objects.create(user=user_obj, res_name=res_obj, title=subject, reviews=message)
        user.save
        res = restuarantInformation.objects.all().get(Name=name)
        comments = review.objects.all().filter(res_name=name)

        if review.objects.filter(res_name=name).exists():
            obj = review.objects.all().filter(res_name=name)
            rep = []
            for i in obj:
                if reply.objects.filter(user_id=i.u_id).exists():
                    rep = reply.objects.all().filter(user_id=i.u_id)

        if addDeal.objects.filter(Email=name).exists():
            deal = addDeal.objects.all().filter(Email=name)
            return render(request, 'ReviewPage.html', {'obj': res, 'deal': deal, 'comments':comments, 'rep':rep})
        else:
            return render(request, 'ReviewPage.html', {'obj': res, 'comments':comments, 'rep':rep})
    else:
        name = request.GET.get('name')

        res = restuarantInformation.objects.all().get(Name=name)

        if review.objects.filter(res_name=name).exists():
            obj = review.objects.all().filter(res_name=name)
            rep = []
            for i in obj:
                if reply.objects.filter(user_id=i.u_id).exists():
                    rep = reply.objects.all().filter(user_id=i.u_id)

        if addDeal.objects.filter(Email=name).exists():
            deal = addDeal.objects.all().filter(Email=name)
            if review.objects.filter(res_name=name).exists():
                comments = review.objects.all().filter(res_name=name)
                return render(request, 'ReviewPage.html', {'obj': res, 'deal': deal, 'comments': comments, 'rep':rep})
            return render(request, 'ReviewPage.html', {'obj': res, 'deal': deal,})

    return render(request, 'ReviewPage.html', {'obj': res})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        check = request.POST['flexRadioDefault']

        if password == confirmpassword:
            if User.objects.filter(username=username).exists():

                message = '*Username is already exist!'
                return render(request, 'signup.html', {'message':message})

            elif User.objects.filter(email=email).exists():
                message = '*Email is already register!'
                return render(request, 'signup.html', {'message':message})
            else:
                user = User.objects.create_user(username=username,email=email, password=password)
                if check == 'vendor':
                    user.is_staff = True
                else:
                    user.is_active = True
                user.save()
                return render(request, 'login.html')

        else:
            message = '*Password does not match!'
            return render(request, 'signup.html', {'message': message})

    else:
        return render(request, 'signup.html')


