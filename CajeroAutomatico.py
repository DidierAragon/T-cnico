saldo = 0
print("bienvenido a su cuenta porfaor ingrese el numero da lo que quiere realizar:")
print("1: ver saldo\n2: depositar\n3: retirar\n4: salir")

while True:
    usu = int(input("ingresar numero: "))
    if usu == 4:
        print("ha cerrado secion ")
        break
    elif usu == 1:
        print(f"tu saldo actual es de {saldo}")
    elif usu == 2: 
        valor=float(input("ingreasr cantidad que quiere depositar: "))
        print(f"su saldo queda en {saldo + valor}")
    elif usu == 3: 
        va=float(input("ingrese valor que quiere retirar: "))
        print(f"su saldo queda en {saldo - va}")
    