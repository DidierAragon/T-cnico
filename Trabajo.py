print("programa de calificacion")
usuario=input("ingresar nombre del estudiante: ") 

materiaN1=input("ingresar primera materia: ")
Nota1=float(input("ingresar primera nota: "))
Nota2=float(input("ingresar segunda nota: "))
Nota3=float(input("ingresar tercera nota: "))
opera1=Nota1+Nota2+Nota3//3

materiaN2=input("ingresar segunda materia: ")
Nota4=float(input("ingresar primera  nota: "))
Nota5=float(input("ingresar segunda nota: "))
Nota6=float(input("ingresar tercera nota: "))
opera2=Nota4+Nota5+Nota6//3


materiaN3=input("ingresar tercera materia: ")
Nota7=float(input("ingresar primera nota: "))
Nota8=float(input("ingresar segunda nota: "))
Nota9=float(input("ingresar tercera nota: "))
opera3=Nota7+Nota8+Nota9//3


materiaN4=input("ingresar cuarta materia: ")
Nota10=float(input("ingresar primera nota: "))
Nota11=float(input("ingresar segunda nota: "))
Nota12=float(input("ingresar tercera nota: "))
opera4=Nota10+Nota11+Nota12//3


materiaN5=input("ingresar quinta materia: ")
Nota13=float(input("ingresar primera nota: "))
Nota14=float(input("ingresar segunda nota: "))
Nota15=float(input("ingresar tercera nota: "))
opera5=Nota13+Nota14+Nota15//3
print(f"hola el estudiante {usuario} tuvo las siguintes calificaciones {Nota1}, {Nota2} y {Nota3} en la asignatura {materiaN1 } con un promedio de { opera1} ")

print(f"hola el estudiante {usuario} tuvo las siguintes calificaciones {Nota4} {Nota5} {Nota6} en la asignatura {materiaN2 } con un promedio de {opera2 } ")

print(f"hola el estudiante {usuario} tuvo las siguintes calificaciones {Nota7} {Nota8} {Nota9} en la asignatura {materiaN3 } con un promedio de {opera3 } ")

print(f"hola el estudiante {usuario} tuvo las siguintes calificaciones {Nota10} {Nota11} {Nota12} en la asignatura {materiaN4 } con un promedio de { opera4} ")

print(f"hola el estudiante {usuario} tuvo las siguintes calificaciones {Nota13} {Nota14} {Nota15} en la asignatura {materiaN5 } con un promedio de { opera5} ")
