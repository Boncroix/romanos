
def convertir_a_romano(numero):
    if type(numero) != int:
        return f"Error: debes introducir un número entero ({numero})"

    # validar el valor del número
    if not (0 < numero < 4000):
        return f"Error: el número debe estar entre 1 y 3999 ({numero})"

    conversores = [
        ["", "M", "MM", "MMM"],
        ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
        ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
        ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
    ]

    divisores = [1000, 100, 10, 1]

    resultado = ""
    contador = 0

    for divisor in divisores:
        cociente = (numero // divisor)
        numero = numero % divisor
        resultado = resultado + conversores[contador][cociente]
        contador = contador + 1

    return resultado


def romano_a_entero(romano):
    romano = romano.upper()

    digitos_romanos = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    if not isinstance(romano, str):
        raise TypeError(
            'ERROR: tiene que ser un número romano en formato cadena de texto')

    resultado = 0
    anterior = 0

    for letra in romano:

        letra_repetida = romano.count(letra)
        if letra_repetida > 3:
            raise ValueError(
                f'ERROR: Numero romano no valido la letra {letra} repetida más de 3 veces')

        if letra not in digitos_romanos:
            raise ValueError(
                f'ERROR: {letra} no es un dígito romano válido (I, V, X, L, C, D, M)')

        actual = digitos_romanos[letra]

        if anterior < actual:
            # comprobar que la resta es posible
            # el orden de magnitud no es mayor de uno

            if anterior > 0 and len(str(actual)) - len(str(anterior)) > 1:
                raise ValueError(
                    f"ERROR: resta no posible (ant: {anterior}, act: {actual})")

            # deshacer la suma (que hemos hecho en la iteración anterior)
            # DCI --- DC
            resultado = resultado - anterior
            # DC(IV) 600 + 4 = 600 + (5 - 1) = resultado + (actual - anterior)
            # sumar el valor actual, pero restando el anterior
            resultado = resultado + (actual - anterior)
        else:
            resultado = resultado + actual

        anterior = actual

    return resultado


'''
errores = ['A', '', 3, ['X', 'X', 'I']]
pruebas = ['IIII', 'I', 'MCXXIII', 'VIII', 'LVI', 'IV',
           'IX', 'XC', 'CM', 'IC', 'IM', 'XM', 'ID', 'VX']


for valor in pruebas:
    try:
        print(romano_a_entero(valor))
    except TypeError as te:
        print('Uy! el tipo no es válido')
    except ValueError as ve:
        print('Va a ser que esa cadena no es un número romano valido')
    except Exception as ex:
        print('Hey!!! Alto ha salido mal', ex)
'''
