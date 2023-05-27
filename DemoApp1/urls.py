from django.contrib import admin
from django.urls import path
from DemoApp1 import views
urlpatterns = [
       path('admin/', admin.site.urls),
       path('first/',views.f1),
       path('second/',views.f2),
]