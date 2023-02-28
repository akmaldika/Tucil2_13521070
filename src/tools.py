import numpy as np
import constant
import random
import time
import math


def randomizeDot(n, dimension) :    
    """ Membuat array of Titik dengan ukuran n x n
    Array 2D diisi dengan nilai random
    nilai elemen dalam array 2d mungkin ada yang sama """
    return np.random.uniform(constant.MIN_RAND, constant.MAX_RAND, (n, dimension))

def randomizeDot2(n, dimension) :
    """ same as randomizeDot but using for loop """
    list_point = np.zeros((dimension, n))
    print(list_point) 
    for i in range(n) :
        for j in range(dimension) :
            list_point[i][j] = random.uniform(constant.MIN_RAND, constant.MAX_RAND)
    return list_point

def isCloser(dot1, dot2, close_dis) :
    """ True jika jarak abs(dot1[i]-dot2[i]) < close_dis**2 untuk i 0..len(dot1) """
    flag = True
    for i in range(len(dot1)) :
        if abs(dot1[i]-dot2[i]) > close_dis :
            flag = False
            break
    return flag

def euclideanDistance(dot1, dot2) :
    """ Menghitung Eucledian Distance antara 2 titik, n Dimensi """
    distance = 0
    for i in range(len(dot1)) :
        distance += (dot1[i] - dot2[i])**2
    return math.sqrt(distance)        

def mergeSort(arr_dot) :
    """ Melakukan merge sort sebuah array of titik berdasarkan nilai x1 """

    if len(arr_dot) > 1:
        # Devide
        mid = len(arr_dot)//2
        L = arr_dot[:mid]
        R = arr_dot[mid:]
        mergeSort(L)
        mergeSort(R)
        
        # Counquer
        i = j = k = 0
        l_len = len(L)
        r_len = len(R)
        temp_arr = np.zeros((len(arr_dot), len(arr_dot[0])))
        
        while i < l_len and j < r_len :
            if L[i][0] < R[j][0]:
                temp_arr[k] = L[i]
                i += 1
            else:
                temp_arr[k] = R[j]
                j += 1
            k += 1
        
        while i < l_len :
            temp_arr[k] = L[i]
            i += 1
            k += 1
            
        while j < r_len :
            temp_arr[k] = R[j]
            j += 1
            k += 1
        
        for i in range(len(arr_dot)):
            arr_dot[i] = temp_arr[i]
        
        

# Test
if __name__ == "__main__":
    print(constant.MAX_RAND, constant.MIN_RAND)
    
    start = time.time()
    array = randomizeDot(5,3)
    print(array)
    stop = time.time()
    print("Time elapsed 1: ", stop - start)
   
    """ start2 = time.time()
    print(randomizeDot2(3,5))
    stop2 = time.time()
    print("Time elapsed 2: ", stop2 - start2)
    
    print(f"fastest : {1 if stop - start < stop2 - start2 else 2} \n") """
    # 20th try : fastest = 1
    print(len(array))
    mergeSort(array)
    print(array)