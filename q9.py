def negativos(sum, num):
    if(num == 0):
        return sum
 
    inp = float(input())

    if(inp < 0):
        return negativos(sum+1, num-1)

    return negativos(sum, num-1)


def main():
    print("Hello, World!")

    sum = 0
    print(negativos(sum, 3))


if __name__ == "__main__":
    main()