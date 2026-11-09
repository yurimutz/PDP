import base as base
import q14 as q14

# Alternativa 1: Recebendo apenas (l1, l2)
def strip(l1, l2):
    if not l2:
        return []

    if(q14.verifica(l1, base.head(l2))):
        return strip(l1, base.tail(l2))

    return [base.head(l2)] + strip(l1, base.tail(l2))


# Alternativa 2: Com lista acumuladora (l1, l2, aux), no mesmo padrão das questões anteriores
def strip_acc(l1, l2, aux):
    if not l2:
        return aux

    if(q14.verifica(l1, base.head(l2))):
        return strip_acc(l1, base.tail(l2), aux)

    return strip_acc(l1, base.tail(l2), aux + [base.head(l2)])


def main():
    print("Hello, World!")

    lista1 = ['a', 'e', 'i', 'o', 'u']
    lista2 = ['s', 'a', 'u', 'd', 'a', 'd', 'e']

    print(strip(lista1, lista2))
    print(strip_acc(lista1, lista2, []))


if __name__ == "__main__":
    main()
