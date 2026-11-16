import base as base

def isPalindrome(string):
    if not string:
        return True

    if base.head(string) != base.last(string):
        return False

    return isPalindrome(base.tail(base.init(string)))

def main():
    print("Hello, World!")

    print(isPalindrome('oi tudo odut io'))

if __name__ == "__main__":
    main()