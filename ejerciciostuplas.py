# #crear una tupla
# numeros=(1,2,3,4,5)
# #mostrar el segundo valor de la tupla
# print(numeros[1])
# #cual es la longitud de la tupla
# print(len(numeros))
# #encontrar la posicion de un numero
# print(numeros.index(4))
# #contar cuantas veces aparece un dato en la tupla
# print(numeros.count(2))
# #crear una tupla con diferentes valores
# datos=(1,"hola mundo",2.3,True)
# print(datos)
# #crear una tupla que tenga otra tupla dentro y acceder a un valor de la tupla interior
# interior=(1,2,3,4)
# exterior=(interior)
# print(interior[2])



# print("taller de tuplas y listas")

# # 1 extraer primer y ultimop datpo de una tupla
# num=(1,2,3,4,5)
# print(num[0])
# print(num[-1])


# 2#extraer el segundo y el cuarto dato de una tupla de 5 numeros decimales
# decimales=(2.3,2.4,2.5,2.6,2.7)
# print(decimales[1])
# print(decimales[-2])


# 3 crear una tupla de tres elementos y agsinarle una cariable a cada uno
# comidas=("huevos fritos","pollo sudado","pan con cafe")
# desayuno=comidas[0]
# almuerzo=comidas[1]
# cena=comidas[2]
# print(desayuno)
# print(almuerzo)
# print(cena)

# 4 crear un lista con numeros y sumarlos luego almacenar el resultado en una variable
# lista=[1,23,4,5]
# result=lista[0]+lista[1]+lista[2]+lista[3]
# print(result)

#5 calcular el promedio de los datos de una tupla
# flotan=(2.3,2.5,3.6,6.7)
# promedio=flotan[0]+flotan[1]+flotan[2]+flotan[3]//4
# print(promedio)

#6 darle variables individuales a datos de una lista
# edades=[3,15,37,75]
# niño=edades[0]
# joven=edades[1]
# adulto=edades[2]
# ancianos=edades[3]
# print(edades)
# print(niño)
# print(joven)
# print(adulto)
# print(ancianos)

# #7 multiplicar datos de una lista
# multi=[2,3]
# ope=multi[0]*multi[1]
# print(ope)

# #8 crear una lista agregarle un nuevo dato y extraer el primer y el, ultimo dato
# generos=["pop","salsa","bachata"]
# generos.insert(2,"merengue")
# print(generos)
# print(generos[0])
# print(generos[-1])

#9 sumar los dos datos primeros de un a tupla de 4 elementos
# numeros=(2,4,56,7)
# opi=numeros[0]+numeros[1]
# print(numeros)
# print(opi)

# #10 restar entre dos datos dentro de una lista
# fechas=[2,40,67,23,90]
# print(fechas[1]-fechas[-2])

#11 multiplicar dos datos de una tupla
# dinero=(1,23,56,78,89)
# ope2=dinero[0]*dinero[-1]
# print(ope2)

#12 division en tupla
# divi=(9,3,5)
# di=divi[0]//divi[2]
# print(di)

# #13 extracion en tuplas 
# extraer=(2,3,45,6)
# print(extraer[2])

#14 sumar decimales en lista
# flo=[1.2,3.45,6.8]
# solu=flo[0]+flo[1]+flo[2]
# print(solu)

#15 cambiar una lista en tupla
# milist=[1,34,5,6]
# mitupla=tuple(milist)
# print(mitupla)

# # #16 covertir de lista a tupla
# mitupla=(23,4,4,55,65)
# milista=list(mitupla)
# print(milista)

#17 convertir de lista a tupla y luego mostrar un dato de la tupla
# milista=[2,4,5,67,5]
# tupla=tuple(milista)
# print(tupla)
# print(tupla[2])

#18 convertir una tupla a lista y cambiar un valor
# tupla=(2,34,55,67)
# lista=list(tupla)
# lista.insert(1,20)
# print(lista)