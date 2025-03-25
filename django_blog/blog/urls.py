from django.urls import path, include
from blog.views import RegisterView, LogoutView, LoginView
from blog.views import PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name = 'register'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('accounts/', LogoutView.as_view(), name = 'accounts/profile/'),
    path('post/', PostListView.as_view(), name = 'post_list'),
    path('post/new/', PostCreateView.as_view(), name = 'post_create'),
    path('post/<int:pk>', PostDetailView.as_view(), name = 'post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post_delete'),

]

