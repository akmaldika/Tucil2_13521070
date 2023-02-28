import designCli as dc
# Input

def inputHandle() :
    n, dimension = inputNandDimension()
    
    return n, dimension

def inputNandDimension():
    while (True) :
        n = input("Masukkan jumlah titik  : ")
        try :
            n = int(n)
            
            if n < 2 :
                print(dc.B_Red + f"Jumlah titik {dc.Underline}minimal 2!" + dc.Reset)
                continue
            else : 
                break
        except ValueError :
            print(dc.B_Red + "Input harus berupa angka!" + dc.Reset)
            continue
    
    while (True) :
        dimension = input("Masukkan dimensi titik : ")
        try :
            dimension = int(dimension)
            
            if dimension < 1 :
                print(dc.B_Red + f"Dimensi {dimension} tidak terdefini! {dc.Underline}dimensi minimal 1!" + dc.Reset)
            else :
                break
        except ValueError :
            print(dc.B_Red + "Input harus berupa angka!" + dc.Reset)
            continue
    return n, dimension

# Output
def outputHandle(min_distance, min_dots, nCal, time) :
                
    print("Jarak terdekat adalah :", min_distance)
    print("Pasangan Titik terdekat adalah :")

    # Print titik
    printTitik(min_dots)

    print("Jumlah perhitungan jarak euclidean : ", nCal)
    print("Waktu perhitungan : ", time, "milidetik")
    
def printTitik(arr_dot) :
    for i in range(len(arr_dot)) :
        point = arr_dot[i]
        print(f"( {point[0] :.4f}", end = "")
        for j in range(1, len(point)):
            print(f", {point[j] :.4f}", end = "")
        print(" )", end = "")
            
        if i % 2 == 0:
            print(" dan ", end = "")
        else :
            print()