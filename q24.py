import q11 as q11

def aux(num, fator):

    if num == 1:
        return []

    if(q11.ehPrimo(fator)):
        if(num % fator == 0):
            return [fator] + aux(num / fator, fator)

    return aux(num, fator+1)

def primes(num):
    return aux(num, 2)

def main():
    print("Hello, World!")

    print(primes(24))


if __name__ == "__main__":
    main()