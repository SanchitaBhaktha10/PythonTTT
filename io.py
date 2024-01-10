def read_file():
    file = open("E:\OneDrive - Anudip Foundation for Social Welfare\Desktop.txt","r")
    for line in file:
        print(line, end="")
    file.close()

read_file()
