"""Resturantly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from vendor import views as vd
from User import views as us
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', us.index, name='home'),
    path('index.html', us.index, name='home'),
    path('login.html', us.login, name='signup'),
    path('contactUs.html', us.contact, name='Conatct'),
    path('restaurantList.html', us.restaurantList, name='restaurantList.html'),
    path('ReviewPage.html', us.reviews, name='reviews'),
    path('signup.html', us.signup, name='registration'),
    path('dashboard.html', vd.dashboard, name='dashboard'),
    path('addDeals.html', vd.displayDeals.as_view(), name='addDeals.html'),
    path('removeDeals', vd.removeDeals, name='removeDeals.html'),
    path('addDeals', vd.addDeals, name='addDeals.html'),
    path('informationForms.html', vd.InformationForms, name='information'),
    path('Reviews.html', vd.vendorReview, name='Reviews'),
    path('logout', vd.logout, name='logout')
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
