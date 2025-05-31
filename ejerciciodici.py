# print("ejercicio numero uno")
# producto=input("ingresar producto: ")
# precio=float(input("ingresar precio del producto: "))
# cantidad=int(input("ingresar cantidad del producto: "))
# unidad=(producto,precio)
# lista=[unidad,cantidad]
# precio_total=precio*cantidad
# registro={ "producto" : lista}
# print(f"el precio total de {"producto"} es {precio_total}")

# print("ejercicio numero dos")
# producto_1=input("ingresar producto: ")
# precio_1=float(input("ingresar precio del producto: "))
# cantidad_1=int(input("ingresar cantidad del producto: "))

# producto_2=input("ingresar producto: ")
# precio_2=float(input("ingresar precio del producto: "))
# cantidad_2=int(input("ingresar cantidad del producto: "))

# producto_3=input("ingresar producto: ")
# precio_3=float(input("ingresar precio del producto: "))
# cantidad_3=int(input("ingresar cantidad del producto: "))

# tupla_1=(producto_1,precio_1)
# tupla_2=(producto_2,precio_2)
# tupla_3=(producto_3,precio_3)

# unidad_1=[tupla_1,cantidad_1]
# unidad_2=[tupla_2,cantidad_2]
# unidad_3=[tupla_3,cantidad_3]

# registro={
#     producto_1 : unidad_1,
#     producto_2 : unidad_2,
#     producto_3 : unidad_3
# }

# total_producto_1= precio_1 * cantidad_1
# total_producto_2= precio_2 * cantidad_2
# total_producto_3= precio_3 * cantidad_3

# total_final=total_producto_1 + total_producto_2 + total_producto_3

# print(f"{producto_1} : {total_producto_1}, {producto_2} : {total_producto_2}, {producto_3} : {total_producto_3}, total de la compra : {total_final}  ")


print("ejercicio numero tres")
estudiante=input("ingresar nombre del estudiante: ")
mat_1=input("nombre de la primera asignatura: ")
nota_1=float(input("ingresar primera nota "))
nota_2=float(input("ingresar segunda nota "))


mat_2=input("nombre de la segunda asignatura: ")
nota_3=float(input("ingresar primera nota "))
nota_4=float(input("ingresar segunda nota "))


mat_3=input("nombre de la tercera asignatura: ")
nota_5=float(input("ingresar primera nota "))
nota_6=float(input("ingresar segunda nota "))

asig_1=(mat_1, nota_1 + nota_2//2)
asig_2=(mat_2, nota_3 + nota_4//2)
asig_3=(mat_3, nota_5 + nota_6//2)

agrupacion_1=[asig_1,nota_1,nota_2]
agrupacion_2=[asig_2,nota_3,nota_4]
agrupacion_3=[asig_3,nota_5,nota_6]

registro={
    "nombre" : estudiante,
    "mat_1" : agrupacion_1,
    "mat_2" : agrupacion_2,
    "mat_3" : agrupacion_3
}

promedio_final = nota_1 + nota_2 + nota_3 + nota_4 + nota_5 + nota_6 //6

print(f"el estudiante {estudiante} en la materia de {mat_1} tuvo las siguientes calificaciones {nota_1} y {nota_2}, en la materia de {mat_2} tuvo las siguientes calificaciones {nota_3} y {nota_4} y en la materia de {mat_3} tuvo las siguientes calificaciones {nota_5} y  {nota_6} con un promedio de {promedio_final}")