from django.contrib import admin
from django.urls import path
from vehicle import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    #VEHICLE
    path('vehicle/', views.VehicleListView.as_view()),
    path('vehicle/<int:pk>', views.VehicleDetailView.as_view()),
    path('vehicle/<int:pk>/update', views.VehicleUpdateView.as_view()),
    path('vehicle/new/', views.VehicleCreateView.as_view()),
    path('vehicle/<int:pk>/delete', views.VehicleDeleteView.as_view()),

    #RENTINSTANCE
    path('rent/', views.RentListView.as_view()),
    path('rent/new/', views.RentCreateView.as_view()),
    path('rent/<int:pk>/update', views.RentUpdateView.as_view()),
    path('rent/<int:pk>/delete', views.RentDeleteView.as_view()),

    #AUTHENTICATION
    path('accounts/login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view(next_page="/vehicle/")),
    path('register/', views.RegisterView.as_view()),
    path('accounts/profile/', views.VehicleListView.as_view()),
    

]
