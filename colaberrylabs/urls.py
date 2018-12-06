from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from users import views as users_views

urlpatterns = [
    url(r'^register/', users_views.register, name= 'register'),
    url(r'^login/', auth_views.LoginView.as_view(template_name= 'users/login.html'), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name= 'users/logout.html'), name='logout'),
    url(r'^password-reset/', auth_views.PasswordResetView.as_view(template_name= 'users/password_reset.html'),
        name='password_reset'),
    url(r'^password-reset-confirm/<uidb64>/<key>/', auth_views.PasswordResetConfirmView.as_view(template_name= 'users/password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'^password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name= 'users/password_reset_done.html'),
        name='password_reset_done'),
    url(r'^admin/', admin.site.urls),
    url(r'^', users_views.index, name= 'home'),
]
