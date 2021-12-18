from datetime import timedelta, date
from bootstrap_modal_forms.forms import BSModalForm
from django.urls import reverse
from .models import Event
import datetime
import calendar


class Calendar():
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		
	# formats a day as a td
	# filter events by day
	def formatday(self, day, events, month, year, week):
		d = ''
		tdymonth = date.today().strftime("%m")
		if tdymonth == month:
			events_per_day = events.filter(start_time__day=day, ) 
			for event in events_per_day:
				d += f"<li> {event.get_html_url} </li>"
		print(week)
		url = reverse('event_new')
		if day!= 0 :
			return f"<a class='eventB' id = '{week}' href='#' data-form = '{url}' data-toggle='modal' data-target='#eventModal'>{day}</a><ul> {d} </ul>"

		return '<span></span>'

	def formatmonthname(self):
		mydate = datetime.datetime.now()
		monthname = mydate.strftime("%B")
		year = str(datetime.date.today().year)
		monthname+= " "+ year
		return f'<div class = "monthname"> {monthname} </div>'

	def formatweekheader(self):
		weekname = ""
		for day in calendar.day_name:
			weekname+= f'<span class="day-name">{day}</span>'
		return weekname
	def formatweek(self, theweek, events):
		week = ''
		today = date.today()
		tdymonth = today.strftime("%m")
		dateNo = theweek.strftime("%#d")
		month = theweek.strftime("%m")
		year = theweek.strftime("%Y")
		day = self.formatday(dateNo, events, month, year, theweek)
		if month != tdymonth:
			week += f'<div class="day day-disabled">{day}</div>'
		if month == tdymonth:
			week += f'<div class="day">{day}</div>'
		return week
	def formatmonth(self):
		events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)
		cal = ""
		calen = calendar.Calendar()
		cal+=f'{self.formatweekheader()}\n'
		for week in calen.itermonthdates(self.year, self.month):
			cal+= f'{self.formatweek(week, events) }\n'
		return cal