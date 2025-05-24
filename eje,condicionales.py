#creo dos variable preguntandole al usuario 
edad=int(input("que edad tienes?: "))
puede=(input("tienes permiso?: "))
#creo la condicion con las variables y los datos que le pregunte al usuario y que muestra la opcion correcta
if edad >= 18 and puede == "si":
    print("puedes conducir")
else:
    print("no puedes conducir")