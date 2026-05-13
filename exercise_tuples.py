def get_coordinate(registro):
    """
    Retorna la coordenada del mapa desde una tupla (tesoro, coordenada).

    Args:
        registro: Una tupla con el formato (tesoro, coordenada)

    Returns:
        Un string con la coordenada del mapa
    """
    return registro[1]


def convert_coordinate(coordenada):
    """
    Separa una coordenada de formato "2A" en sus componentes ("2", "A").

    Args:
        coordenada: Un string con la coordenada (ej: "2A", "7F")

    Returns:
        Una tupla con los componentes individuales (ej: ("2", "A"))
    """
    return (coordenada[0], coordenada[1])

def create_record(registro_azara, registro_rui):
    """
    Combina los registros de Azara y Rui si sus coordenadas coinciden.
    """

    # sacar coordenada de Azara
    coord_azara = registro_azara[1]

    # convertir "4B" → ("4", "B")
    coord_azara_convertida = convert_coordinate(coord_azara)

    # sacar coordenada de Rui
    coord_rui = registro_rui[1]

    # verificar si coinciden
    if coord_azara_convertida == coord_rui:

        return (
            registro_azara[0],   # tesoro
            registro_azara[1],   # coordenada azara
            registro_rui[0],     # ubicacion
            registro_rui[1],     # coordenada rui
            registro_rui[2]      # cuadrante
        )

    else:
        return "not a match"


def sum_tuple(numeros):
    """
    Recorre una tupla de números y retorna la suma total.
    """

    total = 0

    for numero in numeros:
        total = total + numero

    return total

def count_occurrences(tupla, elemento):
    """
    Recorre la tupla y cuenta cuántas veces aparece el elemento.
    """

    contador = 0

    for valor in tupla:
        if valor == elemento:
            contador = contador + 1

    return contador


def find_index(tupla, elemento):
    """
    Retorna el índice de la primera aparición del elemento.
    """

    indice = 0

    for valor in tupla:

        if valor == elemento:
            return indice

        indice = indice + 1

    return -1


def filter_positives(numeros):
    """
    Retorna una nueva tupla con solo los números positivos.
    """

    positivos = ()

    for numero in numeros:

        if numero > 0:
            positivos = positivos + (numero,)

    return positivos