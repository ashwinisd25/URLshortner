from django.contrib import admin
from django.urls import path, include
from shortner.views import  home,ShorturlView,index
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', ShorturlView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('shorturls/',include(router.urls)),
    path('<str:query>/', index, name="index"),
]
