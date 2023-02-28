import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

def visualize(arr_dots, min_dots) :
    """ Visualisasi array of Titik """
    arr_dots = np.array(arr_dots)
    min_dots = np.array(min_dots)
    dim = len(arr_dots[0])
    if dim == 1 :
        OneDPlot(arr_dots, min_dots)
        return True
    elif dim == 2 :
        TwoDPlot(arr_dots, min_dots)
        return True
    elif dim == 3 :
        ThreeDPlot(arr_dots, min_dots)
        return True
    else :
        return False


def OneDPlot(arr_dots, min_dots) :
    """ Plotting 1D array of Titik """
    plt.plot(arr_dots, np.zeros_like(arr_dots), 'bo')
    plt.plot(min_dots, np.zeros_like(min_dots), 'ro')
    connectDots(min_dots,1)
    plt.show()

def TwoDPlot(arr_dots, min_dots) :
    """ Plotting 2D array of Titik """
    plt.scatter(arr_dots[:,0], arr_dots[:,1], marker='o', color='b')
    plt.scatter(min_dots[:,0], min_dots[:,1], marker='o', color='r')
    connectDots(min_dots,2)
    plt.show()

def ThreeDPlot(arr_dots, min_dots) :
    """ Plotting 3D array of Titik """
    plt.figure().add_subplot(projection='3d')
    # ax = plt.axes(projection='3d')
    # ax.scatter3D(arr_dots[:,0], arr_dots[:,1], arr_dots[:,2], marker='o', color='b')
    # ad = plt.axes(projection='3d')
    # ad.scatter3D(min_dots[:,0], min_dots[:,1], min_dots[:,2], marker='o', color='r')
    plt.scatter(arr_dots[:,0], arr_dots[:,1], arr_dots[:,2], marker='o', color='b')
    plt.scatter(min_dots[:,0], min_dots[:,1], min_dots[:,2], marker='o', color='r')
    connectDots(min_dots,3)
    plt.show()

def connectDots(arr_dots, dim) :
    """ Menghubungkan semua pasangan titik yang ada di dalam array """
    if dim == 1 :
        for i in range(0, len(arr_dots), 2) :
            plt.plot([arr_dots[i], arr_dots[i+1]], [0,0], 'r-')
    elif dim == 2 :
        for i in range(0, len(arr_dots), 2) :
            plt.plot([arr_dots[i,0], arr_dots[i+1,0]], [arr_dots[i,1], arr_dots[i+1,1]], 'r-')
    elif dim == 3 :
        for i in range(0, len(arr_dots), 2) :
            plt.plot([arr_dots[i,0], arr_dots[i+1,0]], [arr_dots[i,1], arr_dots[i+1,1]], [arr_dots[i,2], arr_dots[i+1,2]], 'r-')


if __name__ == "__main__" :
    x = np.random.randint(0,10,size = (5,3))
    # y = np.zeros_like(x) # array of zeros
    y = np.random.randint(0,10,size = (5,3))
    
    min2 = np.array([
        [2, 3],
        [4, 5]
    ])
    
    min3 = np.array([
        [2,3,4],
        [5,6,7],
        [7,8,9],
        [10,11,12]
    ])
    
    print(x)
    print(y)
    # plt.scatter(x, y, color='k', marker='o') 
    # plt.show()
    
    # OneDPlot(x, [[1],[2]])
    # TwoDPlot(x, min2)
    visualize(x, min3)