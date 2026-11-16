import base as base
import q13 as q13

def shift(lista, elemento):
    if not lista:
        return []

    if base.head(lista) == elemento:
        return shift(base.tail(lista), elemento)

    return lista

def junta(lista, elemento):
    if not lista:
        return []

    if base.head(lista) == elemento:
        return [base.head(lista)] + junta(base.tail(lista), elemento)

    return []

def pack(lista):
    if not lista:
        return []

    return q13.concat_list([junta(lista, base.head(lista))], pack(shift(lista, base.head(lista))))

def main():
    print("Hello, World!")

    print(pack([1,1,1,2,3,3,3,4,2,2,8,8,7,9]))

if __name__ == "__main__":
    main()