mascotas = ["Rorito","Floppy","Orión","Kissy"]

print(mascotas[1])

mascotas[0] = "Crazy"
print(mascotas)

print(mascotas[2:])#Orion, Kissy
print(mascotas[-1])#Kissy
print(mascotas[1:2:2])#Floppy

numeros = list(range(21))
print(numeros[::2])#numeros pares
print(numeros[1::2])#numeros inpares
