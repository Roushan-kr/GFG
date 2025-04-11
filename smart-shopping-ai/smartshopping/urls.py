from django.contrib import admin
from django.urls import path
from core import views  # ✅ Import views from the core app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home route
    path('recommendations/', views.recommendations, name='recommendations'),  # API for recommendations
]
