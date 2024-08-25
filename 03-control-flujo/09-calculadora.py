print("\nBienvenidos a la calculadora \n\nPara salir escribe 'Salir' en cualquier momento.\n")

res = ""

while True:

    if not res:
        res = input("Ingrese un número: ")
        if res.lower() == "salir":
            break
        res = int(res)

    op =  input("Ingrese una operación (+, -, *, /): ")
    if op.lower() == "salir":
        break

    num2 = input("Ingrese siguiente número: ")
    if num2.lower() == "salir":
        break
    num2 = int(num2)

    if  op == "+":
        res += num2
    elif  op == "-":
        res -= num2
    elif op  == "*":
        res *= num2
    elif  op == "/":
        if num2 != "0":
            res /= num2
        else:
            print("No se puede dividir entre cero")
    else:
        print("Operación no válida")
        break
    print(f"El resultado es: {res}")