
# library for threads for implementation
from threading import *
import threading

from time import sleep

def fit_roomg():
    # Fitting room thread for green
    global id,ctr,room
    global n,b,g
    global blue_done,green_done,switch 
   
   # Fitting room prints ID and color on entry
    print("\n ID: "+ str(id) + " Color: Green")
    green_done+=1
    id+=1
    #Critical section simulation
    sleep(3)
    room.release()
    if room._value == n:
        #If room is empty, prints empty room
        print("\nEmpty fitting room")
    pass
    
def fit_roomb():
    # Fitting room thread for blue
    global id,ctr,room
    global n,b,g
    global blue_done,green_done,switch 
   
    # Fitting room prints ID and color on entry
    print("\n ID: "+ str(id) + " Color: Blue")
    blue_done+=1

    id+=1
    #simulates critical section execution
    sleep(3)
    room.release()
    if room._value == n:
        #If room is empty, prints empty room
        print("\nEmpty fitting room")
    pass



def green_func():
    global id,mtx
    global n,b,g
    global blue_done,green_done,switch
    ctr = 0
    #Function repeats untill all green have finished
    while green_done!=g:
        #Tries to acquire mutex, if other function is is using mutex, waits
        mtx.acquire()
        
        
       
        temp = 1;
        while temp == 1:
            #Acquires room and creates new thread to execute critical section
            room.acquire()
            Thread(target = fit_roomg).start()
            sleep(1)
            
        
            

            if green_done != g:
                #If green is not finished, but value of switch has been reached by counter, waits for room to empty then releases mutex
                if ctr==switch-1:
                    if blue_done!=b:
                        while room._value != n:
                            pass
                        mtx.release()
                        sleep(1)
                        temp = 0
                        ctr = 0
                        
                        
                #Otherwise add to counter        
                else:
                    ctr+=1
            #Otherwise, if all green threads done, wait for room to be empty then release mutex
            elif green_done==g:

                    ctr=0
                    
                    while room._value != n:
                        pass
                    mtx.release()
                    sleep(1)
                    temp = 0
                    
 
    pass
                
    
        
def blue_func():
    global id,mtx
    global n,b,g
    global blue_done,green_done,switch 
    ctr = 0
    #Function repeats untill all blue have finished
    while blue_done!=b:
        #Tries to acquire mutex, if other function is is using mutex, waits
        mtx.acquire()
        
    
    
        
        
        temp = 1;
        while temp == 1:
            #Acquires room and creates new thread to execute critical section
            room.acquire()
            Thread(target = fit_roomb).start()
            sleep(1)
            
            
            #If blue is not finished, but value of switch has been reached by counter, waits for room to empty then releases mutex
            if blue_done != b:
                if ctr==switch-1:
                    if green_done!=g:
                        while room._value != n:
                            pass
                        mtx.release()
                        
                        temp = 0
                        ctr = 0
                        
               #Otherwise add to counter        
                else:
                    ctr+=1
            #Otherwise, if all blue threads done, wait for room to be empty then release mutex
            elif blue_done==b:
                ctr=0
                while room._value != n:
                            pass
                mtx.release()
                temp = 0
                
 
    pass
            





global n,b,g
n,b,g=map(int, input("Enter n , b , g  values: ").split())

global room
# counting semaphore for the fitting rooms where only n number of same colored threads can enter
room = BoundedSemaphore(value=n)


global blue_done, green_done
blue_done=0 
green_done= 0



global id
id=1

# variable used to let the system know it has reached a threshhold and must switch threads to avoid deadlock/starvation
global switch 
switch = n

#mutex locks used to get into the semaphore
global mtx
mtx= Lock()


#if number of green threads is lower than blue threads we prioritize the lower number of threads

green = Thread(target = green_func)

blue = Thread(target = blue_func)

green.start()
sleep(1)
blue.start()
    



    
    
    

    











