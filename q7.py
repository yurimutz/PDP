import q6 as q6

def sequencia(n):
    if(n == 0):
        return 1

    return 1 / q6.fatorial(n) + sequencia(n-1)

def main():
    print("Hello, World!")

    num = int(input())
    print(sequencia(num))


if __name__ == "__main__":
    main()