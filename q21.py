import base as base
import q20 as q20

# q20 retornando lista
def consoantList(lista1, lista2):
    return q20.strip([], lista1) == q20.strip(['a','e','i','o','u'], lista2)

# so se a q20 retornar string
# def consoantList(lista1, lista2):
#     return lista1 == q20.strip(['a','e','i','o','u'], lista2)

def main():
    print("Hello, World!")

    print(consoantList("sdd", "saude"))
    print(consoantList("sdd", "saudade"))


if __name__ == "__main__":
    main()
