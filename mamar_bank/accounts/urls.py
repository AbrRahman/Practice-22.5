
from django.urls import path
from .views import UserRegistrationView, UserLoginView,UserBankAccountUpdateView,userLogout
 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', userLogout, name='logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile' )
]