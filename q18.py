import base as base
import q13 as q13

def invertelista(lista1, lista2):
    if not lista1:
        return lista2

    return invertelista(base.init(lista1), lista2 + [base.last(lista1)])

def main():
    print("Hello, World!")

    
    lista1 = ['b', 'o', 'm']
    lista2 = []

    print(invertelista(lista1, lista2))


if __name__ == "__main__":
    main()