from django.urls import path, include
from blog.views import RegisterView, LogoutView, LoginView
from blog.views import PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView, CommentCreateView, CommentDeleteView, CommentDetailView, CommentListView, CommentUpdateView

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
    path('comment/', CommentListView.as_view(), name = 'comment_list'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name = 'comment_create'),
    path('comment/<int:pk>', CommentDetailView.as_view(), name = 'comment_detail'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name = 'comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name = 'comment_delete'),

]

