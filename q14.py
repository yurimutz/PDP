import base as base

def verifica(lista, elemento):
    if not lista:
        return False

    if(base.head(lista) == elemento):
        return True

    return verifica(base.tail(lista), elemento)


def main():
    print("Hello, World!")

    lista = ['a', 1, 3, 'j']
    print(verifica(lista, 3))


if __name__ == "__main__":
    main()