def esPalindromo(texto):
    texto = noSpace(texto)
    textoInvertido = reverse(texto)
    return texto.lower() == textoInvertido.lower()

def noSpace(texto):
    newTexto=""
    for char in texto:
        if char != " ":
            newTexto += char
    return newTexto

def reverse(texto):
    textoInvertido =""
    for char in texto:
        textoInvertido = char + textoInvertido
    return textoInvertido

print("Abba <=>", esPalindromo("Abba"))
print("Reconocer <=>", esPalindromo("Reconocer"))
print("Amo la paloma <=>", esPalindromo("Amo la paloma"))
print("Hello World <=>", esPalindromo("Hello World"))
