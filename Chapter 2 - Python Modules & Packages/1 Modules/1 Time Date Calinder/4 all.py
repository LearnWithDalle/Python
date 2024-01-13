# # Returns the current time in seconds since the epoch (January 1, 1970)
# import time

# current_time = time.time()
# print("Current time:", current_time)



# # Suspends execution of the current thread for the given number of seconds.

# import time

# print("Start")
# time.sleep(2)  # Sleep for 2 seconds
# print("End")



# # Converts a time in seconds since the epoch to a struct_time in local time.

# import time

# current_time = time.time()
# local_time = time.localtime(current_time)
# print("Local time:", local_time)



# # Converts a struct_time to a string according to the specified format.
# import time

# current_time = time.time()
# local_time = time.localtime(current_time)
# formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
# print("Formatted time:", formatted_time)


# # Similar to localtime(), but returns the time in UTC.

# import time

# current_time = time.time()
# utc_time = time.gmtime(current_time)
# print("UTC time:", utc_time)


# # Converts a struct_time to seconds since the epoch.

# import time

# struct_time = time.localtime()
# epoch_time = time.mktime(struct_time)
# print("Epoch time:", epoch_time)



# # Datetime Module

# # datetime.datetime: This class represents a date and time. It has attributes like year, month, day, hour, minute, second, etc.

# from datetime import datetime

# current_datetime = datetime.now()
# print("Current date and time:", current_datetime)

# # datetime.date: Represents a date (year, month, day).

# from datetime import date

# today = date.today()
# print("Today's date:", today)

# # datetime.time: Represents a time (hour, minute, second, microsecond).

# from datetime import time

# current_time = time(14, 30, 0)
# print("Current time:", current_time)

# # datetime.timedelta: Represents the difference between two dates or times.

# from datetime import datetime, timedelta

# current_datetime = datetime.now()
# future_datetime = current_datetime + timedelta(days=7)
# print("Future date and time:", future_datetime)

# # datetime.strptime(): Parses a string representing a date and time according to a specified format.

# from datetime import datetime

# date_string = "2023-01-01 12:30:45"
# formatted_datetime = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
# print("Formatted datetime:", formatted_datetime)


# # datetime.strftime(): Formats a datetime object as a string according to a specified format.

# from datetime import datetime

# current_datetime = datetime.now()
# formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
# print("Formatted datetime:", formatted_datetime)


# # Calinder: 

# # calendar.month(year, month): Returns a month's calendar in a multi-line string format.

# import calendar

# year = 2023
# month = 1
# print(calendar.month(year, month))


# # calendar.monthcalendar(year, month): Returns a matrix representing a month's calendar, where each row corresponds to a week

# import calendar

# year = 2023
# month = 1
# month_matrix = calendar.monthcalendar(year, month)
# print("Month matrix:")
# for week in month_matrix:
#     print(week)


# # calendar.setfirstweekday(weekday): Sets the weekday (0 is Monday, 6 is Sunday) to start each week.

# import calendar

# calendar.setfirstweekday(calendar.SUNDAY)

# # calendar.weekday(year, month, day): Returns the day of the week (0 is Monday, 6 is Sunday) for the given date.

# import calendar

# year = 2023
# month = 1
# day = 1
# day_of_week = calendar.weekday(year, month, day)
# print("Day of the week:", day_of_week)

# # calendar.isleap(year): Returns True if the given year is a leap year, otherwise False.

# import calendar

# year = 2024
# is_leap = calendar.isleap(year)
# print(f"{year} is a leap year: {is_leap}")

# calendar.leapdays(year1, year2): Returns the number of leap years in the range [year1, year2).

# import calendar

# year1 = 2000
# year2 = 2020
# leap_years = calendar.leapdays(year1, year2)
# print(f"Number of leap years between {year1} and {year2}: {leap_years}")


