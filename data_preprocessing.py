from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
import datetime

''' PREPROCESSING
    Section to check whether the data provided are free of errors
    and belong to the period of interest (2020).
    
    PREPROCESAMIENTO
    Sección dedicada a verificar si los datos proporcionados no tienen errores 
    y pertenecen al período (2020) del que se nos ha pedido hacer el análisis. 
'''

"""
    Features of every data with which we work:

    - product = [id_product, name, price, category, stock]
    - sale = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
    - search = [id_search, id_product]
"""


def sublista(lista, n):
    """Function to obtain a sublist from the n-th entries of a collection of lists.
    :param lista: list of lists
    :param n: n-th entry according to which we obtain the sublist
    :return sublista: list of the n-th entries of the lists of the list
    """
    sublista = []
    for i in range(len(lista)):
        sublista.append(lista[i][n])
    return sublista


def verifica_inconsistencias():
    """Function to check if there are inconsistencies in the data provided
    :return:
    """
    mensaje_de_error = '''
        Existen  inconsistencias en los datos proporcionados.
        Datos enviados para revisión.
        '''

    # verifica si existen identificadores o nombres de productos repetidos
    if len(set(sublista(lifestore_products, 0))) != len(lifestore_products) or \
            len(set(sublista(lifestore_products, 1))) != len(lifestore_products):
        exit(mensaje_de_error)

    # verifica si existen identificadores de ventas repetidos
    if len(set(sublista(lifestore_sales, 0))) != len(lifestore_sales):
        exit(mensaje_de_error)

    # verifica si existen identificadores de búsquedas repetidos
    if len(set(sublista(lifestore_searches, 0))) != len(lifestore_searches):
        exit(mensaje_de_error)

    # verifica si las reseñas de los productos se encuentran en el rango válido de 1 a 5
    for score in set(sublista(lifestore_sales, 2)):
        if score in {1, 2, 3, 4, 5}:
            continue
        else:
            exit(mensaje_de_error)

    # verifica si los valores que toma la variable refund sólo se encuentra en el rango de 0 a 1
    for refund in set(sublista(lifestore_sales, 4)):
        if refund in {0, 1}:
            continue
        else:
            exit(mensaje_de_error)

    productos_id = sublista(lifestore_products, 0)

    # verifica si las id_product de las ventas corresponden a un producto existente
    for sale in lifestore_sales:
        if sale[1] in productos_id:
            continue
        else:
            exit(mensaje_de_error)

    # verifica si las id_product de las búsquedas corresponden a un producto existente
    for search in lifestore_searches:
        if search[1] in productos_id:
            continue
        else:
            exit(mensaje_de_error)


# verifica_inconsistencias()


def is_IDs_sorted(list_of_elements):
    """Function that verifies the IDs of the objects are in increasing order (one at a time)
    :param list_of_elements: list of elements (products, sales, searches)
    :return IDs:
    """
    IDs = sublista(list_of_elements, 0)
    return IDs == sorted(IDs), IDs[-1] == len(list_of_elements)


# print(is_IDs_sorted(lifestore_sales))
# print(is_IDs_sorted(lifestore_products))
# print(is_IDs_sorted(lifestore_searches))


def verifica_fecha(fecha):
    try:
        datetime.datetime.strptime(fecha, '%d/%m/%Y')
        return True
    except ValueError:
        return False


# función para seleccionar las ventas que tienen:
# - el id_product en el rango 1 a 96
# - su score en el rango 1 a 5
# - su refund en el rango 0 a 1
# - fechas válidas
def clasifica_ventas(ventas):
    """Function to obtain the sales with valid values
    :param ventas: list of sales
    :return ventas_sin_errores, ventas_con_errores: tuple of two lists, the first has the sales with
    valid values and the second has the sales with some error
    """
    ventas_sin_errores = []
    ventas_con_errores = []
    for venta in ventas:
        if venta[1] > 0 and venta[1] < 97:
            if venta[2] in [1, 2, 3, 4, 5]:
                if verifica_fecha(venta[3]) and venta[3][6:10] == '2020':
                    if venta[4] in [0, 1]:
                        ventas_sin_errores.append(venta)
                    else:
                        ventas_con_errores.append([venta, 4])
                else:
                    ventas_con_errores.append([venta, 3])
            else:
                ventas_con_errores.append([venta, 2])
        else:
            ventas_con_errores.append([venta, 1])
    return ventas_sin_errores, ventas_con_errores


# ventas_sin_errores , ventas_con_errores = clasifica_ventas(lifestore_sales)
# print(ventas_sin_errores)
# print(ventas_con_errores)

def ventas_no_errores(ventas):
    """Function that returns a list of sales with the sales that hasn't any error
    :param ventas: list of sales
    :return ventas1: list of the sales without errors
    """
    ventas1, ventas2 = clasifica_ventas(ventas)
    return ventas1

# print(ventas_no_errores(lifestore_sales))
