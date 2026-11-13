import base as base
import q13 as q13
import q18 as q18

def inverte(palavra, aux):
    if not palavra:
        return aux

    return inverte(base.init(palavra), aux + base.last(palavra))
    
def geraPalindromo(palavra):
    return inverte(palavra, palavra)

def main():
    print("Hello, World!")

    print(geraPalindromo('abcd'))


if __name__ == "__main__":
    main()