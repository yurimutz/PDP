import q11 as q11

def retPrimo(qtd, num, lista):
    if qtd == 0:
        return lista

    if q11.ehPrimo(num):
        return retPrimo(qtd-1, num+1, lista + [num])
    
    return retPrimo(qtd, num+1, lista)

def main():
    print("Hello, World!")

    num = 5
    lista = []
    print(retPrimo(num, 1, lista))


if __name__ == "__main__":
    main()