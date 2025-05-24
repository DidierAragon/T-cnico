# #le pido al usuario los datos
print("registro de mascotas")
mascota=input("ingresar nombre de la mascota: ")
tipo=input("que tipo de animal es: ")
edad=int(input("que edad tiene la mascota: "))
dueño=input("nombre del dueño: ")
ciudad=input("de que ciudad eres: ")
# #ingresa los datos en un diccionario
registro = {
    "nombre" : mascota,
    "animal" : tipo,
    "años" : edad,
    "responsable" : dueño,
    "lugar" : ciudad}
print(registro)


# dictionary = {"a": 1,
#               "e": 2
#               }
# print()
# print(dictionary)
# print(f"clave a:{dictionary["a"]}")
# print(f"clave e:{dictionary["e"]}")

# dictionary = {"numbers":[18,20,28],
#               "groups":{"a":1,"b":2}
#               }

# print(dictionary)
# print(f"clave numbers:{dictionary["numbers"]}")
# print(f"clave numbers:{dictionary["groups"]}")

# print(f"clave numbers:{dictionary["numbers"],[1]}")
# print(f"clave numbers:{dictionary["numbers"],["b"]}")

# print (dictionary,{"z"})