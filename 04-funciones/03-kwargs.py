def getProduct(**datos): # ** = esto nos obliga a colocar el nombre del parametro seguido del parametro (no tiene limite)
    print(datos["name"])

getProduct(id = "id",
           name = "iPhone",
           desc = "This is an iPhone.")