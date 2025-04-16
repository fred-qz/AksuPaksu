#Aksu Paksu programming language
import os

index = 0
output = []
printIndex = True

os.system('cls' if os.name == 'nt' else 'clear')
print("          _                _____      _              ")
print("    /\   | |              |  __ \    | |             ")
print("   /  \  | | _____ _   _  | |__) |_ _| | _____ _   _ ")
print("  / /\ \ | |/ / __| | | | |  ___/ _` | |/ / __| | | |")
print(" / ____ \|   <\__ \ |_| | | |  | (_| |   <\__ \ |_| |")
print("/_/    \_\_|\_\___/\__,_| |_|   \__,_|_|\_\___/\__,_|")
print("Aksu Paksu programming language Interpreter")
print("v1.0.1 2025")

while True:
    program = input()
    
    if program == "b":
        print("b", output[-1])
        output.pop()
    elif program == "r":
        print(output)
    elif program == "run":
        result = ""
        for code in output:
            if 0 <= code <= 255:
                result += chr(code)
        print(result)
    elif program == "cl":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif program == "re":
        index = 0
        output = []
    elif program == "i":
        choice = input("True/False ")
        if choice == "True":
            printIndex = True
        elif choice == "False":
            printIndex = False  
    elif program == "h":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Aksu Paksu help v1.0.1")
        print("   a = +1   k = +2")
        print("   s = *2   u = ^2")
        print("   A = -1   P = -2")
        print("   = reset counter")
        print("  p = add to output")
        print("b = remove last counter")
        print("   r = show output")
        print("run = run ASCII output as text")
        print("     cl = clear")
        print("      h = help")
        print("re = reset everything")
        print("i = print index at p")
    
    for instruction in program:
        if instruction == "a":
            index += 1
        elif instruction == "k":
            index += 2
        elif instruction == "s":
            index *= 2
        elif instruction == "u":
            index = index * index
        elif instruction == "A":
            index -= 1
        elif instruction == "P":
            index -= 2
        elif instruction == " ":
            index = 0
        elif instruction == "p":
            output.append(index)
            if printIndex == True:
                print(index)
            
        if index < -1 or index > 256:
            index = 0
