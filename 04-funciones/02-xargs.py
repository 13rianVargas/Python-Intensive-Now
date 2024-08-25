def suma(*numeros): # * = el asterisco transforma a los parametros en algo iterable
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(2,5,7)
suma(2,5,7,9)
suma(2,8)
    