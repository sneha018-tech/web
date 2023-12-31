"""
URL configuration for movies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from film import views
from django.conf import settings
from django.conf.urls.static import static
app_name="film"
urlpatterns = [
    path('',views.home,name='home'),
    path('base1/',views.base1,name='base1'),
    path('gosomewhere/<p>',views.gosomewhere,name='gosomewhere'),
    path('delete/<p>',views.delete,name='delete'),
    path('edit/<p>',views.edit,name='edit'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

