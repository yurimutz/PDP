import base as base;

def fibonnaci(n):
    if(n) == 0:
        return 0

    if(n) == 1:
        return 1

    return fibonnaci(n-1) + fibonnaci(n-2)


def main():
    print("Hello, World!")

    print(fibonnaci(3))


if __name__ == "__main__":
    main()