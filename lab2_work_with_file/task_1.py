
with open("task_1_output.txt", "w") as file:
    file.write("rgn4c ckjnr2   \n" + "cm23n1j \n" + "HELLO")
with open("task_1_output.txt", "r") as file:
    for line in file:
        print(line.strip()) 
       
