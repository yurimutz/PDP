import base as base
import q14 as q14
import q21 as q21

def matches(lista, consoantes):
    if not lista:
        return []

    if q21.consoantList(consoantes, base.head(lista)):
        return [base.head(lista)] + matches(base.tail(lista), consoantes)

    return matches(consoantes, base.tail(lista))
    

def main():
    print("Hello, World!")

    dic = ['arara', 'oi', 'ola', 'arara']

    print(matches(dic, 'rr'))


if __name__ == "__main__":
    main()