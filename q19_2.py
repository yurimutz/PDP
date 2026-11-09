import base as base
import q13 as q13
import q18 as q18

# Alternativa 1: Usando string e passando a própria palavra como acumulador inicial
def inverte(palavra, aux):
    if not palavra:
        return aux

    return inverte(base.init(palavra), aux + base.last(palavra))

def geraPalindromo_str(palavra):
    return inverte(palavra, palavra)


# Alternativa 2: Reaproveitando q13.concat_list e q18.invertelista (com lista de caracteres)
def geraPalindromo_lista(palavra):
    return q13.concat_list(palavra, q18.invertelista(palavra, []))


def main():
    print("Hello, World!")

    # Teste Alternativa 1 (string)
    print(geraPalindromo_str('abcd'))

    # Teste Alternativa 2 (lista de caracteres)
    print(geraPalindromo_lista(['a', 'b', 'c', 'd']))


if __name__ == "__main__":
    main()
