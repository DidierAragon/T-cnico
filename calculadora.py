numero_1=float(input("ingresar primer numero: "))
numero_2=float(input("ingresar segundo numero: "))
print("ingresar numero correspondiente a la operacion:")
print("operaciones:" \
"1 Suma" \
"2 Resta" \
"3 Multiplicacion" \
"4 Division" \
"5 exponente")
operacion=int(input("ingresar el numero de la operacion deseada: "))
suma=numero_1 + numero_2
resta=numero_1 - numero_2
multi=numero_1 * numero_2
divi=numero_1 // numero_2
expo=numero_1 ** numero_2 
if operacion == 1:
    print("la suma de {numero_1} y {numero_2} es {suma}")