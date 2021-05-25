from django.urls import path
from user import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
	path('login/', views.login_view, name='login'),
	path('signup/', views.signup, name = 'signup'),
	path('logout/', LogoutView.as_view(next_page = 'login'), name = 'logout'),
]
