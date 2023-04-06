# Implementar la función operacion, donde:
# - Si multiplicar es True: devolver la multiplicación entre a y b.
# - Si multiplicar es False: devolver la division entre a y b.
# - Si multiplicar es False y b es cero: imprimir por consola "Operación no valida".


def operacion(a, b, multiplicar):
    if multiplicar:
        return a * b
    elif multiplicar == False and b != 0:
        return a / b
    else:
        return "Operacion no valida"

print(operacion(1, 0, 0))
