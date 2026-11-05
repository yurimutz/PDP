import base as base

def sup_qtd(lista, num, sum):
    if not lista:
        return sum

    if(base.head(lista) > num):
        return sup_qtd(base.tail(lista), num, sum+1)

    return sup_qtd(base.tail(lista), num, sum)

def main():
    print("Hello, World!")
   
    lista = [1, 20, 13]
    sum = 0
    print(sup_qtd(lista, 4, sum))


if __name__ == "__main__":
    main()