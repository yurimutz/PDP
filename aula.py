def head(lista):
    return lista[0]

def tail(lista):
    tam = len(lista)
    lista2 = []
    for i in range(1, tam):
        lista2.append(lista[i])

    return lista2;

def init(lista):
    tam = len(lista) - 1
    lista2 = []
    for i in range(tam):
        lista2.append(lista[i])

    return lista2;

def last(lista):
    return lista[-1];

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n-1) 

def main():
    print("Hello, World!")
    
    # Testando as funções
    numeros = [10, 20, 30, 40]
    print("Head:", head(numeros))
    print("Tail:", tail(numeros))
    print("Init:", init(numeros))
    print("Last:", last(numeros))

    num = int(input());
    print("Fibonacci:", fibonacci(num))
    print("Fatorial:", fatorial(num))

if __name__ == "__main__":
    main()


