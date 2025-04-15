"""
URL configuration for Canteen_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from Base_App.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView,name="home"),
    path('book', BookView,name="book"),
    path('menu', MenuView,name="menu"),
    path('about', AboutView,name="about"),
 path('feedback', FeedbackView,name="feedback"),

path('login/', loginView, name='login'),
path('register/', registerView, name='register'),
path('logout/', logoutView, name='logout'),

 path('cart', cartView, name='cart'),
    path('add-to-cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('update-cart/<int:item_id>/', update_cart, name='update_cart'),
    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),

path('payment/', paymentView, name='payment'),
path('payment/success/', paymentSuccess, name='payment_success'),
path('payments/', payment_list, name='payment_list')
    

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)