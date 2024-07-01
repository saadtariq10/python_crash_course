# Sleep time

import time
max_reteries=5
wait_time=1
attempts=0

while attempts < max_reteries:
    print("Your Attempt is:", attempts + 1, "\nWait time:", wait_time, "seconds")
    time.sleep(wait_time)
    wait_time*=2
    attempts+=1