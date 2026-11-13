def pyths(n):

    res = [(x,y,z) for x in range(1,n+1) for y in range(1,n+1) for z in range(1,n+1) if (x*x) + (y*y) == (z*z)]

    return res

def main():
    print("Hello, World!")

    print(pyths(5))


if __name__ == "__main__":
    main()