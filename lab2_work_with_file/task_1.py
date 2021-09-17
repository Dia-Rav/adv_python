
with open("1task", "w") as file:
    file.write("rgn4c ckjnr2   \n" + "cm23n1j \n" + "HELLO")
with open("1task", "r") as file:
    for line in file:
        print(line.strip()) 
       
