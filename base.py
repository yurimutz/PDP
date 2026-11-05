def head(lista):
    return lista[0]

def tail(lista):
    aux = []
    tam = len(lista)
    for i in range(1, tam):
        aux.append(lista[i])
    return aux

def init(lista):
    aux = []
    tam = len(lista)
    for i in range(0, tam-1):
        aux.append(lista[i])
    return aux

def last(lista):
    tam = len(lista)
    return lista[tam-1]

def main():
    print("Hello, World!")

    lista = [1,2,3,4]
    print(init(lista))


if __name__ == "__main__":
    main()