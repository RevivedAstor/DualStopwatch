import time
import keyboard

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.elapsed = 0.0
        self.mode = 0   # 0 = work, 1 = rest
        self.switches = 0

        self.work_total = 0.0
        self.rest_total = 0.0

        self.abort = False
    


    # format given time into hours:mins:secs
    def format_time(self, seconds=None):
        if seconds == None:
            seconds = self.elapsed
        mins, secs = divmod(int(seconds), 60)
        hours, mins = divmod(mins, 60)
        return f"{hours:02}:{mins:02}:{secs:02}"

    # format given time into hours:mins:secs.millis
    # uses format_time to format hours:mins:secs
    def format_time_milli(self):
        millis = int((self.elapsed - int(self.elapsed)) * 1000)
        return f"{self.format_time()}.{millis:03}"
    
    def total_work_time(self):
        if self.mode == 0:  # currently working
            return self.format_time(self.work_total + self.elapsed)
        return self.format_time(self.work_total)

    def total_rest_time(self):
        if self.mode == 1:  # currently resting
            return self.format_time(self.rest_total + self.elapsed)
        return self.format_time(self.rest_total)

    

    def start_stopwatch(self):
        input("Press Enter to start...")

        if self.start_time is None:
            self.start_time = time.time()

        print("Stopwatch started. Press [ctrl+alt+`] to switch the mode, [ctrl+alt+-] for Quit")


        while True:
            if self.abort: #abort is updated in method quit_stopwatch
                break


            self.elapsed = time.time() - self.start_time

            print(
                f"\rElapsed Time: {self.format_time_milli()} "
                f"| Work: {self.total_work_time()} "
                f"| Rest: {self.total_rest_time()} "
                f"| Switches: {self.switches}\n"
                f"Currently: {'Resting' if self.mode else 'Working'}",
                end="\033[F"  # move cursor up one line after printing
                # very cool trick, make sure to remember
            )


            time.sleep(0.001)


    def switch_mode(self):
        # to stop multiple switched from happening during a single hold
        while keyboard.is_pressed("`"):
            time.sleep(0.05)

        self.switches += 1

        if self.mode == 0:
            self.work_total += self.elapsed
        else:
            self.rest_total += self.elapsed

        self.start_time = time.time()
        self.elapsed = time.time() - self.start_time
        self.mode ^= 1 # toggle between 1 and 0
    

    def quit_stopwatch(self):
        if self.start_time is not None:
            self.elapsed += time.time() - self.start_time
            self.start_time = None
        self.abort = True
    
    # Not sure if this would be needed
    def reset(self):
        self.start_time = None
        self.elapsed = 0.0



sw = Stopwatch()

# stop stopwatch
keyboard.add_hotkey("ctrl+alt+-", sw.quit_stopwatch)

# change mode
keyboard.add_hotkey("ctrl+alt+`", sw.switch_mode)

sw.start_stopwatch()