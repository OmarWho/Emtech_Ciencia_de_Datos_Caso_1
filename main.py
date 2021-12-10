# importa listas desde lifestore_file.py
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
import sys
# import numpy as np

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


def verifica_inconsistencias():
    mensaje_de_error = '''
        Existen  inconsistencias en los datos proporcionados.
        Datos enviados para revisión.
        '''

    # verifica si existen identificadores o nombres de productos repetidos.
    if len(set(sublista(lifestore_products, 0))) != len(lifestore_products) or \
            len(set(sublista(lifestore_products, 1))) != len(lifestore_products):
        sys.exit(mensaje_de_error)

    # verifica si existen identificadores de ventas repetidos
    if len(set(sublista(lifestore_sales, 0))) != len(lifestore_sales):
        sys.exit(mensaje_de_error)

    # verifica si existen identificadores de búsquedas repetidos
    if len(set(sublista(lifestore_searches, 0))) != len(lifestore_searches):
        sys.exit(mensaje_de_error)

    # verifica si las reseñas de los productos se encuentran en el rango válido de 1 a 5
    for score in set(sublista(lifestore_sales, 2)):
        if score in {1, 2, 3, 4, 5}:
            continue
        else:
            sys.exit(mensaje_de_error)

    # verifica si los valores que toma la variable refund sólo se encuentra en el rango de 0 a 1
    for refund in set(sublista(lifestore_sales, 4)):
        if refund in {0, 1}:
            continue
        else:
            sys.exit(mensaje_de_error)

    productos_id = sublista(lifestore_products, 0)

    # verifica si las id_product de las ventas corresponden a un producto existente.
    for sale in lifestore_sales:
        if sale[1] in productos_id:
            continue
        else:
            sys.exit(mensaje_de_error)

    # verifica si las id_product de las búsquedas corresponden a un producto existente.
    for search in lifestore_searches:
        if search[1] in productos_id:
            continue
        else:
            sys.exit(mensaje_de_error)


''' SISTEMA DE ANÁLISIS
    Código del sistema de análisis que fue preparado elaborar el ánalisis de los datos.
'''

# sistema de análisis

num_products = len(lifestore_products)      # obtiene el número de productos
num_sales = len(lifestore_sales)            # obtiene el número de ventas
num_searches = len(lifestore_searches)      # obtiene el número de búsquedas

# separador de secciones del sistema de análisis
separated = ['⥼', '⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯', '⥽']
separator = separated[0] + separated[1] + separated[2]

# mensaje de introducción
introduction = """\nSISTEMA DE ANÁLISIS:
    Sistema diseñado para mostrar reportes mensuales y\o 
    anuales de los productos más vendidos, menos vendidos, 
    más buscados, menos buscados, mejor reseñados, peor reseñados, 
    los ingresos y la cantidad de ventas.
    """


print(introduction)
print(separator)

accounts = [['omar100', 'LOL'], ['emtech', '1234']]             # lista con las cuentas registradas

# sección de ingreso al sistema
print("INGRESO AL SISTEMA")

# bucle para validar las credenciales
while True:
    user = input("\tIngrese su usuario: ")
    password = input("\tIngrese su contraseña: ")
    if [user, password] not in accounts:
        print("\n\tEl usuario o la contraseña no son válidos, por favor, reintente.\n")
    else:
        break
print(separator)


options = ['Reporte mensual', 'Reporte anual']      # opciones para presentar el reporte

selection = 0

# menú principal
print('MENÚ PRINCIPAL')
options_list = ''
index = 1
for option in options:
    if index % 2:
        vignette = '✦'
    else:
        vignette = '✧'
    options_list += f'{vignette}{index}{vignette} ' + option + '\n'
    index += 1
while True:
    print('\tVer:')
    print(options_list)
    a = f'{" " * (len(separated[1]) - 3)}'
    enter_data = input(a + '・➣ ')
    try:
        selection = int(enter_data)
        if selection < 1 or selection > 2:
            print("El número no corresponde a ningúna opción indicada.")
            print("Las opciones son \'1\' y \'2\'.")
            print("Reintente, por favor.\n")
        else:
            break
    except Exception as error:
        print("Error: {}".format(error))
        print("Las opciones son \'1\' y \'2\'.")
        print("Reintente, por favor.\n")

print(separator)

# opciones para escoger el mes
months = [
    'Enero',
    'Febrero',
    'Marzo',
    'Abril',
    'Mayo',
    'Junio',
    'Julio',
    'Agosto',
    'Septiembre',
    'Octubre',
    'Noviembre',
    'Diciembre'
]

# menú para el reporte mensual
print('MENÚ PARA REPORTE MENSUAL')
options_list = ''
index = 1
for month in months:
    if index % 2:
        vignette = '✦'
    else:
        vignette = '✧'
    options_list += f'{vignette}{index}{vignette} ' + month + '\n'
    index += 1

flag = 0
year = 0
month = 0
while True:
    if flag == 0:
        print("\tAños disponibles: 2020")
        a = f'{" " * (len(separated[1]) - 20)}'
        enter_data = input(a + "Ingrese el año: ")
        try:
            year = int(enter_data)
            if year == 2020:
                flag += 1
            else:
                print("El año seleccionado no se encuentra en el registro.")
                print("Los años disponibles son: 2020")
                print("Reintente, por favor.\n")
        except Exception as error:
            print("Error: {}".format(error))
            print("Los años disponibles son: 2020")
            print("Reintente, por favor.\n")
    if flag == 1:
        print("\tVer:")
        print(options_list)
        a = f'{" " * (len(separated[1]) - 3)}'
        enter_data = input(a + "・➣ ")
        try:
            month = int(enter_data)
            if month < 1 or month > 12:
                print("El número ingresado no corresponde a ningún mes.")
                print("Las opciones son: 1-12.")
                print("Reintente, por favor.\n")
            else:
                break
        except Exception as error:
            print("Error: {}".format(error))
            print("Las opciones son: 1-12.")
            print("Reintente, por favor.\n")

