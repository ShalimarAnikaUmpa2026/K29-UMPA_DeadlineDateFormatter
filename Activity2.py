import datetime

# Asking the user for details
event = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))
day = int(input("Enter day: "))

# Converting into real date
date = datetime.date(year, month, day)
month_name = date.strftime("%B")
weekday = date.strftime("%A")

# Displaying formatted output
print("Formatted Output:")
print("Event:", event.strip().upper())
print("Date:", month_name, day, ",", year)
print("Year:", year)
print("Month:", month_name)
print("Day:", day)
print("Weekday:", weekday)
