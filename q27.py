import base as base
import q13 as q13

def joinToken(num, lista):
    if not lista:
        return []
    
    if not base.tail(lista):
        return base.head(lista) + joinToken(num, base.tail(lista))
        
    return q13.concat_list((q13.concat_list(base.head(lista), [num])), joinToken(num, base.tail(lista)))


def main():
    print("Hello, World!")

    lista1 =  [1,2,3,4,2,5,67,8,9,2,0,3]
    lista = [[1], [3,4, 7, 10], [5, 67, 8, 9], [0, 3]]

    print(joinToken( 2, lista))


if __name__ == "__main__":
    main()