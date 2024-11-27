from django.urls import path
from .views import HomeView, reservation_view

app_name = 'booking'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Use the class-based view
    path('reservation/', reservation_view, name='reservation'),
]