print(year)
print(month)

print(separator)


def top_n_most(dictionary, n):
    top_n_most_list = []
    auxiliar_set = set(dictionary.values())
    for i in range(n):
        if len(auxiliar_set) > 0:
            maximum_element = max(auxiliar_set)
            auxiliar_set.remove(maximum_element)
            if len(top_n_most_list) < n:
                for product in dictionary.keys():
                    if len(top_n_most_list) < n:
                        if dictionary[product] == maximum_element:
                            top_n_most_list.append([product, maximum_element])
                            # print([product, maximum_element])
                    else:
                        break
            else:
                break
    return top_n_most_list


def top_n_least_by_category(dictionary, n, list, category):
    top_n_least_by_category_list = []
    auxiliar_set = set(dictionary.values())
    for i in range(n):
        if len(auxiliar_set) > 0:
            minimum_element = min(auxiliar_set)
            auxiliar_set.remove(minimum_element)
            if len(top_n_least_by_category_list) < n:
                for product in dictionary.keys():
                    if len(top_n_least_by_category_list) < n:
                        if dictionary[product] == minimum_element and list[product - 1][3] == category:
                            top_n_least_by_category_list.append([product, minimum_element])
                            # print([product, maximum_element])
                    else:
                        break
            else:
                break
    return top_n_least_by_category_list


months_num = [f'/0{i + 1}/' if i < 9 else f'/{i + 1}/' for i in range(12)]
# print(months)

month = months_num[0]

flag_sales_month = True
sales_by_month = []

for i in range(num_sales):
    if month in lifestore_sales[i][3]:
        sales_by_month.append(lifestore_sales[i])

print(sales_by_month)

sales_by_product_and_month = dict()

if len(sales_by_month) > 0:
    for i in range(num_products):
        sales_by_product_and_month[lifestore_products[i][0]] = 0

    for i in range(len(sales_by_month)):
        if lifestore_sales[i][4] == 0:
            sales_by_product_and_month[lifestore_sales[i][1]] += 1
else:
    flag_sales_month = False

print(sales_by_product_and_month)

top_5_most_sold = top_n_most(sales_by_product_and_month, 5)

print(top_5_most_sold)


flag_searches = True
searches_by_product = dict()

if len(lifestore_searches) > 0:
    for i in range(num_searches):
        if lifestore_searches[i][1] in searches_by_product.keys():
            searches_by_product[lifestore_searches[i][1]] += 1
        else:
            searches_by_product[lifestore_searches[i][1]] = 1
else:
    flag_searches = False

print(searches_by_product)

top_10_most_searched = top_n_most(searches_by_product, 10)

print(top_10_most_searched)


categories = []

for i in range(num_products):
    if lifestore_products[i][3] in categories:
        continue
    else:
        categories.append(lifestore_products[i][3])

print(categories)

num_categories = len(categories)

top_5_least_sold_by_category = []

for category in categories:
    top_5_least_sold = top_n_least_by_category(sales_by_product_and_month, 5, lifestore_products, category)
    top_5_least_sold_by_category.append([category, top_5_least_sold])

print(top_5_least_sold_by_category)

top_10_least_searched_by_category = []

for category in categories:
    top_10_least_searched = top_n_least_by_category(searches_by_product, 10, lifestore_products, category)
    top_10_least_searched_by_category.append([category, top_10_least_searched])

print(top_10_least_searched_by_category)




top_5_best_score = []

auxiliar_set = set(sublista(sales_by_month, 2))
for i in range(5):
    if len(auxiliar_set) > 0:
        maximum_element = max(auxiliar_set)
        auxiliar_set.remove(maximum_element)
        if len(top_5_best_score) < 5:
            for i in range(len(sales_by_month)):
                if len(top_5_best_score) < 5:
                    if sales_by_month[i][2] == maximum_element and [sales_by_month[i][1], maximum_element] not in top_5_best_score:
                        top_5_best_score.append([sales_by_month[i][1], maximum_element])
                        # print([product, maximum_element])
                else:
                    break
        else:
            break

print(top_5_best_score)

top_5_worst_score = []

auxiliar_set = set(sublista(sales_by_month, 2))
for i in range(5):
    if len(auxiliar_set) > 0:
        minimum_element = min(auxiliar_set)
        auxiliar_set.remove(minimum_element)
        if len(top_5_worst_score) < 5:
            for i in range(len(sales_by_month)):
                if len(top_5_worst_score) < 5:
                    if sales_by_month[i][2] == minimum_element: #and [sales_by_month[i][1], minimum_element] not in top_5_worst_score:
                        top_5_worst_score.append([sales_by_month[i][1], minimum_element])
                        # print([product, maximum_element])
                else:
                    break
        else:
            break

print(top_5_worst_score)

total_incoming_by_month = [0 for i in range(12)]
total_sales_by_month = [0 for i in range(12)]

for j in range(12):
    month = months_num[j]
    sales_by_month = []
    for i in range(num_sales):
        if month in lifestore_sales[i][3]:
            sales_by_month.append(lifestore_sales[i])

    for sale in sales_by_month:
        if sale[4] == 0:
            total_incoming_by_month[j] += lifestore_products[sale[1]-1][2]
            total_sales_by_month[j] += 1


print(total_incoming_by_month)
print(total_sales_by_month)

print(sum(total_incoming_by_month))





