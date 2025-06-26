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


print("ejercicio numero 4 ")
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


print("ejercicio numero 5")
# #pide al usuario notas entre 0 y 5 hasta que escriba "salir" guardar las notas en una lista y mopstrar el promedio
# notas=[]
# fin = 0
# nota=int(input("ingresar notas de 1 a 5 (escribe 0 si quieres finalizar): "))
# while nota != fin:
#         notas.append(nota)
#         nota=int(input("ingresar notas de 0 a 5 (escribe salir si quieres finalizar): "))
# print(f"tus notas son {notas} ")
# print(f"tu promedio es {sum(notas)/len(notas)}")
   

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


print("ejercicio numero 8")
frutas = ("piña","mango","manzana")
adivina=input("adivina que frutas tengo: ")
while adivina != frutas:
    print(f"la fruta {adivina} no la tengo")
    adivina=input("adivina que frutas tengo: ")
print(f"la fruta {adivina} si la tengo")