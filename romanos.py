def convertir_a_romano(numero):
    # Comprobar número entero
    if not isinstance(numero, (int, float)):
        print(f'Error: debes introducir un número entero ({numero})')

    # Comprobar que número está entre 2 números
    if not (0 < numero < 4000):
        return f'Error: el número debe estar entre 1 y 3999 ({numero})'

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


def romano_a_entero(romano):
    digitos_romanos = {'I': 1,
                       'V': 5,
                       'X': 10,
                       'L': 50,
                       'C': 100,
                       'D': 500,
                       'M': 1000
                       }

    if not isinstance(romano, str):
        return 'ERROR: tiene que ser un número romano en formato cadena de texto'

    resultado = 0
    anterior = 0
    for letra in romano:
        if letra not in digitos_romanos:
            return f'ERROR: {letra} no es un dígito romano válido (I, V, X, L, C, D, M)'
        actual = digitos_romanos[letra]

        if anterior < actual:
            # deshacer la suma  que hemos hecho en la iteración anterior
            resultado = resultado - anterior
            # sumar el valor actual, pero restando el anterior
            resultado = resultado + (actual - anterior)
        else:
            resultado = resultado + anterior

        anterior = actual

    return resultado


errores = ['A', '', 4, ['X', 'X', 'I'], 'IV']
pruebas = ['I', 'MMMCMXCIX']
for valor in errores:
    print(romano_a_entero(valor))
