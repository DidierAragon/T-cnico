# usuario = int(input("ingresa tu edad: "))
# if usuario > 17:
#     print("eres mayor de edad")
# elif usuario < 18:
#     print("eres menor de edad")
# else:
#     print("error")
# #permiten controlar el flujo de ejecución de un programa, permitiendo que se realicen diferentes acciones dependiendo de si se cumplen ciertas condiciones. Las estructuras condicionales en Python se basan en las palabras clave if, else y elif

# #le pido al usuario dos numeros
# primerNumero=float(input("ingresar primer numero: "))
# segundoNumero=float(input("ingresar segundo numero: "))

edad = int(input("ingresar edad: "))
if edad == 0 and edad <= 4:
    print("entrada gratis")
elif edad >= 5 and edad <= 18:
    print("entrada 5 euros")  
elif edad >= 18 and edad <= 100:
    print("entrada 18 euros")
elif edad < 0:
    print("no es una edad correta")

print("finaliza")