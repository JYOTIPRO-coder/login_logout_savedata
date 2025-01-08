
from django.contrib import admin
from django.urls import path,include
from webapp import views

urlpatterns = [
   
    path('', views.home,name=''),
    path('register', views.register,name='register'),
    path('my-login', views.my_login,name='my-login'),
    path('dashboard', views.dashboard,name='dashboard'),
    path('user-logout', views.user_logout, name="user-logout"),
    path('create-record', views.create_record, name="create-record"),
    path('record/<int:pk>', views.single_record, name="record"),
    path('update-record/<int:pk>', views.update_record, name="update-record"),
    path('delete-record/<int:pk>',views.delete_record,name='delete-record')
]
