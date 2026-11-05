import base as base

def tamanho(sum, lista):
    if not lista:
        return sum

    return tamanho(sum+1, base.tail(lista))

def main():
    print("Hello, World!")

    sum = 0
    lista = [1, 4, 'a', 2, 2, 2]
    print(tamanho(sum, lista))


if __name__ == "__main__":
    main()