from django.urls import path
from . import views

urlpatterns = [
    path('create_referral/', views.create_referral, name='create_referral'),
    path('referral_success/', views.referral_success, name='referral_success'),
    path('create_action/<int:task_id>/', views.create_action, name='create_action'),
    path('action_success/', views.action_success, name='action_success'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),  # URL for user dashboard
    path('general_dashboard/', views.general_dashboard, name='general_dashboard'),  # URL for general dashboard


]
