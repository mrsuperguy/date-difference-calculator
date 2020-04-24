import datetime

def timeUntil():
    day = datetime.datetime.now().day
    month  = datetime.datetime.now().month

    userMonth = int(input('Enter the month: '))
    userDay = int(input('Enter the day: '))
    months = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month == userMonth:
        if day <= userDay:
            difDays = userDay - day
            
        else:
            difDays = 365 - (day - userDay)
          
    elif month < userMonth:
        difDays = months[month] - day
        for each in range(month + 1, userMonth):
            difDays += months[each]
        difDays += userDay
        
    else:
      difDays = months[userMonth] - userDay
      for each in range(userMonth + 1, month):
          difDays += months[each]
      difDays += day
  	  difDays = 365 - difDays
      
  	print('\nIt is ', difDays, ' days until the next occurance of your chosen date \n\n')

def timeUntilBetterWay():
	today = datetime.datetime.now()

	userYear = int(input("Enter the year: "))
	userMonth = int(input('Enter the month: '))
	userDay = int(input('Enter the day: '))

	userDate = datetime.datetime(userYear, userMonth, userDay)

	diffdays = (userDate - today).days

	print("\nIt is ", diffdays, "days until the chosen date")
	

while True:
  timeUntil()
	timeUntilBetterWay()
