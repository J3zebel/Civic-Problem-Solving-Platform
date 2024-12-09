"""
URL configuration for Mainproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.urls import path,include

urlpatterns = [
    
    path('Admin/',include('Admin.urls')),
    path('Guest/',include('Guest.urls')),
    path('User/',include('User.urls')),
    path('MVD/',include('MVD.urls')),
    path('KSEB/',include('KSEB.urls')),
    path('PWD/',include('PWD.urls')),
    path('Muncipality/',include('Muncipality.urls')),
]