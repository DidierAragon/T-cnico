print("Taller con while")

# print("ejercicio numero 1")
# #pide al usuario numeros enteros y sumalos hasta que ingrese el 0. luego muestra el total
# usu=int(input("ingresar un numero entero para sumarlo y cuando termines escribe 0 para terminar: "))
# contador = 0
# while usu != 0:
#     contador += usu
#     usu=int(input("ingresar un numero entero para sumarlo y cuando termines escribe 0 para terminar: "))
# print(f"la suma total es:", contador)


# print("ejercicio numero 2")
# #crea una programa que pida la contraseña usando while y hasta que no escriba "python123" correcto
# pro=input("ingresa la contraseña: ")
# clave = "python123"
# while clave != pro:
#     print("contraseña incorrecta")
#     pro=input("ingresa la contraseña: ")
# print("haz iniciado secion")


# print("ejercicio numero 3")
# #pide productos al usuario que vas almacenando en una lista y termina cuando el usuario escriba "fin".
# compras =[]
# alimen=input("ingresa compras (y cuando termines escribes fin): ")
# while alimen.lower() != "fin":
#     compras.append(alimen)
#     alimen=input("ingresa compras (y cuando termines escribes fin): ")
# print("tu lista de compras es: ",compras)


#print("ejercicio numero 4 ")
#pide al usuario numeros y ve cuales son pares e impares

# contador = 0
# pares = 0
# impares = 0

# print("Ingresa 10 números:")

# while contador < 10:
#     numero = int(input(f"Número {contador + 1}: "))
#     if numero % 2 == 0: 
#         pares += 1
#     else:
#         impares += 1
#     contador += 1

# print(f"\nEn los 10 números que me diste hay {pares} pares")
# print(f"En los 10 números que me diste hay {impares} impares")


# print("ejercicio numero 5")
# #pide al usuario notas entre 0 y 5 hasta que escriba "salir" guardar las notas en una lista y mopstrar el promedio
notas=[]
while True:
        nota=(input("ingresar notas de 1 a 5 (escribe salir si quieres finalizar): "))
        if nota.lower() == "salir":
                break
        calificacion=float(nota)
        if 0 <= calificacion <= 5:
            notas.append(calificacion)
promedio = sum(notas) / len(notas) if notas else 0
print(f"tus notas son {notas} ")
print(f"el promedio de las notas es: {promedio}")
   

# print("ejercicio numero 6")
# numero = int(input("ingrese un numero para hacer una tabla de multiplicar: "))
# contador = 1
# while contador <= 10:
#     resusultado=numero*contador 
#     print(f"{numero} * {contador} = {resusultado}")
#     contador +=1

# print("ejercicio numero 7")
# numero_secreto = 17

# print("¡Adivina el número entre 1 y 100!")

# while True:
#     intento = int(input("Ingresa tu número: "))
    
#     if intento < numero_secreto:
#         print("El número es mayor.")
#     elif intento > numero_secreto:
#         print("El número es menor.")
#     else:
#         print("¡Felicidades! Adivinaste el número.")


# print("ejercicio numero 8")
# frutas = ("piña","mango","manzana")
# while True:
#     adivina=input("adivina que frutas tengo: ")
#     if adivina in frutas:
#         print(f"la fruta {adivina} si la tengo ")
#     else:
#         print(f"no tengo esa fruta")


# print("ejercicio numero 9")
# diccionari = {
#     "rojo" : "red",
#     "amarillo" : "yellow",
#     "rosa" : "pink",
#     "azul" : "blue",
#     "verde" : "green"
# }

# print("traductor de colores, escribe un color y te muestro la traduccion en ingles")
# while True:
#     color=input("ingresar color en español: ")
#     if color in diccionari:
#         print(f"el color {color} en ingles es {diccionari[color]}")
#     else:
#         print("no tengo ese color")


# print("ejercicio numero 10")
# print("calculadora basica")
# primer=float(input("ingresar primer digito: "))
# segundo=float(input("ingresar segundo digito: "))
# print(f"OPERACIONES: \n 1: suma \n 2: resta \n 3: multiplicacion \n 4:division \n 5:salir")
# while True:

#     operacion = int(input("ingresar el numero de la opcion que desea: "))
#     if operacion == 5:
#         break
#     elif operacion == 1:
#         print(f" {primer} + {segundo} = {primer + segundo}")
#     elif operacion == 2:
#         print(f"{primer} - {segundo} = {primer - segundo}")
#     elif operacion == 3:
#         print(f"{primer} x {segundo} = {primer * segundo}")
#     elif operacion == 4:
#         print(f"{primer} / {segundo} = {primer // segundo}")
#     else:
#         print("error")


# print("ejercicio numero 11")
# personas ={}
# while True:
#     nombre = input("ingrese el nombre de la persona o salir para finalizar: ")
#     if nombre.lower() == "salir":
#         break
#     edad=int(input(f"ingresar la edad de {nombre}: "))
#     personas[nombre] = edad

# print(f"personas registradas: \n {personas}")


# print("ejercicio numero 12")
# colores=["amarillo","azul","blanco","verde","negro"]
# print("adivina que color tengo")
# while True:
#     adivino=input("adivina que color tengo: ").lower()
#     if adivino in colores:
#         print(f"felicidades si tengo el {adivino}")
#     else:
#         print("intenta otra vez")


# print("ejercicio numero 13")
# exponente= 1
# numero=int(input("ingrese el numero: "))

# while exponente < 6:
#     print(f"{numero} ** {exponente} = {numero ** exponente}")
#     exponente += 1




# print("ejercicio numero 14")
# numero=[]
# cuadrados=[]
# contador=0
# while contador < 5:
#     num=int(input(f"dame 5 numeros {contador + 1}: "))
#     numero.append(num)
#     cuadrados.append(num ** 2)
#     contador += 1
# print(f"los numeros {numero} y su cuadrado {cuadrados}")




# print("ejercicio numero 15")
# estudiantes = {}
# while True:
#     nombre=input("ingresar nombre de estudiante \n o escribir fin para terminar: ")
#     if nombre.lower() == "fin":
#         break
#     nota=float(input(f"ingresar nota de {nombre}: "))
#     estudiantes[nombre] = nota
# print(f"estudiantes y su nota: {estudiantes}")