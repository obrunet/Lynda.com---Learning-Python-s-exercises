#manipulatin of the timedelta class - usefull for caculation of time

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

print("We are now: ", datetime.now())

#creation of a spare of time
print("timedelta", timedelta(days=365, hours=10, minutes=50, seconds=30))

#calculate the date & time in 1 year
print("One year from now it will be: ", str(datetime.now() + timedelta(days=365)))

#calculate the date one week ago
t=datetime.now() - timedelta(weeks=1)
print("One week ago it was:" + t.strftime("%A %B %d, %Y"))


# How many days until April Fools' Day
today = date.today() 
afd = date(today.year, 4, 1)  # get April Fool's for the same year

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print ("April Fool's day already went by %d days ago" % ((today-afd).days))
    afd = afd.replace(year=today.year + 1)  # if so, get the date for next year

# Now calculate the amount of time until April Fool's Day  
time_to_afd = afd - today
print ("It's just", time_to_afd.days, "days until next April Fools' Day!")