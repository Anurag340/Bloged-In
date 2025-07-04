from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'profiles', views.UserProfileViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'likes', views.LikeViewSet)

# The API URLs are now determined automatically by the router
urlpatterns = [
    # Router URLs
    path('', include(router.urls)),
    
    # Custom API endpoints
    path('search/', views.SearchView.as_view(), name='search'),
    path('comments/create/', views.CommentCreateView.as_view(), name='comment-create'),
    path('likes/create/', views.LikeCreateView.as_view(), name='like-create'),
    
    # API root
    path('api-auth/', include('rest_framework.urls')),
] 