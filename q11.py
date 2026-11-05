def verifica_div(num, div):

    if(div == num):
        return True

    if(num % div == 0):
        return False

    return verifica_div(num, div+1)

def ehPrimo(num):
    if(num <= 1):
        return False

    if num == 2:
        return True

    return verifica_div(num, 2)


def main():
    print("Hello, World!")

    num = 11
    print(ehPrimo(num))


if __name__ == "__main__":
    main()