# Text Colour
Black = "\u001b[0;30m"
Red = "\u001b[0;31m"
Green = "\u001b[0;32m"
Yellow = "\u001b[0;33m"
Blue = "\u001b[0;34m"
Magenta = "\u001b[0;35m"
Cyan = "\u001b[0;36m"
White = "\u001b[0;37m"
Reset = "\u001b[0;00m"

B_Black = "\u001b[30;1m"
B_Red = "\u001b[31;1m"
B_Green = "\u001b[32;1m"
B_Yellow = "\u001b[33;1m"
B_Blue = "\u001b[34;1m"
B_Magenta = "\u001b[35;1m"
B_Cyan = "\u001b[36;1m"
B_White = "\u001b[37;1m"
Reset = "\u001b[0m"

# bg colour
Bg_Black = "\u001b[40m"
Bg_Red = "\u001b[41m"
Bg_Green = "\u001b[42m"
Bg_Yellow = "\u001b[43m"
Bg_Blue = "\u001b[44m"
Bg_Magenta = "\u001b[45m"
Bg_Cyan = "\u001b[46m"
Bg_White = "\u001b[47m"

# Text Style
Bold = "\u001b[1m"
Underline = "\u001b[4m"
Reversed = "\u001b[7m"

if __name__ == "__main__":
    print(Black + "Black" + Reset)
    print(Red + "Red" + Reset)
    print(Bold + Red + "Red Bold" + Reset)
    print(Green + "Green" + Reset)
    print(Yellow + "Yellow" + Reset)
    print(Blue + "Blue" + Reset)
    print(Magenta + "Magenta" + Reset)
    print(Cyan + "Cyan" + Reset)
    print(White + "White" + Reset)
    
    print("reset")
    
    print(B_Black + Underline + "B_Black" + Reset)
    print(B_Red + "B_Red" + Reset)
    print(B_Green + "B_Green" + Reset)
    print(B_Yellow + "B_Yellow" + Reset)
    print(B_Blue + "B_Blue" + Reset)
    print(B_Magenta + "B_Magenta" + Reset)
    print(B_Cyan + "B_Cyan" + Reset)
    print(B_White + "B_White" + Reset)

    print(f"{Bold}Bold{Reset}")
    print(Underline + "Underline" + Reset)
    print(Reversed + "Reversed" + Reset)
    print("RESET")