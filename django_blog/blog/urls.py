from django.urls import path, include
from blog.views import RegisterView, LogoutView, LoginView
from blog.views import PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name = 'register'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('accounts/', LogoutView.as_view(), name = 'accounts/profile/'),
    path('posts/', PostListView.as_view(), name = 'post_list'),
    path('posts/new/', PostCreateView.as_view(), name = 'post_create'),
    path('posts/<int:pk>', PostDetailView.as_view(), name = 'post_detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name = 'post_update'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name = 'post_delete'),

]

