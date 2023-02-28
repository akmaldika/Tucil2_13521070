# File : main.py
# Application to find nearest 2 point from n point in 3D space and calculate distance between them

import os
import time
import bruteforce as bf
import tools as tl
import DnCTitik as DnC
import ioApp as io
import visualizer as vis

if __name__ == "__main__":
    io.StartScreen()
    
    n, dimension = io.inputHandle()
    arr_dots = tl.randomizeDot(n, dimension)

    tl.mergeSort(arr_dots)
    
    
    dnc_nCal = 0
    dnc_timeS = time.time()
    dnc_min_dis, dnc_min_dots, dnc_nCal  = DnC.devidenConquer(arr_dots, dnc_nCal)
    dnc_timeE = time.time()
        
    io.BoxOpenScreen("Devide and Conquer")
    io.outputHandle(dnc_min_dis, dnc_min_dots, dnc_nCal, (dnc_timeE - dnc_timeS)*1000)
    io.BoxCloseScreen("Devide and Conquer")
    vis.visualize(arr_dots, dnc_min_dots)
    
    bf_nCal = 0
    bf_timeS = time.time()
    bf_min_dis, bf_min_dots, bf_nCal  = bf.bruteforceDots(arr_dots)
    bf_timeE = time.time()
    
    io.BoxOpenScreen("Brute Force")    
    io.outputHandle(bf_min_dis, bf_min_dots, bf_nCal, (bf_timeE - bf_timeS)*1000)
    io.BoxCloseScreen("Brute Force")
    vis.visualize(arr_dots, bf_min_dots)