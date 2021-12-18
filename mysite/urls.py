
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from Users import views as users_views
from cal import views as cal_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('signup/', users_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name = "login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name = "logout"),
    
    path('password-reset/',
    	 auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
    	 name = 'password_reset'),

    path('password-reset/done/',
    	 auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
    	 name = 'password_reset_done'),

    path('password-reset-complete/',
    	 auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
    	 name = 'password_reset_complete'),

    path('password-reset-confirm/<uidb64>/<token>/',
    	 auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
    	 name = 'password_reset_confirm'),

    path('profile/', users_views.profile, name='profile'),
    path('calendar/', cal_views.CalendarView.as_view(), name='calendar'),
    path('event/new/', cal_views.event, name='event_new'),
    path('event/<int:pk>/edit/', cal_views.eventEdit, name='event_edit'),
    path('event/<int:pk>/delete/', cal_views.eventDelete, name='event_delete'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

