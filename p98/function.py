def swap():
    info = input("Enter FIle Path For File 1: ")
    info2 = input("Enter FIle Path For File 2: ")
    file1 = open(info,"r")
    f1 = file1.read()
    file2 = open(info2,"r")
    f2 = file2.read()

    with open(info,'w') as file1:
        file1.write(f2)

    with open(info2,'w') as file2:
        file2.write(f1)    
    print("Swap has been completed!!😀😀😀")
swap()        