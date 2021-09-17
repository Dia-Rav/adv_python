def write_array(array, file_name):
    """записывает строки из array в файл file_name"""
    text = ''
    array = '\n'.join (array)
    file_name.writelines(array)


list1 = ["qwe", "rty", "uio"]
with open("task_2_output.txt", "w") as file:
    write_array(list1, file)
with open("task_2_output.txt", "r") as file:
    for line in file:
        print(line.strip())
