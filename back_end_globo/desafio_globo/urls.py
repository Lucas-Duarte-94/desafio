"""desafio_globo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from card import views

router = routers.DefaultRouter()
router.register(r'cards', views.CardView, 'card')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/create-card/', views.CreateCardView.as_view(), name="create-card"),
    path('api/card/<int:pk>/', views.UpdateDeleteCardView.as_view(), name="update-delete-card"),
    path('api/tags/', views.TagView.as_view(), name="tag"),
    path('api/create-tag/', views.TagView.as_view(), name="create-tag"),
    path('api/tag/<int:pk>/', views.TagView.as_view(), name="update-delete-tag"),
]
