from django.urls import path
from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns= [

    path('' , views.home_view , name="home_view"),
    path('dashboard/' , views.dashboard_view , name="dashboard_view"),
    path('addassets/', views.add_assets_view, name="add_assets_view"),
    path('addassets_form/', views.add_assets_form_view, name ="add_assets_form_view"),
    path('search/', views.search_view, name='search_view'),
    path('register/', views.register_view, name="register_view"),
    path('login/', views.login_view, name="login_view"),
    path('approvals/', views.approvals_view, name="approvals_view"),
    path('logout/', views.logout_view, name="logout_view"),
    url(r'approved/$', views.approved_view, name="approved_view"),
    url(r'rejected/$', views.rejected_view, name="rejected_view"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name="password_reset_done"),

    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name="password_reset_complete"),
    
]


