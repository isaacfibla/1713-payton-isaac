numero1= float(input("Introdueix el primer número: "))
numero2= float(input("Introdueix el segon número: "))
numero3= float(input("Introdueix el tercer número: "))

if numero1 >= numero2 and numero1 >= numero3:
    print("El primer número és el més gran.")
elif numero2 >= numero1 and numero2 >= numero3:
    print("El segon número és el més gran.")
else:
    print("El tercer número és el més gran.")