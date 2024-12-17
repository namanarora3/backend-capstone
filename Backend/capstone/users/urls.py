from django.urls import path
from .views import *

urlpatterns = [
  path('register/', RegisterUser.as_view()),
  path('login/', LoginUser.as_view()),
  path('profile/', UserDetails.as_view()),
  path('token/', TokenView.as_view())
]