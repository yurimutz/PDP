import base as base
import q13 as q13

def concat_str(s1, s2):
    if not s2:
        return s1

    return concat_str(s1 + base.head(s2), base.tail(s2))

def monta(num, elemento):
    if num == 0:
        return ""

    return elemento + monta(num-1, elemento)

def traduz(lista):
    return monta(base.head(lista), base.last(lista))


def decode(lista):
    if not lista:
        return ""

    return concat_str(traduz(base.head(lista)), decode(base.tail(lista)))

def main():
    print("Hello, World!")

    print(decode([(4, 'a'), (1, 'b'), (2, 'c'), (2, 'a'), (1, 'd'), (4, 'e')]))

if __name__ == "__main__":
    main()