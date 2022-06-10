
# library for threads for implementation
from threading import *
import threading

from time import sleep



def fits():
    global id , blue_done, room, green_done,blue_mutex,green_mutex

    

    room.acquire()
    #check which has the key and increase ctr for that color
    if  blue_mutex.locked()==True:
        print("Blue Thread # "+ str(id))
        blue_done+=1
    else:
        print("Green Thread # "+ str(id))
        green_done+=1
    
    id+=1
    

    #simulates critical section execution
    sleep(1)

    give_key()
    
    room.release()




def give_key():
    global ctr,blue_mutex,green_mutex
    global n,b,g
    global blue_done,green_done,switch ,first

    #checks if there are more threads to be executed in both threads
    if blue_done != b and green_done!=g:
        if ctr%switch==0:
            ctr=1
            #if blue has key give to green
            if blue_mutex.locked()==True:
                
                blue_mutex.release()
                
                green_mutex.acquire()
            # otherwise green gives to blue
            else:
                
                green_mutex.release()
        
                blue_mutex.acquire()
                
            print("\nEmpty fitting room")
        else:
            ctr+=1
    #if blue is finished and has the key transfer it to green
    elif blue_done== b and blue_mutex.locked()==True:
            ctr=-1
            blue_mutex.release()
                
            green_mutex.acquire()

            print("\nEmpty fitting room")
            #signal that the first will be blue
            first=1
    #if green is finished and has the key transfer it to blue
    elif green_done==g and green_mutex.locked()==True:
            ctr=-1
            green_mutex.release()
        
            blue_mutex.acquire()

            print("\nEmpty fitting room")
            #signal that the first will be green
            first=1
    #if only one of the threads is executing just let it execute
    else:
        pass






global n,b,g
n,b,g=map(int, input("Enter n , b , g  values: ").split())

global room
# counting semaphore for the fitting rooms where only n number of same colored threads can enter
room = BoundedSemaphore(value=n)


global blue_done, green_done
blue_done=0 
green_done= 0

global ctr,first
first=0
ctr=1

global id
id=1

# variable used to let the system know it has reached a threshhold and must switch threads to avoid deadlock/starvation
global switch 
switch = n

#mutex locks used to get into the semaphore
global blue_mutex,green_mutex
blue_mutex= Lock()
green_mutex= Lock()

#by default blue gets the mutex lock
blue_mutex.acquire()

#if number of green threads is lower than blue threads we prioritize the lower number of threads
if b>g:
    blue_mutex.release()
    green_mutex.acquire()




for i in range(1,b+g+1):
    #If blue has key let it execute
    if blue_mutex.locked()==True:
        if ctr==1 or first==1 :
            
            print("\nBlue Only\n")

            if first==1:
                first=0

        
        blue= threading.Thread(target=fits)

        blue.start()
        blue.join()
    #else if green has the key let it execute    
    else:
        if ctr==1 or first==1:

            
            print("\nGreen Only\n")

            if first==1:
                first=0
        
        green= threading.Thread(target=fits)
        green.start()
        green.join()
        
    

    











