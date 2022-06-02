
# library for threads for implementation
from threading import *

from time import sleep


n,b,g=map(int, input("Enter n , b , g  values: ").split())
print("number of available slots in fitting room: ", n)
print("number of blue threads: ", b)
print("number of green threads: " , g)