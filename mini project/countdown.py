import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
    
    print("Time's up!")

# Set the countdown time in seconds
countdown_time = 10  # for a 10-second countdown
countdown(countdown_time)
