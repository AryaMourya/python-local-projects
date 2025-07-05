#countdown timer
import time
import winsound

class color:
    BOLD='\033[1m'
    YELLOW='\033[93m'
    RED='\033[91m'
    END='\033[0m'

def beep(frequency=1000,duration=500):
    """Play a beep sound """
    try:
        winsound.Beep(frequency,duration)
    except:
        print("\a")

my_time=int(input("Enter the time in seconds:"))

for x in range(my_time,0,-1):

    hours=x//3600
    minutes=(x%3600)//60
    seconds=x%60

    time_str=(
                f"{color.BOLD}{hours:02}{color.END}:"
        f"{color.BOLD}{minutes:02}{color.END}:"
        f"{color.BOLD}{seconds:02}{color.END}"
    )

    if x<=5:
        time_str=(
            f"{color.BOLD}{color.RED}{hours:02}{color.END}:"
            f"{color.BOLD}{color.RED}{minutes:02}{color.END}:"
            f"{color.BOLD}{color.RED}{seconds:02}{color.END}"
        )
        beep(800,200)

    print(time_str)
    time.sleep(1)

print(f"{color.BOLD}{color.YELLOW}TIME'S UP!{color.END}") 

for _ in range(3):
    beep(1200,300) 
    time.sleep(0.2)
    