"""pishyab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from user import views as user_view
from home import views as home_view
from offer import views as offer_view
from django.contrib.auth import views as auth

urlpatterns = [
    #path('home/', include('home.urls')),
    #path('', include('home.urls')),
    path('admin/', admin.site.urls),
    ##### user related path########################## 
    path('', include('home.urls')),
    path('login/', user_view.Login, name ='login'),
    path('logout/', user_view.logout_view, name ='logout'),
    path('register/', user_view.register, name ='register'),
    path('new_offer/', offer_view.new_offer, name ='new_offer'),
    path('set_offer_priority/<int:offer_id>', offer_view.set_priority, name ='set_priority'),
    path('search/<str:input_>', offer_view.search_offer, name ='search_offer'),
    # path('view_offers/', offer_view.view_offers, name ='view_offers'),
    path('profile/<str:username_>', user_view.view_profile, name ='view_profile'),
    path('fav_offer/<int:offer_id>', user_view.fav_offer, name="fav_offer"),
    path('edit/<str:username_>', user_view.edit_view, name ='edit_view'),
    path('delete/<str:username_>', user_view.delete_view, name ='delete_view'),
]