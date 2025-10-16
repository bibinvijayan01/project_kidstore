from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                                 # Homepage
    path('auth/', views.login_register_view, name='login_register'),     # Combined Login + Register (kept this one)
    path('logout/', views.logout_view, name='logout_view'),              # Logout
    path('profile/', views.profile_view, name='profile_view'),           # User Profile
    path('profile/edit/', views.edit_profile, name='edit_profile'),      # Edit Profile
    path('change-password/', views.change_password, name='change_password'), # Change Password
    path('cards/', views.cards_view, name='cards_view'),
                                      # Cards Page
    path('product/<int:pk>/', views.product_detail_view, name='product_detail'), # Product Detail Page
    path('products/', views.product_list, name='product_list'),
]