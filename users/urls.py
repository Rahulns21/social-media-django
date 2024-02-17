from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.user_register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('password-change/', login_required(auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html')), name='password-change'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html', success_url = reverse_lazy('users:password-reset-done')), name='password-reset'),
    path('password-reset/success/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password-reset-done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password-reset-confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password-reset-complete')
]
