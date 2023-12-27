import datetime 

def dayOfTheWeek(number):

 days = {
  1: 'Monday',
  2: 'Tuesday',
  3: 'wednesday',
  4: 'Thursday',
  5: 'Friday',
  6: 'Saturday',
  7: 'Sunnday'
 } 
 
 return days[number]

print("Enter your date of birth in the format: dd-mm-yyyy")
dateOfBirth=input()
date=dateOfBirth.split("-") 

day=int(date[0])
month=int(date[1])
year=int(date[2])

print(year)

dateOfBirth = datetime.date(year, month, day)
a = dateOfBirth.isoweekday()
print(dayOfTheWeek(a))