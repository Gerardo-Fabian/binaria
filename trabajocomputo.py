def binaria(lista, x):
    if len(lista) <=0:
        return "Número no encontrado"

    m = lista[len(lista)// 2]
    if m == x:
       return "Número encontrado"
    else:
        if x < m:
            return binaria(lista[:len(lista)// 2],x)
        else:
            return binaria(lista[(len(lista)// 2)+1:],x)

