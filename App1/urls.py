from django.urls import path
from .views import *

urlpatterns = [
    path('', home ,name='home' ),
    path('register/', register ,name='register' ),
    path('login/', login_function ,name='login' ),
    path('forget_password/', forget_password ,name='forget_password'),
    path('logout/', logout_fonction ,name='logout' ),
    path('diabetes/', diabetes ,name='diabetes' ),
    path('pneumonia/', pneumonia ,name='pneumonia' ),
    path('cardio/', cardio ,name='cardio' ),
    path('confirm/<str:uidb64>/<str:token>/', Confirm_email, name='Confirm_email'),
    path('change_password/<str:uidb64>/<str:token>/', change_password, name='change_password'),
    path('chatbot', chatbot, name='chatbot'),
]