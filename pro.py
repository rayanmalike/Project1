import math
current = int(input('Enter the current time, in hours: ')) # grabs user input on what time it is
if current >= 24: # if the current time is not between 0 and 24, it points it out and ends the program.
    print(f'The current time can not be {current}:00.')
    quit()
hours = int(input('How many hours until your alarm goes off? ')) # how many hours until the alarm sounds
alarm = current + hours #variable to determine day and time when the alarm sounds
#Below are simple if statements, producing text depending on when the alarm sounds
if hours == 0:
    print('Your alarm is going off right now, or you never set one.')
    quit()
if alarm == 24:
    print('Your alarm will go off at midnight: 0:00')
elif alarm < 24:
    print('Your alarm will go off today, at', str(alarm) + ':00')
elif alarm > 24:
    days = math.floor(hours / 24) # determines how many days until the alarm sounds
    hoursleft = hours % 24 # calculates how many hours until the alarm sounds: the remainder of the previous operation.
    time = current + hoursleft # adds the remaining hours to the original time
    #below are more if statements to determine the correct day, time, and grammar is used.
    if time >= 24:
        time = time - 24
    if days == 1:
        print(f'Your alarm will go off in one day, at {str(time)}:00.')
    elif days > 1:
        if hoursleft > 0:
            print(f'Your alarm will go off in {str(int(days))} days and {str(hoursleft)} hours, at {str(time)}:00.')
        elif hoursleft == 0:
            print(f'Your alarm will go off in exactly {str(int(days))} days, at {str(time)}:00.')
    else:
        print(f'Your alarm will go off in one day, at {str(time)}:00.')
