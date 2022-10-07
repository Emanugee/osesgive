from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('signout', views.signout, name='signout'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('pay', views.home, name='home'),
    path('confirm', views.confirm, name='confirm'),
    path('payment', views.payment, name='payment'),
    path('thanks', views.thankyou, name='thanks'),
]
