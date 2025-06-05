print("calculadora")

#le pido dos numero aleatorios al usuario

numero_1=float(input("ingresar primer numero: "))

numero_2=float(input("ingresar segundo numero: "))

#le pido al usuario que escoja con que operador va a realizar dicha operacion

print(f"ingresar numero correspondiente a la operacion:")

print(f"operaciones:" \
" 1:" \
"Suma" \
" 2:Resta" \
" 3:Multiplicacion" \
" 4:Division" \
" 5:exponente")

operacion=int(input("ingresar el numero de la operacion deseada: "))

#creo las operaciones

suma=numero_1 + numero_2

resta=numero_1 - numero_2

multi=numero_1 * numero_2

divi=numero_1 // numero_2

expo=numero_1 ** numero_2 

#de acuerdo a lo que me pida el usuario se va a hacer dicha operacion con condicionales

if operacion == 1:
    print(f"la suma de {numero_1} y {numero_2} es {suma}")
elif operacion == 2:
    print(f"la resta de {numero_1} y {numero_2 } es {resta} ")
elif operacion == 3:
    print(f"la multiplicacion de {numero_1} y {numero_2} es {multi}")
elif operacion == 4:
    print(f"la division de {numero_1} y {numero_2} es {divi}")
elif operacion == 5:
    print(f"el numero {numero_1} elevado a {numero_2} es {expo}")
else:
    print(f"no ingresaste ningun numero pedido")
