usuario = int(input("en que año naciste: "))
if usuario <= 1940:
    print("eres una generacion silenciosa")
elif usuario <= 1964:
    print("eres de la  generacion baby boomer ")
elif usuario <= 1979:
    print("eres de la  generacion X ")
elif usuario <= 2000:
    print("eres de la  generacion Y ")
elif usuario <= 2010:
    print("eres de la  generacion Z ")
else:
    print("eres muy joven")