from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,Http404
from django.contrib.auth.models import User, auth
from .models import restuarantInformation,addDeal
from django.views.generic import ListView, View, DetailView
from django.core.files.storage import FileSystemStorage
from django.forms import ImageField
from .templatetags import extra





# Create your views here.
from User.models import review

from User.models import reply







def logout(request):
    auth.logout(request)
    return render(request, 'index.html')


@login_required
def dashboard(request):

    if restuarantInformation.objects.filter(Email=request.user.email).exists():

        obj = restuarantInformation.objects.get(Email=request.user.email)

        if restuarantInformation.objects.filter(Name=obj.Name).exists():
            if addDeal.objects.filter(Email=obj.Name).exists():
                obj2 = addDeal.objects.all().filter(Email=obj.Name)
                return render(request, 'dashboard.html', {'obj': obj, 'obj2': len(obj2)})
            else:
                return render(request, 'dashboard.html', {'obj': obj})
    else:
        return render(request, 'dashboard.html')

class displayDeals(ListView):
    template_name = 'addDeals.html'


    def get_queryset(self):
        if restuarantInformation.objects.filter(Email=self.request.user.email).exists():
            obj = restuarantInformation.objects.get(Email=self.request.user.email)
            return addDeal.objects.all().filter(Email=obj.Name)
        else:
            return redirect('addDeals.html')


def InformationForms(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        address = request.POST['address']
        city = request.POST['city']
        zip = request.POST['zip']
        description = request.POST['description']
        event = request.POST.getlist('event')
        food = request.POST.getlist('food')
        payment = request.POST.getlist('payment')
        if request.FILES:
            image = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            url = fs.url(filename)


        if restuarantInformation.objects.filter(Name=name).exists() and request.FILES:
            obj = restuarantInformation.objects.filter(Name=name).update(Email=email, Name=name, Address=address, City=city, Zip=zip,
                                                       Description=description, Event=event, FoodType=food,
                                                        PaymentMethod=payment,Image=url)

            message = '*Information is updated successfuly!'
        elif restuarantInformation.objects.filter(Name=name).exists():
            obj = restuarantInformation.objects.filter(Name=name).update(Email=email, Name=name, Address=address, City=city, Zip=zip,
                                                       Description=description, Event=event, FoodType=food,
                                                        PaymentMethod=payment)

            message = '*Information is updated successfuly!'
        else:
            obj = restuarantInformation.objects.create(Email=email, Name=name, Address=address, City=city, Zip=zip,
                                                       Description=description, Event=event, FoodType=food,
                                                       PaymentMethod=payment, Image=url)
            obj.save()
            message = '*Information is save successfuly!'
        obj = restuarantInformation.objects.get(Email=request.user.email)

        context = {
            'Email': obj.Email,
            'Name': obj.Name,
            'Address': obj.Address,
            'City': obj.City,
            'Zip': obj.Zip,
            'Description': obj.Description,
            'Event': obj.Event,
            'Food': obj.FoodType,
            'Payment': obj.PaymentMethod,
            'Image': obj.Image
        }

        return render(request, 'informationForms.html', {'message': message, 'context':context, 'obj': obj})

    else:
        if restuarantInformation.objects.filter(Email=request.user.email).exists():
            obj = restuarantInformation.objects.get(Email=request.user.email)

            context = {
                'Email': obj.Email,
                'Name': obj.Name,
                'Address': obj.Address,
                'City': obj.City,
                'Zip': obj.Zip,
                'Description': obj.Description,
                'Event': obj.Event,
                'Food': obj.FoodType,
                'Payment': obj.PaymentMethod,
                'Image': obj.Image
            }

            return render(request, 'informationForms.html', {'context': context, 'obj': obj})
        else:
            return render(request, 'informationForms.html')
    obj = restuarantInformation.objects.get(Email=request.user.email)
    return render(request, 'informationForms.html', {'context': obj})

def vendorReview(request):
    if request.method == 'POST':
        comment = request.POST['reply']
        userid = request.POST['id']

        if review.objects.filter(u_id=userid).exists():
            user_obj = review.objects.get(u_id=userid)

            add = reply.objects.create(user_id=user_obj, replys=comment)
            add.save()

    if restuarantInformation.objects.filter(Email=request.user.email).exists():
        fil = restuarantInformation.objects.get(Email=request.user.email)
        name = fil.Name


        if review.objects.filter(res_name=name).exists():
            obj = review.objects.all().filter(res_name=name)
            rep = []
            for i in obj:
                if reply.objects.filter(user_id=i.u_id).exists():
                    rep = reply.objects.all().filter(user_id=i.u_id)


            if rep is not None:
                return render(request, 'Reviews.html', {'obj': obj, 'rep':rep})


            return render(request, 'Reviews.html', {'obj':obj})
        return render(request, 'Reviews.html')

    return render(request, 'Reviews.html')

def removeDeals(request):
    if request.method == 'POST':
        value = request.POST['remove']
        if addDeal.objects.filter(Name=value).exists():
            obj = restuarantInformation.objects.get(Email=request.user.email)
            addDeal.objects.filter(Name=value).delete()
            instance = addDeal.objects.all().filter(Email=obj.Name)

            return render(request,'addDeals.html', {'object_list': instance})
        else:
            return render(request, 'addDeals.html')

    else:
        return render(request, 'addDeals.html')

def addDeals(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        if request.FILES:
            image = request.FILES['img']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            url = fs.url(filename)


        if restuarantInformation.objects.filter(Email=request.user.email).exists():
            obj = restuarantInformation.objects.get(Email=request.user.email)


            if addDeal.objects.filter(Name=name).exists() and request.FILES:
                add = addDeal.objects.filter(Name=name).update(Name=name, Email=obj.Name, Description=description,
                                                               Price=price, Image=url)
                message = '*Deal is updated successfully!'
                var = addDeal.objects.all().filter(Email=obj.Name)
                return render(request, 'addDeals.html', {'object_list': var, 'message': message, 'obj': obj})

            elif addDeal.objects.filter(Name=name).exists():
                add = addDeal.objects.filter(Name=name).update(Name=name, Email=obj.Name, Description=description,
                                                               Price=price)
                message = '*Deal is updated successfully!'
                var = addDeal.objects.all().filter(Email=obj.Name)
                return render(request, 'addDeals.html', {'object_list': var, 'message': message, 'obj': obj})

            else:
                if request.FILES:
                    add = addDeal.objects.create(Name=name, Email=obj, Description=description,
                                                               Price=price, Image=url)
                else:
                    add = addDeal.objects.create(Name=name, Email=obj, Description=description,
                                                 Price=price)
                add.save()
                message = '*Deal is added successfully!'
                var = addDeal.objects.all().filter(Email=obj.Name)
                return render(request, 'addDeals.html', {'object_list': var, 'message': message, 'obj': obj})

        else:
            message = 'Add Restaurant information first!'
            return render(request, 'addDeals.html', {'error': message})


    else:
        obj = addDeal.objects.get(Email=request.user.email)
        return render(request, 'addDeals.html', {'obj': obj})


