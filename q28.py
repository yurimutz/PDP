import base as base
import q10 as q10

def anda(lista, inicio):
    if inicio <= 0:
        return lista

    return anda(base.tail(lista), inicio-1)

def aux(lista, inicio, fim):
    if not lista:
        return []

    if inicio == fim:
        return []

    return [base.head(lista)] + aux(base.tail(lista), inicio+1, fim)

def splitHalf(lista):

    tam = q10.tamanho(0, lista)
    
    return [aux(lista, 0, int(tam/2))] + [aux(anda(lista, int(tam/2)), int(tam/2), tam)]

def main():
    print("Hello, World!")

    lista =  [1,2,3,4,2,5,67,8,9,2,0,3]

    print(splitHalf(lista))


if __name__ == "__main__":
    main()