# File : DnCTitik.py
# Menyelesaikan closest pair titik dengan divide and conquer

import tools

def devidenConquer(arr_dot, nCal) :
    """ Mencari jarak terdekat antara 2 titik dengan devide and conquer 
    jarak dicari dari array of titik """
    
    length_arr = len(arr_dot)
    
    if length_arr <= 3 :
        return baseCaseDNC(arr_dot, nCal)
    else :
        mid = length_arr//2
        left_arr = arr_dot[:mid]
        right_arr = arr_dot[mid:]
        
        dis1, dots1, nCal = devidenConquer(left_arr, nCal)
        dis2, dots2, nCal = devidenConquer(right_arr, nCal)
        
        close_dis = min(dis1, dis2)
        if close_dis == dis1 :
            close_dots = dots1
        else :
            close_dots = dots2
        
        dis_mid, dots_mid, nCal = closestPairStrip(left_arr, right_arr, close_dis, close_dots, arr_dot[mid], nCal)
        
        close_dis = min(close_dis, dis_mid)
        if close_dis == dis_mid :
            close_dots = dots_mid
        return close_dis, close_dots, nCal

def baseCaseDNC(arr_dot, nCal) :
    """ Mencari jarak terdekat antara 2 titik dari array 3 atau 2 titik """
    dis = tools.euclideanDistance(arr_dot[0], arr_dot[1])
    nCal += 1
    dots = [arr_dot[0], arr_dot[1]]
    
    if (len(arr_dot) == 3) :
        # Cek jika ada 3 titik
        for i in range(2) :     # 0-2 dan 1-2
            temp_dis = tools.euclideanDistance(arr_dot[i], arr_dot[2])
            nCal += 1
            if temp_dis < dis :
                dis = temp_dis
                dots = [arr_dot[i], arr_dot[2]]
                
    
    return dis, dots, nCal
    
def closestPairStrip(left_arr, right_arr, close_dis, close_dots, mid, nCal) :
    """
    Mencari Jarak titik terdekat antara 2 titik yang dibatasi garis khayalan berdasarkan divide and conquer 
    close
    Args:
        left_arr (array of Titik): Titik di kiri garis khayalan
        right_arr (array of Titik): Titik di kanan garis khayalan
        close_dis (int): jarak terdekat (terdefinisi)
        close_dots (array of Titik): titik terdekat (terdefinisi)
        mid (Titik) : titik tengah berdasarkan x
        nCal (int): jumlah perhitungan euclidean distance
    
    Returns:
        int : jarak terdekat antara 2 titik;
        array of Titik : Hasil titik;
        int : jumlah perhitungan euclidean distance
    """    
    strip_arr, n_left, n_right = stripClose(left_arr, right_arr, mid, close_dis)
    dots = close_dots
    dis = close_dis
    
    # Titik kiri hanayan mengecek titik kanan garis khayalan
    for i in range(n_left) :
        for j in range(n_left, n_left+n_right) :
            temp_dis = tools.euclideanDistance(strip_arr[i], strip_arr[j])
            nCal += 1
            if temp_dis < dis :
                dis = temp_dis
                dots = [strip_arr[i], strip_arr[j]]
    return dis, dots, nCal

def stripClose(l_arr, r_arr, mid, close_dis) :
    """
    Mencari titik terdekat antara 2 titik yang dibatasi garis khayalan berdasarkan divide and conquer 
    close
    Args:
        l_arr (array of Titik): Titik di kiri garis khayalan
        r_arr (array of Titik): Titik di kanan garis khayalan
        mid (Titik): titik tengah berdasarkan x
        close_dis (int): jarak terdekat (terdefinisi)
    Returns:
        array of Titik : Hasil titik [n_left banyak | n_right banyak];
        int : banyak titik di kiri garis khayalan dalam strip_arr;
        int : banyak titik di kanan garis khalayan dalam strip_arr;
    """    
    strip_arr = []
    length_l = len(l_arr)
    length_r = len(r_arr)
    n_left = 0
    n_right = 0
    
    for i in range (length_l) :
        if (abs(l_arr[i][0] - mid[0]) < close_dis) :
            strip_arr += [l_arr[i]]
            n_left += 1
    for j in range (length_r) :
        if (abs(r_arr[j][0] - mid[0]) < close_dis) :
            strip_arr += [r_arr[j]]
            n_right += 1
    return strip_arr, n_left, n_right

if __name__ == "__main__" :
    arr = [0,1,2,3,4,5,6]
    arr2 = [0,1,2,3,4]
    n = len(arr)
    mid = n//2
    print(n)
    print(mid)
    print(arr[:mid])
    print(arr[mid:])
    for i in range (3) :
        print(i)
        for j in range (3, 4+3) :
            print(" j =",j)

    
    arr3 = []
    arr3 += [arr] + [arr2]
    print(arr3)