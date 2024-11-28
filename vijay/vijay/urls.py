from django.contrib import admin 
from django.urls import path 
from mathapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('powercalculator/',views.powercalc,name="powercalculator"),
    path('',views.powercalc,name="powercalculatorroot")
]
