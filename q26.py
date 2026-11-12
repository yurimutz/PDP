import base as base

def shift(lista, elemento):
    if not lista:
        return []

    if base.head(lista) == elemento:
        return 

    return lista

def aux(lista, elemento):
    if not lista:
        return []

    if base.head(lista) == elemento:
        return []

    return [base.head(lista)] + aux(base.tail(lista), elemento) 


def splitToken(num, lista):
    if not lista:
        return []

    return aux(lista, num) + splitToken(num, shift(lista, num))


def main():
    print("Hello, World!")
    lista =  [1,2,3,4,2,5,67,8,9,0,3]
    print(splitToken( 2, lista))


if __name__ == "__main__":
    main()