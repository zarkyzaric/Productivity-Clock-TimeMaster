import time
import os
import random
import pygame

os.chdir(os.path.dirname(os.path.abspath(__file__)))

END_mp3 = 'bell.wav'
BACKGROUND_mp3='brown_noise.mp3'

def countdown_timer(total_time,END_mp3=END_mp3,BACKGROUND_mp3=BACKGROUND_mp3):
    pygame.mixer.init()
    # Load beep sound
    end_sound = pygame.mixer.Sound(END_mp3)
    pygame.mixer.music.load(BACKGROUND_mp3)
    pygame.mixer.music.play(loops=-1)  # Play in an infinite loop)

    half_time = total_time / 2
    pause_duration = random.uniform(0,half_time)
    # print(f'pause duration = {oause_duration}')
    freeze_time = random.uniform(0,total_time)

    start_time = time.time()
    remaining_time = total_time
    print(total_time)
    WAS_PAUSED = False
    
    while remaining_time > 0:
        current_time = time.time()

        elapsed_time = current_time - start_time
        remaining_time = total_time - elapsed_time
        # print(elapsed_time, end='')
        # print(remaining_time, end='\n')
        if remaining_time <= 0:
            break
        
        print(f"Time remaining: {int(remaining_time)} seconds", end='\r')
        time.sleep(1)

        if elapsed_time >= freeze_time and WAS_PAUSED == False:
            # print(f"\nClock frozen for {pause_duration:.2f} seconds.")
            time.sleep(pause_duration)
            # remaining_time = pause_duration
            WAS_PAUSED = True

    print("\nTime's up!")
    end_sound.play()
    
    time.sleep(2.5)  # Ensure beep sound plays before the script end


# Example usage
total_time = int(input("Enter the total countdown time in seconds: "))
countdown_timer(total_time)
