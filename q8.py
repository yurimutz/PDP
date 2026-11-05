def negativos(sum):
    num = int(input())

    if(num == 0):
        return sum
    
    if(num > 0):
        return negativos(sum)
    else:
        return negativos(sum+num)
             

def main():
    print("Hello, World!")

    sum = 0
    print(negativos(sum))


if __name__ == "__main__":
    main()