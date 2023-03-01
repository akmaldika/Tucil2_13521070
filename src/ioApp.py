import designCli as dc

# Input

def inputHandle() :
    n, dimension = inputNandDimension()
    # n, dimendion = fileinput()
    return n, dimension

def inputNandDimension():
    """ Menangani input dari pengguna berupa dimensi dan banyak titik]"""
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
    # Output Text App
def outputHandle(min_distance, min_dots, nCal, time) :
    """ Mencetak hasil perhitungan program """
    print("Jarak terdekat adalah              :", min_distance)
    print("Pasangan Titik terdekat adalah     :", end=' ')

    # Print pasangan titik
    printTitik(min_dots)

    print("Jumlah perhitungan jarak euclidean :", nCal)
    print("Waktu perhitungan                  :", time, "milidetik")
    
def printTitik(arr_dot) :
    """ mencetak pasangan titik dalam bentuk (x1, y1,...) dan (x2, y2,...) """
    for i in range(len(arr_dot)) :
        point = arr_dot[i]
        print(f"( {point[0] :.4f}", end = "")
        for j in range(1, len(point)):
            print(f", {point[j] :.4f}", end = "")
        print(" )", end = "")
            
        if i % 2 == 0:
            print(dc.B_Green+" dan ", end = "" + dc.Reset)
        else :
            print()

    # Splash

def StartScreen() :
    """ Spalsh dari Startscreen """
    print(dc.B_Magenta,"""
 $$$$$$\ $$\                                      $$\           $$$$$$$\ $$\           $$\                                         
$$  __$$\$$ |                                     $$ |          $$  __$$\\__|          $$ |                                        
$$ /  \__$$ |$$$$$$\  $$$$$$$\ $$$$$$\  $$$$$$$\$$$$$$\         $$ |  $$ $$\ $$$$$$$\$$$$$$\   $$$$$$\ $$$$$$$\  $$$$$$$\ $$$$$$\  
$$ |     $$ $$  __$$\$$  _____$$  __$$\$$  _____\_$$  _|        $$ |  $$ $$ $$  _____\_$$  _|  \____$$\$$  __$$\$$  _____$$  __$$\ 
$$ |     $$ $$ /  $$ \$$$$$$\ $$$$$$$$ \$$$$$$\   $$ |          $$ |  $$ $$ \$$$$$$\   $$ |    $$$$$$$ $$ |  $$ $$ /     $$$$$$$$ |
$$ |  $$\$$ $$ |  $$ |\____$$\$$   ____|\____$$\  $$ |$$\       $$ |  $$ $$ |\____$$\  $$ |$$\$$  __$$ $$ |  $$ $$ |     $$   ____|
\$$$$$$  $$ \$$$$$$  $$$$$$$  \$$$$$$$\$$$$$$$  | \$$$$  |      $$$$$$$  $$ $$$$$$$  | \$$$$  \$$$$$$$ $$ |  $$ \$$$$$$$\\$$$$$$$\ 
 \______/\__|\______/\_______/ \_______\_______/   \____/       \_______/\__\_______/   \____/ \_______\__|  \__|\_______|\_______|
          """, dc.Reset)
    print("{: ^144}".format(dc.B_Yellow + dc.Underline + "Akmal Mahardika Nurwahyu Pratama - 13521070") + dc.Reset + "\n")

def BoxOpenScreen(name) :
    """ Box pembatas (buka) """
    print(dc.Bold + "┌{}{:^24}{}┐".format("─"*53,name,"─"*53) + dc.Reset + "\n")

def BoxCloseScreen(name) :
    """ Box pembatas (tutup) """
    print("\n" + dc.Bold + "└{}{:^24}{}┘".format("─"*53,name,"─"*53) + dc.Reset + "\n")
    
    

if __name__ == "__main__" :
    StartScreen()
    BoxOpenScreen("Devide and Conquer")
    BoxCloseScreen("Devide and Conquer")
