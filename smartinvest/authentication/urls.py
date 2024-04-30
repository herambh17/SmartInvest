from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='login'),
    path('signout/',views.signout,name="logout"),
]