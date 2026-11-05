import base as base;

def fatorial(n):
    if(n == 0):
        return 1

    return n * fatorial(n-1)

def main():
    print("Hello, World!")

    print(fatorial(3))

if __name__ == "__main__":
    main()