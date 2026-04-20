from django.contrib import admin
from django.urls import path
from todoapp.views import home, ucreatetask, taskview, delete, contact
from auapp.views import usignup, ulogin, ulogout, uresetpass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('usignup/', usignup, name='usignup'),
    path('ulogin/', ulogin, name='ulogin'),
    path('ulogout/', ulogout, name='ulogout'),
    path('ucreatetask/', ucreatetask, name='ucreatetask'),
    path('uresetpass/', uresetpass, name='uresetpass'),
    path('taskview/', taskview, name='taskview'),
    path('delete/<int:id>', delete, name='delete'),
    path('contact/', contact, name='contact'),
    
]