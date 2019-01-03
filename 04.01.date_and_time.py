#Few examples showing how to manipulate date and time with a common python libray

#import different usefull lib
from datetime import date
from datetime import time
from datetime import datetime

#retrieve today's date with the appropriate class
today = date.today()
print("Today's date is", today)

#individuals components of today
print("date components", today.day, today.month, today.year)

#retrieve which day of the week, from 0 to 6
weekDays=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print("We are", weekDays[today.weekday()])


print("____________________")
current_date_time = datetime.now()
print("The current date and time is ", current_date_time)
print("the time is ", datetime.time(current_date_time))

#same thing as before but with the creation of a var
#t=datetime.time(current_date_time)
#print("the time is ", t)