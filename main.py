# import lists from lifestore_file.py
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
import data_preprocessing as dp
import data_classification as dc

months = [  # opciones para escoger el mes
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


def system_login():
    print("LOGIN")


def months_menu():
    # menú para el reporte mensual
    print('MENÚ PARA REPORTE MENSUAL')
    options_list = dc.menu_options(months)
    months_number_range = [f'{i + 1}' for i in range(12)]
    while True:
        print("\tVer:")
        print(options_list)
        a = f'{" " * (len(separated[1]) - 3)}'
        month = input(a + "・➣ ")
        if month in months_number_range:
            return month
        else:
            print(f"Error: {month} no es un opción válida.")
            print("Las opciones son: 1 a 12.")
            print("Reintente, por favor.\n")


''' PROGRAMA '''

# separator of the sections of the program
separated = ['⥼', '⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯', '⥽']
separator = separated[0] + separated[1] + separated[2]

''' INGRESO AL SISTEMA
    Código del inicio del programa.
'''

# start menu
flag = True
while True:
    if flag:
        print('INICIO')
        flag = False
    options = ['Ingreso  al sistema de análisis', 'Salir']
    options_list = dc.menu_options(options)
    print('\tEliga una opción:')
    print(options_list)
    a = f'{" " * (len(separated[1]) - 3)}'
    selection = input(a + '・➣ ')
    if selection == '1' or selection == '2':
        break
    else:
        print(f"Error: {selection} no es una opción válida")
        print("Las opciones son 1 a 2.")
        print("Reintente, por favor.\n")

if selection == '2':
    exit("Programa terminado.")

print(separator)


''' SISTEMA DE ANÁLISIS
    Código del sistema de análisis que fue preparado elaborar el ánalisis de los datos.
'''

# introductory message
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

tries = 3

while True:
    if tries > 0:
        user = input("\tIngrese su usuario: ")
        password = input("\tIngrese su contraseña: ")
        if user in dp.sublista(accounts, 0):
            if [user, password] in accounts:
                print("\n\tIngreso al sistema exitoso!\n")
                break
            else:
                tries -= 1
                print("\nLa contraseña es incorrecta.")
                if tries > 0:
                    print("Por favor, reintente, tiene {} intentos restantes\n".format(tries))
        else:
            tries -= 1
            print("\nEl usuario es incorrecto.")
            if tries > 0:
                print("Por favor, reintente, tiene {} intentos restantes\n".format(tries))
    else:
        print("\n\tLas credenciales no son correctas, ya no tiene más intentos, lo sentimos.\n"
              "\tVuelva más tarde.")
        exit()

print(separator)

# menú principal
options = ['Reporte mensual', 'Reporte anual']      # opciones para presentar el reporte
selection = 0
print('MENÚ PRINCIPAL')
options_list = dc.menu_options(options)
while True:
    print('\tVer:')
    print(options_list)
    a = f'{" " * (len(separated[1]) - 3)}'
    selection = input(a + '・➣ ')
    if selection == '1' or selection == '2':
        break
    else:
        print(f"Error: {selection} no es una opción válida")
        print("Las opciones son 1 a 2.")
        print("Reintente, por favor.\n")

print(separator)


if selection == '1':

    month = months_menu()
    month_name = months[int(month) - 1]
    month_format = dc.month_format(int(month))

    print(month_format, month_name)

    print(f"\n\tReporte mensual: {month_name}/2020\n")
    dc.obtain_monthly_report(lifestore_sales, lifestore_searches, lifestore_products,
                             month_format, False)

else:
    print("\n\tReporte anual:\n")
    dc.obtain_yearly_report(lifestore_sales, lifestore_searches, lifestore_products)
