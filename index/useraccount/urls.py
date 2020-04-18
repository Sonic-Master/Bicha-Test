from django.urls import path
from useraccount import views

urlpatterns      = [
    path('',views.signup, name='signup'),
    path('login/',views.login , name='login'),
    path('logout/',views.logout, name='logout'),
]