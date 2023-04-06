# Implementar la función es_vocal, que reciba un carácter y
# devuelva un booleano en base a si letra es una vocal o no.


# Resolver utilizando listas y el operador in.
def es_vocal(letra):
    return letra in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']


print(es_vocal('a'))