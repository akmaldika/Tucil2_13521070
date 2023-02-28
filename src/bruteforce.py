# File bruteforce.py
import tools

def bruteforceDots(arr_dot) :
    nCal = 0
    dis = -1
    close_dis = 99999
    close_dots = []
    
    for i in range(len(arr_dot)) :
        for j in range(i+1, len(arr_dot)) :
            dis = tools.euclideanDistance(arr_dot[i], arr_dot[j])
            nCal += 1
            if dis < close_dis :
                close_dis = dis
                close_dots = [arr_dot[i], arr_dot[j]]
    
    return close_dis, close_dots, nCal

if __name__ == "__main__" : 
    Array = [[2,3], [7,16], [5,7]]
    close_dis, close_dots, nCal = bruteforceDots(Array)
    print(close_dis)
    print(close_dots)
    print(nCal)
    
    # [[2,3], [7,16], [5,7]]
    # 5.0
    # [[2, 3], [5, 7]]
    # 3