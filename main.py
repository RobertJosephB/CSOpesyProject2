
# library for threads for implementation
from threading import *
import threading

from time import sleep

def fit_roomg():
    global id,ctr,blue_mutex,green_mutex,room
    global n,b,g
    global blue_done,green_done,switch ,first
   
    print("\nGreen Thread # "+ str(id))
    green_done+=1
    id+=1
    sleep(3)
    room.release()
    if room._value == n:
        print("\nEmpty fitting room")
    pass
    
def fit_roomb():
    global id,ctr,blue_mutex,green_mutex,room
    global n,b,g
    global blue_done,green_done,switch ,first
   
    
    print("\nBlue Thread # "+ str(id))
    blue_done+=1

    id+=1
    #simulates critical section execution
    sleep(3)
    room.release()
    if room._value == n:
        print("\nEmpty fitting room")
    pass



def green_func():
    global id,blue_mutex,green_mutex,mtx
    global n,b,g
    global blue_done,green_done,switch ,first
    ctr = 0
    while green_done!=g:

        mtx.acquire()
        print("Green Acquired")
        
        #check which has the key and increase ctr for that color
        temp = 1;
        while temp == 1:
            room.acquire()
            Thread(target = fit_roomg).start()
            sleep(1)
            
        
            

            if green_done != g:
                if ctr==switch-1:
                        
                        while room._value != n:
                            pass
                        mtx.release()
                        sleep(1)
                        temp = 0
                        ctr = 0
                        
                        
                        
                else:
                    ctr+=1
            else :
                    ctr=0
                    
                    while room._value != n:
                        pass
                    mtx.release()
                    sleep(1)
                    temp = 0
                    
 
    pass
                
    
        
def blue_func():
    global id,blue_mutex,green_mutex
    global n,b,g
    global blue_done,green_done,switch ,first
    ctr = 0
    while blue_done!=b:
        mtx.acquire()
        print("Blue Acquired")
    
    
        #check which has the key and increase ctr for that color
        
        temp = 1;
        while temp == 1:
            room.acquire()
            Thread(target = fit_roomb).start()
            sleep(1)
            
            
            
            if blue_done != b:
                if ctr==switch-1:
                        while room._value != n:
                            pass
                        mtx.release()
                        
                        temp = 0
                        ctr = 0
                        
                else:
                    ctr+=1
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
    



    
    
    

    











