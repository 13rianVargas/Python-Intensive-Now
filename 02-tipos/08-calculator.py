n1 = input("Ingresa primer número.")
n2 = input("Ingresa segundo número.")

print(n1,n2)
print(n1 + n2)
n1 = int(n1)
n2 = int(n2)
print(n1 + n2)

sum = n1 + n2
res = n1 - n2
mul = n1 * n2
div = n1 / n2

mensaje = f"""
Para los números {n1} y {n2},
el resultado de la suma es: {sum},
el resultado de la resta es: {res},
el resultado de la multiplicación es: {mul},
el resultado de la división es: {div},
"""
print(mensaje)


