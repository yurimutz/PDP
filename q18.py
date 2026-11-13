import base as base
import q13 as q13

# fiz sem a q13
# def invertelista(lista1, lista2):
#     if not lista1:
#         return lista2
    
#     return invertelista(base.init(lista1), lista2 + [base.last(lista1)])

def invertelista(lista1):
    if not lista1:
        return []

    return q13.concat_list(invertelista(base.tail(lista1)), [base.head(lista1)])

def main():
    print("Hello, World!")

    
    lista1 = ['b', 'o', 'm']

    print(invertelista(lista1))


if __name__ == "__main__":
    main()