import base as base
import q13 as q13

def sup(lista1, lista2, num):
    if not lista2:
        return lista1

    if(base.head(lista2) > num):
        return sup(q13.concat_list(lista1, [base.head(lista2)]), base.tail(lista2), num)

    return sup(lista1, base.tail(lista2), num)

def main():
    print("Hello, World!")

    lista1 = []
    lista2 = [1, 20, 13]
    print(sup(lista1, lista2, 4))


if __name__ == "__main__":
    main()