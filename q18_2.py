import base as base
import q13 as q13

# Alternativa 1: Recebendo apenas 1 lista (como no exemplo do PDF) usando head, tail e q13.concat_list
def invertelista(lista1):
    if not lista1:
        return []

    return q13.concat_list(invertelista(base.tail(lista1)), [base.head(lista1)])


# Alternativa 2: Mantendo o acumulador (lista1, lista2) e usando head, tail e q13.concat_list
def invertelista_acc(lista1, lista2):
    if not lista1:
        return lista2

    return invertelista_acc(base.tail(lista1), q13.concat_list([base.head(lista1)], lista2))


def main():
    print("Hello, World!")

    lista1 = ['b', 'o', 'm']
    lista2 = []

    print(invertelista(lista1))
    print(invertelista_acc(lista1, lista2))


if __name__ == "__main__":
    main()
