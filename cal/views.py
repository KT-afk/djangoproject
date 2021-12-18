from django.views import generic
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
import calendar
from django.views.generic import ListView
from datetime import datetime, timedelta, date
from .models import *
from .utils import Calendar
from .forms import EventForm
from django.contrib import messages

class CalendarView(ListView):
    model = Event
    template_name = 'cal/cal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        
        html_cal = cal.formatmonth()
        #context['prev_month'] = prev_month(d)
        #context['next_month'] = next_month(d)
        context['calendar'] = mark_safe(html_cal)

        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
        print(x)
    return datetime.today()

"""def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
"""
def event(request, pk=None):
    
    instance = Event()
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        messages.success(request, 'Event has been added successfully')
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'cal/event.html', {'form': form})

def eventEdit(request, pk):
    if pk:
        instance = get_object_or_404(Event, pk=pk)
        print(instance)
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        messages.success(request, 'Event has been updated successfully')
        print("Great job")
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'cal/event_edit.html', {'form': form, 'id':pk})

def eventDelete(request, pk):

    instance = get_object_or_404(Event, pk=pk)
    instance.delete()
    messages.success(request, 'It has been deleted')
    return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'cal/event_edit.html', {'id':pk})
