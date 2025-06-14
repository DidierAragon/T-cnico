saldo = 0
print("bienvenido a su cuenta porfaor ingrese el numero da lo que quiere realizar:")
print("1 ver saldo")
print("2 depositar saldo")
print("3 retirar saldo")
usu = int(input("ingresar numero: "))

if usu == 1:
    print(f"tu saldo actual es de {saldo}")
elif usu == 2:
    valor=float(input("ingreasr cantidad que quiere depositar: "))
    print(f"su saldo queda en {saldo + valor}")
elif usu == 3:
    va=float(input("ingrese valor que quiere retirar: "))
    print(f"su saldo queda en {saldo - va}")
else:
    print("error")