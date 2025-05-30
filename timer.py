import time
import keyboard

def format_time(elapsed):
    mins, secs = divmod(int(elapsed), 60)
    hours, mins = divmod(mins, 60)
    return f"{hours:02}:{mins:02}:{secs:02}"

def format_time_milli(elapsed):
    millis = int((elapsed - int(elapsed)) * 1000)
    return f"{format_time(elapsed)}.{millis:03}"


#The code also counts 0 as num 0. That's bad

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

    #variable to count the times the mode was switched
    switcheroo = 0

    print("Started at:", time.strftime("%H:%M:%S", time.localtime(start_time)))

    while True:    
        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("alt") and keyboard.is_pressed("-"):
            while keyboard.is_pressed("ctrl") and keyboard.is_pressed("alt") and keyboard.is_pressed("-"):
                time.sleep(0.005)

            break

        
        elapsed = time.time() - start_time

        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("alt") and keyboard.is_pressed("`"):
            #Currently, the code waits until the key is no longer pressed to
            #continue. I should probably change that
            #Wait for the key to be released (debounce fix)
            while keyboard.is_pressed("ctrl") and keyboard.is_pressed("alt") and keyboard.is_pressed("`"):
                time.sleep(0.05)

            switcheroo += 1

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



        print(f"\rElapsed Time: {format_time_milli(elapsed)} | Work: {format_time(work)} | Rest: {format_time(rest)} | Switches : {switcheroo}" , end="")

        time.sleep(0.001)

stopwatch()