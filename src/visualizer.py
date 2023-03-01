import matplotlib.pyplot as plt
import numpy as np
import constant as c
import designCli as dc

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
        print(dc.B_Red + "Tidak dapat melakukan visualisasi" + dc.Reset)
        return False


def OneDPlot(arr_dots, min_dots) :
    """ Plotting 1D array of Titik """
    ax = plt.gca()
    ax.set_title("Visualisasi Titik")
    plt.plot(arr_dots, np.zeros_like(arr_dots), 'bo')
    plt.plot(min_dots, np.zeros_like(min_dots), 'ro')
    connectDots(min_dots,1)
    plt.xlabel('X')
    plt.show()

def TwoDPlot(arr_dots, min_dots) :
    """ Plotting 2D array of Titik """
    ax = plt.gca()
    ax.set_title("Visualisasi Titik")
    
    plt.scatter(arr_dots[:,0], arr_dots[:,1], marker='o', color='b')
    plt.scatter(min_dots[:,0], min_dots[:,1], marker='o', color='r')
    connectDots(min_dots,2)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

def ThreeDPlot(arr_dots, min_dots) :
    """ Plotting 3D array of Titik """
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_title("Visualisasi Titik")
    ax.scatter(arr_dots[:,0], arr_dots[:,1], arr_dots[:,2], color='b')
    ax.scatter(min_dots[:,0], min_dots[:,1], min_dots[:,2], color='r')
    connectDots(min_dots,3, ax)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

def connectDots(arr_dots, dim, ax = None) :
    """ Menghubungkan pasangan titik yang ada di dalam array """
    if dim == 1 :
        for i in range(0, len(arr_dots), 2) :
            plt.plot([arr_dots[i], arr_dots[i+1]], [0,0], 'r-')
    elif dim == 2 :
        for i in range(0, len(arr_dots), 2) :
            plt.plot([arr_dots[i,0], arr_dots[i+1,0]], [arr_dots[i,1], arr_dots[i+1,1]], 'r-')
    elif dim == 3 :
        # fig = plt.figure()
        # ax = fig.add_subplot(projection='3d')
        for i in range(0, len(arr_dots), 2) :
            ax.plot([arr_dots[i,0], arr_dots[i+1,0]], [arr_dots[i,1], arr_dots[i+1,1]], [arr_dots[i,2], arr_dots[i+1,2]], 'r-')


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
    
    # print(x)
    # print(y)
    # print(min3[:,0])
    # plt.scatter(x, y, color='k', marker='o') 
    # plt.show()
    
    # OneDPlot(x, [[1],[2]])
    # TwoDPlot(x, min2)
    # visualize(x, min3)
    
    np.random.seed(42)

    xs = np.random.uniform(0, 10, 100)

    ys = np.random.uniform(0, 10, 100)

    zs = np.random.uniform(0, 10, 100)
    
    print(xs)
    print(ys)
    print(type(zs))

    fig = plt.figure()

    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(xs,ys,zs)

    plt.show()