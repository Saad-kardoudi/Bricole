from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.Login_page, name='Login'),
    path('logout', views.Logout_page, name='Logout'),
    path('register', views.register, name='register'),
    path('register2/<str:pk>', views.register2, name='register2'),
    path('home', views.home, name='home'),
    path('MyAccount', views.MyAccount, name='MyAccount'),
    path('Account/<str:pk>', views.Account_page, name='Account'),
    path('editAccount/', views.edit_MyAccount, name='editAccount'),
    path('HireMe/<str:pk>', views.hire_me, name='HireMe'),
    path('MyHiring/', views.myhiring, name='MyHiring'),
    path('ShowHiring/<str:pk>', views.ShowHiring, name='ShowHiring'),
]