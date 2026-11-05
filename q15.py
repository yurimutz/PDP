import base as base
import q14 as q14

def concat_list(l1, l2):
    if not l2:
        return l1

    if(q14.verifica(l1, base.head(l2))):
        return concat_list(l1, base.tail(l2))

    return concat_list(l1 + [base.head(l2)], base.tail(l2))

def main():
    print("Hello, World!")

    
    lista1 = ['b', 'o', 'm']
    lista2 = ['d', 'i', 'a', 'e', 'o', 'a']

    print(concat_list(lista1, lista2))


if __name__ == "__main__":
    main()