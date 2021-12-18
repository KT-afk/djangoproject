from django.urls import path, include
from . import views as base
from Users import views as users_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from cal import views as cal_views



urlpatterns = [
	path('', PostListView.as_view(), name='home'),
	path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('about-me/', base.about, name='about'),
	path('contact/', base.contact, name='contact'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
	
]
