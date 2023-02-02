from django.urls import path

from users.views import UserView, UserDetail, UserCreateView, UserDeleteView, UserUpdateView, LocationViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.authtoken import views


router = routers.SimpleRouter()
router.register('location', LocationViewSet)
urlpatterns = [

    path('user/', UserView.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
    path('user/create/', UserCreateView.as_view()),
    path('user/<int:pk>/update/', UserUpdateView.as_view()),
    path('user/<int:pk>/delete/', UserDeleteView.as_view()),
    path('user/token/', TokenObtainPairView.as_view()),
    path('user/token/refresh/', TokenRefreshView.as_view()),
    path('user/login/', views.obtain_auth_token),

]
urlpatterns += router.urls
