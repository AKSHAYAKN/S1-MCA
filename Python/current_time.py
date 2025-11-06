import time
import datetime

print("Current date and time:", datetime.datetime.now())
print("Current year:", datetime.date.today().strftime("%Y"))  
print("Month of the year:", datetime.date.today().strftime("%B"))
print("Week number of the year:", datetime.date.today().strftime("%U"))
print("Day number of the week:", datetime.date.today().strftime("%w"))
print("Day of the year:", datetime.date.today().strftime("%j"))
print("Day of the month:", datetime.date.today().strftime("%d"))
print("Day of the week:", datetime.date.today().strftime("%A"))

print("\nUsing time module:")
current_time = time.localtime()
print("Today's date:", time.strftime("%Y-%m-%d", current_time))
