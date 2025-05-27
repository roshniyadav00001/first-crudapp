
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:id>', views.deleteData),
    path('edit/<int:id>', views.edit),
    path('update/', views.update),
    path('signup/', views.signuppage),
    path('login/', views.loginpage, name="login"),
    path('logout/', views.logoutuser)
   
]