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
    list_point = np.zeros((n, dimension)) 
    for i in range(n) :
        for j in range(dimension) :
            list_point[i][j] = random.uniform(constant.MIN_RAND, constant.MAX_RAND)
    return list_point

def euclideanDistance(dot1, dot2, close_dis = None) :
    """ Menghitung Eucledian Distance antara 2 titik, n Dimensi | 
    (Overload) akan berhenti jika jaraknya lebih besar dari close_dis mengembalikan UNDEFINED """
    distance = 0
    if (close_dis == None) :
        for i in range(len(dot1)) :
            distance += (dot1[i] - dot2[i])**2
        return math.sqrt(distance)
    else :
        flag = True
        for i in range(len(dot1)) :
            distance += (dot1[i] - dot2[i])**2
            if (distance > close_dis**2) :
                flag = False
                break
            
        return math.sqrt(distance) if flag else constant.UNDEFINED
 
def mergeSortbyX(arr_dot) :
    """ Melakukan merge sort sebuah array of titik berdasarkan nilai x1 """
    length = len(arr_dot)//2
    if length > 1:
        # Devide
        mid = length//2
        L = arr_dot[:mid]
        R = arr_dot[mid:]
        mergeSortbyX(L)
        mergeSortbyX(R)
        
        # Counquer
        i = j = k = 0
        l_len = len(L)
        r_len = len(R)
        while i < l_len and j < r_len :
            if L[i][0] < R[j][0]:
                arr_dot[k] = L[i]
                i += 1
            else:
                arr_dot[k] = R[j]
                j += 1
            k += 1
        
        while i < l_len :
            arr_dot[k] = L[i]
            i += 1
            k += 1
            
        while j < r_len :
            arr_dot[k] = R[j]
            j += 1
            k += 1
            
        
        

# Test
if __name__ == "__main__":
    print(constant.MAX_RAND, constant.MIN_RAND)
    
    start = time.time()
    array = randomizeDot(8,5)
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
    mergeSortbyX(array)
    print(array)