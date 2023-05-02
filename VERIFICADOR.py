def compare_files(file1, file2):
    with open(file1, 'r', encoding='iso-8859-1') as f1:
        content1 = f1.read()
    with open(file2, 'r', encoding='iso-8859-1') as f2:
        content2 = f2.read()

    if content1 == content2:
        print("Los archivos son iguales")
    else:
        print("Los archivos son diferentes")




compare_files("C:/Users/R3/Downloads/LaBiblia.txt", "C:/Users/R3/Downloads/LaBiblia-elmejorprofesor.txt")
