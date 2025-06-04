#!/usr/bin/env python3
"""Genera contraseñas seguras aleatorias."""
import argparse
import secrets
import string

# Caracteres disponibles: letras, dígitos y símbolos
CHARSET = string.ascii_letters + string.digits + string.punctuation

def generate_password(length: int) -> str:
    """Retorna una contraseña aleatoria de la longitud indicada."""
    return ''.join(secrets.choice(CHARSET) for _ in range(length))

def main():
    parser = argparse.ArgumentParser(description="Generador de contraseñas seguras")
    parser.add_argument('-l', '--length', type=int, default=16,
                        help='Longitud de la contraseña (por defecto: 16)')
    args = parser.parse_args()
    print(generate_password(args.length))

if __name__ == '__main__':
    main()
