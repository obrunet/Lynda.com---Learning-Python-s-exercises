#Formating date and time

from datetime import datetime

rightnow = datetime.now()
# %a weekday, %b month, %d day number, %y year with a capital Y for the century"
print("we are now", rightnow.strftime("%a, %b, %d, %Y"))

#locale's date - depending on the computer settings
print(rightnow.strftime("Local date and time: %c"))
print(rightnow.strftime("Local date: %x"))
print(rightnow.strftime("Local time: %X"))

#locale's time - 1st with AM/PM with seconds - 2nd 24H format
print(rightnow.strftime("Current time: %I:%H:%S %p"))
print(rightnow.strftime("24Hours time: %H:%M"))
