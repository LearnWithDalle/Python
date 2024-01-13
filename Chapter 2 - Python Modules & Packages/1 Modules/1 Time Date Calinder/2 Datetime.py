from datetime import *

# datetime.now()
currentDateTime = datetime.now()
print(currentDateTime)

# datetime.date()
todaydate = datetime.today()
# print(todaydate)

# datetime.time: this is show the number in time format

nowtime = time(1,2,3,4)
# print(nowtime)

# timedelta
future = currentDateTime + timedelta(days=366)
# print(future)



