""" Calendar Maker, by Isaack joshua, isaackjoshua23@gmail.com
    Create monthly calendars, saved to a text file and fit for printing.
"""

import datetime

# Set up the constants:
DAYS = ('Sunday','Monday','Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December')

print('Calender Maker,by Isaack Joshua')

while True: #Loop to get a year from the user.
    print('Enter the year for the Calender:')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Please enter a numeric year like 2023.')
    continue

while True: # loop to get a month from the user.
    print("Enter the month for the calender, 1-12:")
    response = input('> ')

    if not response.isdecimal():
        print('Enter a numeric month, like 3 for March.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Please enter a number from 1 to 12.')

def getCalendarFor(year, month):
    calText = ''  # calText will contain the string of our calender.

    # Put the month and year at the top of the calender:
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n' 

    #Add the days of the week labes to the calender:
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    #The horizontal line string that separate weeks:
    weekSeparator = ('+----------'*7) + '+\n'

    # The blank rows have ten spaces in between the | day separators:
    blankRow = ('|          ' * 7) + '|\n'

    # Get the first date in the month. (The datetime module handles all 
    # the complicated calender stuff for us here.)
    currentDate = datetime.date(year, month, 1)

    # Roll back currentDate untill it is Sunday. (Weekday() returns 6
    # for sunday, not 0.)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:   #Loop over each week in the month.
        calText += weekSeparator

        # dayNumberRow is the row with the day number labels:
        dayNummberRow = ''
        for i in range(7):
            dayNummberLabel = str(currentDate.day).rjust(2)
            dayNummberRow += '|' + dayNummberLabel + (' '*8)
            currentDate += datetime.timedelta(days=1) # Go to next day.
        dayNummberRow += '|\n' # Add the vertical line after saturday

        #Add the day number row and 3 blank rows to the calendar text.
        calText += dayNummberRow
        for i in range(3): 
            calText += blankRow

        #Check if we're done with the month
        if currentDate.month != month:
            break

    #Add the horizontal line at the very button of the calendar.
    calText += weekSeparator
    return calText

calText = getCalendarFor(year, month)
print(calText) # Display the calender

# Save the calender to a text file :
calenderFilename = 'calender_{}_{}.txt'.format(year, month)
with open(calenderFilename, 'w') as fileObj:
    fileObj.write(calText)

print('Saved to ' + calenderFilename)
