"""
URL configuration for codathon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from farmapp import views
from farmapp.models import Product1
from django.conf.urls.static import static
from django.conf import settings
from  farmapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signuppage,name='signup'),
    path('login/',views.loginpage,name='login'),
    path('f1/',views.f1y,name='f1'),
    path('f2/',views.f2w,name='f2'),
    path('f3/',views.f3s,name='f3'),
    path('logout/',views.LogoutPage,name='logout'),
    path('f4/',views.f4c,name='f4'),
    path('p/',views.p,name='p'),
    path('create_product/',views.create_product,name='create_product'),
    #path('profile_and_product_form/',views.profile_and_product_form,name='profile_and_product_form'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)