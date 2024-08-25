numero = 1

while numero < 100:
    print(numero)
    numero *= 2

comando = ""

while comando.lower != "salir":
    comando = input("Ingrese alguna vuelta: \n")
    print(comando)

while True:
    comando = input("Ingrese alguna vuelta: \n")
    print(comando)
    if comando.lower() == "salir":
        break
    