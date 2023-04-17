
from django.contrib import admin
from django.urls import path
from django.conf.urls import include



urlpatterns = [
    path('admin/',admin.site.urls),
    path("DemoApp1/",include("DemoApp1.urls")),
    path("DemoApp2/",include("DemoApp2.urls")),
]