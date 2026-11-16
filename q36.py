import base as base
import q13 as q13

def shift(lista, elemento):
    if not lista:
        return []

    if base.head(lista) == elemento:
        return shift(base.tail(lista), elemento)

    return lista

def num(lista, elemento):
    if not lista:
        return 0

    if base.head(lista) == elemento:
        return 1 + num(base.tail(lista), elemento)

    return 0

def encode(lista):
    if not lista:
        return []

    return q13.concat_list(([[num(lista, base.head(lista))] + [base.head(lista)]]), encode(shift(lista, base.head(lista))))

def main():
    print("Hello, World!")

    print(encode("aaaabccaadeeee"))

if __name__ == "__main__":
    main()