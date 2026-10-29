import aula

def q7(n):
    if n == 0:
        return 1

    return (1 / aula.fatorial(n)) + q7(n-1);

def main():
    num = int(input())
    print(q7(num))

if __name__ == "__main__":
    main()