# import time
# import os

# def countdown(time_sec):
#     # pause=input("Enter ")
#     while time_sec:
        
#         mins, secs = divmod(time_sec, 60)
#         timeformat = '{:02d}:{:02d}'.format(mins, secs)
#         print(timeformat)
#         time.sleep(1)
#         time_sec -= 1
#         pause=input("Enter p to pasue:")
#         os.system('cls') 
        
        
        

#     print("stop")

# countdown(15)

# import os    
# import time    
# second = 0    
# minute = 2 
# hours = 0    
# while(True):    
#     print("Simple Stopwatch(in Python) Created By Sourabh Somani...")    
#     print('\n\n\n\n\n\n\n')    
#     print('\t\t\t\t-------------')    
#     print('\t\t\t\t  %d : %d : %d '%(hours,minute,second))    
#     print('\t\t\t\t-------------')    
#     time.sleep(1)    
#     second+=1    
#     if(second == 60):    
#         second = 0    
#         minute+=1    
#     if(minute == 60):    
#         minute = 0    
#         hour+=1;    
#     os.system('cls') 


import keyboard
import time


def countdown_1():
    pause_keyboard = False  # I use a bolean as a state is clearer for me
    i = 1  # minutes
    j = 0


    while True:

        starting_time = time.time()

        while True:  # this loop wait one second or slightly more

            if time.time() - starting_time >= 1: #  a second or more
                break

            if keyboard.is_pressed('p'):
                pause_keyboard = True

            elif keyboard.is_pressed('s'):
                pause_keyboard = False

        if pause_keyboard:
            continue


        if (j == -1): ## here we adjust the count when we changes minutes

            j = 59  # 59 secondes
            i -= 1  # one minutes less

        if(j > 9):  ## in order to pretty print

            print("{}{}:{}".format(0, i, j))  # you can direclty use 0 instead of k.
        else:
            print("{}{}:{}{}".format(0, i, 0, j))

        j -= 1

        if(i==0 and j==-1):  # we finish the counter
            break

    if(i==0 and j==-1):
        print("END")
        time.sleep(1) # wait a last second


countdown_1()