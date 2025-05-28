import time
import keyboard

def format_time(elapsed):
    mins, secs = divmod(int(elapsed), 60)
    hours, mins = divmod(mins, 60)
    return f"{hours:02}:{mins:02}:{secs:02}"

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
            break

        
        elapsed = time.time() - start_time

        if keyboard.is_pressed("num 0"):
            if mode == 0:
                work_saved = work_saved + elapsed
            if mode == 1:
                rest_saved = rest_saved + elapsed
            start_time = time.time()
            mode ^= 1
        
        if mode == 0:
            work = work_saved + elapsed
        
        if mode == 1:
            rest = rest_saved + elapsed

        print(f"\rElapsed Time: {format_time(elapsed)} | Work: {format_time(work)} | Rest: {format_time(rest)}" , end="")

        time.sleep(1)

stopwatch()