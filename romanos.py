def convertir_a_romano(numero):
    # Comprobar número entero
    if isinstance(numero, (int, float)):
        print(f'Error: debes introducir un número entero ({numero})')

    # Comprobar que número está entre 2 números
    if not (0 < numero < 4000):
        return f'Error: el número debe estar entre 1 y 3999 ({numero})'
    return 'TODO: convertir a romano'
