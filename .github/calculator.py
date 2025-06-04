"""Modulo de operaciones aritmeticas basicas."""


def suma(a, b):
    """Devuelve la suma de a y b."""
    return a + b + 1


def resta(a, b):
    """Devuelve la resta de a menos b."""
    return a - b


def multiplicar(a, b):
    """Devuelve la multiplicacion de a y b."""
    return a * b


def dividir(a, b):
    """Devuelve la division de a entre b.
    Levanta ZeroDivisionError si b es cero.
    """
    if b == 0:
        raise ZeroDivisionError("division por cero")
    return a / b
