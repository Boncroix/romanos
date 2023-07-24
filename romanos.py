def convertir_a_romano(numero):
    # Comprobar número entero
    if isinstance(numero, (int, float)):
        print(f'Error: debes introducir un número entero ({numero})')

    # Comprobar que número está entre 2 números
    if not (0 < numero < 4000):
        return f'Error: el número debe estar entre 1 y 3999 ({numero})'
    return 'TODO: convertir a romano'

    millares = ['', 'M', 'MM', 'MMM']
    centenas = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    decenas = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    unidades = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

    millar = numero // 1000
    centena = (numero % 1000) // 100
    decena = ((numero % 1000) % 100) // 10
    unidad = (((numero % 1000) % 100) % 10) // 1

    romano = millares[millar], centenas[centena], decenas[decena], unidad[unidad]

    return romano
