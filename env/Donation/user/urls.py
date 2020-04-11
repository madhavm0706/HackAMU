from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
      path('', views.index, name='index'),
      path('donar/',views.donar,name='donar'),
      path('register/user/',views.userRegister,name='uregister'),
      path('login/user/',views.UserLogin,name='ulogin'),
      
      path('profile/user/',views.UserProfile,name='uprofile'),
      path('user/create/',views.createUser,name='ucreate'),
      path('update/<int:id>/',views.updateUser,name='uuprofile'),

      path('login/user/donation/',views.dona_list,name='udonation'),
      path('register/police/',views.policeRegister,name='pregister'),
      path('login/police/',views.PoliceLogin,name='plogin'),
      path('logout/',views.Logout,name='logout'),
]