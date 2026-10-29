import aula

def q8(lista):
    if(aula.head(lista) == 0):
        return 0
    if(aula.head(lista) < 0):
        return aula.head(lista) + q8(aula.tail(lista))
    
    return q8(aula.tail(lista))

def main():

    numeros = [10, 20, 30, 40, -10, 0]
    print(q8(numeros))

if __name__ == "__main__":
    main()