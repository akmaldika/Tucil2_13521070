# File : main.py
# Application to find nearest 2 point from n point in 3D space and calculate distance between them

import os
import time
import bruteforce as bf
import tools as tl
import DnCTitik as DnC
import ioApp as io

if __name__ == "__main__":
    n, dimension = io.inputHandle()
    
    arr_dots = tl.randomizeDot(n, dimension)
    nCal = 0
        
    print()
    nCal = 0
    min_dis = 0
    ts = time.time()
    min_dis, min_dots, nCal  = bf.bruteforceDots(arr_dots)
    te = time.time()
    
    io.outputHandle(min_dis, min_dots, nCal, (te - ts)*1000)
    
    tl.mergeSort(arr_dots)
    print()
    ts = time.time()
    min_dis, min_dots, nCal  = DnC.devidenConquer(arr_dots, nCal)
    te = time.time()
    
    io.outputHandle(min_dis, min_dots, nCal, (te - ts)*1000)