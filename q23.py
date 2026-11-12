import q12 as q12
import base as base
import q11 as q11

def aux(num, ver):
    if q11.ehPrimo(ver):
        if(ver > num):
            return ver

    return aux(num, ver+1)

def proximoPrimo(num):
    return aux(num,1)

def main():
    print("Hello, World!")

    print(proximoPrimo(5))


if __name__ == "__main__":
    main()