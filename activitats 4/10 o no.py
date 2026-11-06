excelent = False
while True:
    nota = float(input("Escriu una nota (o -1 per acabar): "))
    
    
    if nota == -1:
        break
    
   
    if nota == 10:
        excelent = True
        break


if excelent:
    print("tenim un 10")
else:
    print("no tenim cap 10")