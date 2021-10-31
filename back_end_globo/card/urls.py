from django.urls import path, include
from django.contrib import admin
from . import views
from rest_framework import routers
from card import views

router = routers.DefaultRouter()
router.register(r'cards', views.CardView, 'card')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('hello/', views.say_hello)
]