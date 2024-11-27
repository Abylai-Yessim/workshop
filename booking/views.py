from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from .forms import ReservationForm
from .models import Table
from datetime import datetime

class HomeView(TemplateView):
    template_name = 'booking/home.html'

def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guests = form.cleaned_data['guests']
            available_tables = Table.objects.filter(
                capacity__gte=guests
            ).order_by('capacity')
            
            if available_tables.exists():
                reservation = form.save(commit=False)
                reservation.table = available_tables.first()
                reservation.save()
                messages.success(request, 'Бронирование успешно создано!')
                return redirect('booking:home')
            else:
                messages.error(request, 'К сожалению, нет доступных столиков')
    else:
        form = ReservationForm()
    
    return render(request, 'booking/reservation.html', {'form': form}) 