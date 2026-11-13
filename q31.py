import q10 as q10
import q30 as q30
import base as base

def acessaIndice(lista, index):
    if index == 0:
        return base.head(lista)

    return acessaIndice(base.tail(lista), index-1)

def prodEsc(vet1, vet2):

    return q30.soma([acessaIndice(vet1, x) * acessaIndice(vet2, x) for x in range(q10.tamanho(0,vet1))])

def main():
    print("Hello, World!")

    vet1 = [1,2,3,1]
    vet2 = [1,2,3,1]

    print(prodEsc(vet1, vet2))

if __name__ == "__main__":
    main()