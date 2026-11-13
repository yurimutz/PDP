import base as base

def shift(lista, elemento):
    if not lista:
        return []

    if base.head(lista) == elemento:
        return shift(base.tail(lista), elemento)

    return lista

def anda(lista, elemento):
    if not lista:
        return []

    if base.head(lista) == elemento:
        return base.tail(lista)

    return anda(base.tail(lista), elemento)

def pega(lista, elemento):
    if not lista:
        return []

    if base.head(lista) == elemento:
        return []

    return [base.head(lista)] + pega(base.tail(lista), elemento)

def splitToken(num, lista):
    if not lista:
        return []

    if base.head(lista) == num:
        return splitToken(num, shift(lista, num))

    return [pega(lista, num)] + splitToken(num, anda(lista, num))

def main():
    print("Hello, World!")
    lista =  [1,2,3,4,2,5,67,8,9,2,0,3]
    print(splitToken( 2, lista))


if __name__ == "__main__":
    main()