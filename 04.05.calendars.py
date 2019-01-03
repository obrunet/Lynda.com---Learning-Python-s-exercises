#different examples on how to manipulate calendars

#import the calendar module
import calendar

#create a plain text calendar
c=calendar.TextCalendar(calendar.MONDAY)
print(c.formatmonth(2018, 2, 0, 0))

#create an html calendar
hc=calendar.HTMLCalendar(calendar.TUESDAY)
print(hc.formatmonth(2018,5))
