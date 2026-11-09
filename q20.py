import q14 as q14
import base as base

def strip(lista1, lista2):
    if not lista2:
        return []

    if q14.verifica(lista1, base.head(lista2)):
        return strip(lista1, base.tail(lista2))

    return [base.head(lista2)] + strip(lista1, base.tail(lista2))

def main():
    print("Hello, World!")

    lista1 = ['a', 'b', 'c']
    lista2 = ['d', 'a', 'e', 'a']

    print(strip(lista1, lista2))

if __name__ == "__main__":
    main()