import time
wait_time=1
max_retries=5
attemps=0
while attemps<max_retries:
    print("attemps",attemps,+1,"-waittime",wait_time,)
    time.sleep(wait_time)
    wait_time*=2
    attemps+=1