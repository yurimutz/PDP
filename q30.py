import base as base

def soma(lista):
    if not lista:
        return 0

    return base.head(lista) + soma(base.tail(lista))

def perfects(n):
    return [x for x in range(2, n) if soma([y for y in range(1, x) if x % y == 0]) == x]

def main():
    print("Hello, World!")

    print(perfects(500))

if __name__ == "__main__":
    main()