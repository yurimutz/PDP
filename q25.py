import q24 as q24
import base as base
import functools as functools

def sup_qtd(lista, num, sum):
    if not lista:
        return sum

    if(base.head(lista) == num):
        return sup_qtd(base.tail(lista), num, sum+1)

    return sup_qtd(base.tail(lista), num, sum)

def shift(lista, elemento):
    if not lista:
        return []

    if base.head(lista) == elemento:
        return shift(base.tail(lista), elemento)

    return lista

def aux(lista):
    if not lista:
        return []

    return [base.head(lista), sup_qtd(lista, base.head(lista), 0)]


def aux2(lista):
    if not lista:
        return []

    return [aux(lista)] + aux2(shift(lista, base.head(lista)))

def primeFactors(num):
    return aux2(q24.primes(num))

def main():
    print("Hello, World!")
    print(primeFactors(61))


if __name__ == "__main__":
    main()