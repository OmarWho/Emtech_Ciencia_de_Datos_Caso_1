from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

''' PREPROCESAMIENTO
    Sección dedicada a verificar si los datos proporcionados no tienen errores 
    y pertenecen al período (2020) del que se nos ha pedido hacer el análisis. 
'''

# función que permite obtener una sublista de las n-ésimas entradas de las listas
# que conforman otra lista
def sublista(lista, n):
    sublista = []
    for i in range(len(lista)):
        sublista.append(lista[i][n])
    return sublista


# función que verifica inconsistencias
def verifica_inconsistencias():
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


def is_number(string):
    try:
        number = int(string)
        return number
    except Exception as error:
        print(error)
        return None


def dates_verification(date):
    date_parts = date.split('/')
    date_number = []
    for part in date_parts:
        date_number.append(is_number(part))
    return date_number


for sale in lifestore_sales:
    print(dates_verification(sale[3]))


import datetime
correctDate = None
try:
    newDate = datetime.datetime.strptime('28/02/2020', '%d/%m/%Y')
    correctDate = True
except ValueError:
    correctDate = False
print(str(correctDate))


# función para seleccionar las ventas que tienen:
# - el id_product en el rango 1 a 96
# - su score en el rango 1 a 5
# - su refund en el rango 0 a 1
# - fechas válidas
def ventas_no_errores(ventas):
    ventas_sin_errores = []
    ventas_con_errores = []
    for venta in ventas:
        if venta[1] > 0 and venta[1] < 97:
            ventas_sin_errores.append(venta[0])
        else:
            ventas_con_errores.append([venta[0], 1])



