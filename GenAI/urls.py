from django.contrib import admin
from django.urls import path
from GenAI import views


urlpatterns = [
    path("" , views.index , name='index'),
    path("QA" , views.qa , name='QA'),
    path("contact" , views.contact , name='contact'),
    path("signup" , views.signup , name='signup'),
    path("signin" , views.signin , name='signin'),
    path("home" , views.home , name='home'),

]