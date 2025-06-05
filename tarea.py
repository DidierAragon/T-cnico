#creo diez variable donde le pido al usuario diez numeros diferentes

print("hola, te voy a pedir 10 numeros acontinuacion")

num1=int(input("ingrese primer numero: "))

num2=int(input("ingrese segundo numero: "))

num3=int(input("ingrese tercer numero: "))

num4=int(input("ingrese cuarto numero: "))

num5=int(input("ingrese quinto numero: "))

num6=int(input("ingrese sexto numero: "))

num7=int(input("ingrese septimo numero: "))

num8=int(input("ingrese octavo numero: "))

num9=int(input("ingrese noveno numero: "))

num10=int(input("ingrese decimo numero: "))

#creo una lista donde agregare todos los numeros pedidos

numeros=[num1,num2,num3,num4,num5,num6,num7,num8,num9,num10]

#le creo una tupla a cada numero donde aparece el original y al cuadrado

tupla1=(num1,num1*num1)

tupla2=(num2,num2*num2)

tupla3=(num3,num3*num3)

tupla4=(num4,num4*num4)

tupla5=(num5,num5*num5)

tupla6=(num6,num6*num6)

tupla7=(num7,num7*num7)

tupla8=(num8,num8*num8)

tupla9=(num9,num9*num9)

tupla10=(num10,num10*num10)

#sumo los numeros originales

suma=num1+num2+num3+num4+num5+num6+num7+num8+num9+num10

#saco el promedio de los numeros

promedio=suma//10

#saco el doble de la suma de los numeros

doble=suma*2

#saco la mitad del promedio

mitad=promedio//2

#creo una lista donde agrego todas las tuplas

tuplas=[tupla1,tupla2,tupla3,tupla4,tupla5,tupla6,tupla7,tupla8,tupla9,tupla10]

print(f"los numeros que ingresaste fueron: {numeros}")

print(f"el numero y su cuadrado: {tuplas}")

print(f"la suma de los diez numeros: {suma}")

print(f"el promedio de los numeros es: {promedio}")

print(f"el doble de la suma de los diez numeros es: {doble}")

print(f"la mitad del promedio es: {mitad}")