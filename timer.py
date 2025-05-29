import time
import keyboard

def format_time(elapsed):
    mins, secs = divmod(int(elapsed), 60)
    hours, mins = divmod(mins, 60)
    return f"{hours:02}:{mins:02}:{secs:02}"

def format_time_milli(elapsed):
    millis = int((elapsed - int(elapsed)) * 1000)
    return f"{format_time(elapsed)}.{millis:03}"


def stopwatch():
    input("Press Enter to start...")
    start_time = time.time()

    print("Stopwatch started. Press [num 0] to switch the mode, [num -] for Quit")

    #mode = 0 -> Work: mode = 1 -> rest 
    mode = 0

    work_saved = 0
    work = 0
    rest_saved = 0
    rest = 0

    while True:    
        if keyboard.is_pressed("num -"):
            while keyboard.is_pressed("num -"):
                time.sleep(0.005)

            break

        
        elapsed = time.time() - start_time

        if keyboard.is_pressed("num 0"):
            #Currently, the code waits until the key is no longer pressed to
            #continue. I should probably change that
            #Wait for the key to be released (debounce fix)
            while keyboard.is_pressed("num 0"):
                time.sleep(0.05)

            if mode == 0:
                work_saved = work_saved + elapsed
            else:
                rest_saved = rest_saved + elapsed

            start_time = time.time()
            elapsed = time.time() - start_time
            mode ^= 1


        
        if mode == 0:
            work = work_saved + elapsed
        
        if mode == 1:
            rest = rest_saved + elapsed

        print(f"\rElapsed Time: {format_time_milli(elapsed)} | Work: {format_time(work)} | Rest: {format_time(rest)}" , end="")

        time.sleep(0.001)

stopwatch()