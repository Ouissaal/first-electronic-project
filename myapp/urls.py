from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('sign_up/', views.show_sign_up, name='sign_up'),
    path('store_page1/', views.store_page, name='store_page1'),
]
