
# library for threads for implementation

from threading import *
import threading

from time import sleep

def give_key():
    global ctr,blue_mutex,green_mutex
    global n,b,g
    global blue_done,green_done,switch 

    #checks if there are more threads to be executed in both threads
    if blue_done != b and green_done!=g:
        if ctr==switch:
            ctr=0
            #if blue has key give to green
            if blue_mutex.locked()==True:
                
                blue_mutex.release()
                
                green_mutex.acquire()
            # otherwise green gives to blue
            else:
                
                green_mutex.release()
        
                blue_mutex.acquire()
        else:
            ctr+=1
    #if blue is finished and has the key transfer it to green
    elif blue_done== b and blue_mutex.locked()==True:
            ctr=1
            blue_mutex.release()
                
            green_mutex.acquire()

            print("Empty fitting room")
    #if green is finished and has the key transfer it to gblue
    elif green_done==g and green_mutex.locked()==True:
            ctr=1
            green_mutex.release()
        
            blue_mutex.acquire()

            print("Empty fitting room")
    #if only one of the threads is executing just let it execute
    else:
        pass


            
            

        
            



def blue_fits():
    global id , blue_done, room

    room.acquire()
    print("Blue Thread # "+ str(id))
    
    id+=1
    blue_done+=1

    
    give_key()
    #simulates critical section execution
    sleep(0.5)
    room.release()

def green_fits():
    global id , green_done, room

    room.acquire()
    print("Green Thread # "+ str(id))
    
    id+=1
    green_done+=1

    
    give_key()
    #simulates critical section execution
    sleep(0.5)
    room.release()










global n,b,g
n,b,g=map(int, input("Enter n , b , g  values: ").split())


print("number of available slots in fitting room: ", n)
print("number of blue threads: ", b)
print("number of green threads: " , g)

global room
# counting semaphore for the fitting rooms where only n number of same colored threads can enter
room = BoundedSemaphore(value=n)


global blue_done, green_done
blue_done=0 
green_done= 0

global ctr
ctr=0

global id
id=0

# variable used to let the system know it has reached a threshhold and must switch threads to avoid deadlock/starvation
global switch 
switch = n+3
#mutex locks used to get into the semaphore
global blue_mutex,green_mutex
blue_mutex= Lock()
green_mutex= Lock()

#by default blue gets the mutex lock
blue_mutex.acquire()

#if number of green threads is larger than blue threads we prioritize green
if g>b:
    blue_mutex.release()
    green_mutex.acquire()




for i in range(b+g):
    if blue_mutex.locked()==True:
        if ctr==0:
            print("blue Only")
        
        blue= threading.Thread(target=blue_fits)

        blue.start()
        blue.join()
        
    else:
        if ctr==0:
            print("Green Only")
        
        green= threading.Thread(target=green_fits)
        green.start()
        green.join()
        
    

    











