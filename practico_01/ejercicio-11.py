# Implementar la función es_primo(), que devuelva un booleano en base a
# si numero es primo o no.


def es_primo(numero):
    if numero > 0:
        for i in range(2, numero - 1):
            if numero % i == 0:
                return False
        return True
    else:
        return False

print(es_primo(37))

