"""asset_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from assets import views
from assets import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('assets/', include('assets.urls')),
    # path('addassets_form/', views.addassets_form, name ="addasset_form"),
    # path('search/', views.searchposts, name='searchposts'),
    # path('register/', views.register, name="register"),
    # path('login/', views.login, name="login"),
    # path('dashboard/' , views.dashboardView , name="dashboard"),
    # path('approvals/', views.approvals, name="approvals"),
    # path('logout/', views.logout, name="logout"),
    
    
]
