from django.contrib import admin
from django.urls import path
from DemoApp2 import views
urlpatterns = [
       path('admin/', admin.site.urls),
       path('thrid/',views.f3),
       path('fourth/',views.f4),
    ]