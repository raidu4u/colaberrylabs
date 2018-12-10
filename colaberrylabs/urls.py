from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from users import views as users_views

urlpatterns = [
    url(r'^register/', users_views.register, name= 'register'),
    url(r'^login/', auth_views.LoginView.as_view(template_name= 'users/login.html'), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name= 'users/logout.html'), name='logout'),
    
    url(r'^password-reset/$', auth_views.PasswordResetView.as_view(template_name= 'users/password_reset.html'),
        name='password_reset'),
    url(r'^password-reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name= 'users/password_reset_done.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name= 'users/password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'^reset/done/$',
        auth_views.PasswordResetCompleteView.as_view(template_name= 'users/password_reset_complete.html'), name='password_reset_complete'),
    url(r'^admin/', admin.site.urls),
    url(r'^', users_views.index, name= 'home'),
]
