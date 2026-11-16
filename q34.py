import base as base
import q13 as q13

def shift(lista, elemento):
    if not lista:
        return []

    if base.head(lista) == elemento:
        return shift(base.tail(lista), elemento)

    return lista

def compress(lista):
    if not lista:
        return []

    return [base.head(lista)] + compress(shift(lista, base.head(lista)))

def main():
    print("Hello, World!")

    print(compress([1,1,1,2,7,7,7,8,3,4]))

if __name__ == "__main__":
    main()