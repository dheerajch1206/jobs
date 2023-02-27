from datetime import date
from datetime import datetime

today = date.today() # today date
d3 = today.strftime("%m/%d/%y")
print(today,d3)
print(today - datetime.strptime('Aug 17, 2022', "%b %d, %Y").date())
print(today - datetime.strptime(datetime.strptime('Aug 17, 2022', "%b %d, %Y").strftime("%m/%d/%y"),"%m/%d/%y"))