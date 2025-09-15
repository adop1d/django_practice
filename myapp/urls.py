from django.urls import path
from . import views  # Import the view functions

urlpatterns = [
    path('',views.hello_world),  # Added this line to map the root URL to the hello_world view,
    path('about/', views.about)
]