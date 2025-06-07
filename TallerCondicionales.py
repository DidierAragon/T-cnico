# print("ejercicio numero 1")
# numero=int(input("ingresar un numero entero: "))
# if numero == 0:
#     print("el numero es cero")
# elif numero < 0:
#     print("el numero es negativo")
# elif numero > 0:
#     print("el numero es positivo")

# print("ejercicio numero 2")
# numero_1=int(input("ingresar un numero entero: "))
# numero_2=int(input("ingresar un numero entero: "))
# if numero_1 > numero_2:
#     print(f"el numero {numero_1} es mayor que {numero_2}")
# elif numero_2 > numero_1:
#      print(f"el numero {numero_2} es mayor que {numero_1}")

# print("ejercicio numero 3")
# numero_3=int(input("ingresar un numero entero: "))
# par=numero_3 % 2
# if par == 0:
#     print("el numero es par")
# else:
#     print("el numero es impar")

# print("ejercicio numero 4")
# numero_4=int(input("ingresar un numero entero: "))
# if numero_4 < 10 and numero_4 < 20:
#     print(f"el numero {numero_4} no esta entre 10 y 20")
# else:
#     print(f"el numero {numero_4}  esta entre 10 y 20")

# print("ejercicio numero 5")
# numero_5=int(input("ingresar un numero entero: "))

# numero_6=int(input("ingresar un numero entero: "))

# numero_7=int(input("ingresar un numero entero: "))

# if numero_5 > numero_6 and numero_5 > numero_7:
#     print(f"el numero {numero_5} es mayor a {numero_6} y {numero_7}")
# elif numero_6 > numero_5 and numero_6 > numero_7:
#     print(f"el numero {numero_6} es mayor a {numero_5} y {numero_7}")
# elif numero_7 > numero_6 and numero_7 > numero_5:
#     print(f"el numero {numero_7} es mayor a {numero_5} y {numero_6}")


# print("ejercicio numero 6")
# precio=float(input("ingrese el precio: "))
# descuento=precio * 0.10
# total=precio-descuento
# if precio >= 100:
#     print(f"el descuento de su compra es {descuento} y el precio queda en {total}")
# else:
#     print(f"su compra no tiene descuento")

# print("ejercicio numero 7")
# edad=int(input("ingrese su edad: "))
# if edad >= 18:
#     print("tu puedes votar")
# else:
#     print("no puedes votar")


# print("ejercicio numero 8")
# precio_1=float(input("ingrese el precio: "))
# print("eres cliente VIP ?" \
# " ingresar:" \
# " SI" \
# " NO")
# cliente=input("ingresar respuesta: ").upper()
# descuento_1=precio_1 * 0.20
# total=precio_1 - descuento_1
# if cliente == "SI":
#     print(f"el precio de su compra con el descuento de {descuento_1} queda en {total}")
# elif cliente == "NO":
#     print(f"su compra no tiene descuento, su compra queda en {precio_1}")

# print("ejercio numero 9")
# multiplo=int(input("ingresar numero "))
# nu5= multiplo % 5
# nu7= multiplo % 7
# if nu5 == 0:
#     print(f"su nuero {multiplo} es multiplo de 5 ")
# elif nu7 == 0:
#     print(f"su nuero {multiplo} es multiplo de 7 ")
# else:
#     print("su mumero no es multiplo de 5 ni de 7")

# print("ejercicio numero 10")
# numero4=int(input("ingresar un numero entero: "))
# numero5=int(input("ingresar primer divisor: "))
# numero6=int(input("ingresar segundo divisor: "))

# if numero4 % numero5 == 0 and numero5 % numero6 ==0:
#     print(f"el numero {numero4} es divisible con el numero {numero5} y {numero6} ")
# elif numero4 % numero5 == 0:
#     print(f"el numero {numero4} es divisible con el numero {numero5}")
# elif numero4 % numero6 == 0:
#     print(f"el numero {numero4} es divisible con el numero {numero6}")
# else:
#     print(f"el numero {numero4} no es divisible con {numero5} y {numero6}")

# print("ejercicio numer 11")
# lista=[1,2,34,90,56]
# if lista[3] > 10:
#     print("el numero es mayor a 10")
# else:
#     print("el numero es menor a 10")

# print("ejercicio numero 12")
# listu=[3,5,6,7,9]
# if listu[3] == 7 :
#     print("el numero esta en la lista")
# else:
#     print("no esta en la lista")

# print("ejercicio numero 13")
# numeros=[5,6,7,8,9]
# resultado = numeros[0] + numeros[1]
# if resultado > 10:
#     print("suma alta")
# else:
#     print("suma baja")

# print("ejercicio numero 14")
# trabajadores=["luis","camilo","caballo","marta"]
# if trabajadores[-1] == "marta":
#     print("nombre correcto")
# else:
#     print("nombre diferente")


# print("ejercicio numero 15")
# colores = ["amarillo","azul","rojo"]
# if colores[1] == "azul":
#     colores.insert(1,"rosa")
# print(colores)


# print("ejercico numero 16")
# tupla=(2,4,5,6,7,8)
# if tupla[0] < tupla[-1]:
#     print("orden ascendente")
# else:
#     print("orden descendente")

# print("ejercicio numero 17")
# edades=(25, 32, 45)
# if edades[1] > 30:
#     print("edad mayor a 30")
# else:
#     print("edad menor o igual a 30")

# print("ejercicio numero 18")
# numero=(1,2,3)
# numers=list(numero)
# if numers[1] == 2:
#     numers.insert(1,10)
# final=tuple(numers)
# print(final)

# print("ejercicio numero 19")
# cordenadas=(4,9)
# if cordenadas[1] > 5:
#     print("coordenada alta")
# else:
#     print("coordenada baja")

# print("ejercicio numero 20")
# tupla_1 = (1,3)
# tupla_2 = (1,2)
# if tupla_1 == tupla_2:
#     print("las tuplas son iguales")
# else:
#     print("las tuplas son diferentes")

# print("ejercicio numero 21")
# nombre="juan"
# edad=17
# datos={
#     nombre:"juan",
#     edad : 17
# }
# if datos[edad] >= 18:
#     print("ADULTO")
# else:
#     print("menor de edad")

# print("ejercicio numero 22")
# persona={"nombre":"nombre", "edad": 20}
# if persona["edad"] > 18:
#     persona["edad"] = 21
# print(persona)

# print("ejercicio numero 23")
# nacionalidad = {"nombre":"carlos" }
# if "ciudad" not in nacionalidad:
#     nacionalidad["ciudad"]="bogota"
# print(nacionalidad)

# print("ejercicio numero 24")
# compra={"producto":"pan","precio":2000}
# if "precio" in  compra:
#     print(f"el precio es {compra["precio"]}")
# else:
#     print("no hay precio")

# print("ejercicio numero 25")
# productos={"pan":1200,"leche":2000}
# if "pan" in productos:
#     print(f"el precio es {productos['pan']}")