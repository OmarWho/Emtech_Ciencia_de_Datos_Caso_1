# from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
import data_preprocessing as dp

''' CLASSIFICATION:
    Section to classify the data according to distinct criteria.
    
    CLASIFICACIÓN:
    Sección dedicada a clasificar los datos de acuerdo a distintos criterios.
'''

"""
    Features of every data with which we work:
    
    - product = [id_product, name, price, category, stock]
    - sale = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
    - search = [id_search, id_product]
"""

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


def sales_without_refund(sales):
    """Function to select the sales without refund
        :param sales: list of sales
        :return sales_return: list of sales without refund
    """
    sales_return = []
    for sale in sales:
        if sale[4] == 0:
            sales_return.append(sale)
    return sales_return


def month_format(month_number):
    """Function that returns a month in the format '/mm/'
    :param month_number: number of the month (int)
    :return month_format_return: string of the month in the format '/mm/'
    """
    if month_number < 10:
        month_format_return = f'/0{month_number}/'
    else:
        month_format_return = f'/{month_number}/'
    return month_format_return


def ids_sales_products_from_month(sales, month):
    """Function to select the sales and products IDs of a given month
        :param sales: list of sales
        :param month: string of a month in the format '/mm/'
        :return id_sales_return: list of sales and products IDs of the month
    """
    ids_return = []
    for sale in sales:
        if month in sale[3]:
            ids_return.append([sale[0], sale[1]])
    return ids_return


def ids_sales_products_from_2020(sales):
    """Function to select the sales and products IDs of the year 2020
        :param sales: list of sales
        :return id_sales_return: list of sales and products IDs of the year 2020
    """
    ids_return = []
    for month_number in range(12):
        month_format_string = month_format(month_number + 1)
        id_sales_month = ids_sales_products_from_month(sales, month_format_string)
        ids_return.append(id_sales_month)
    return ids_return


def ids_elements_by_category(products, list_ids_element_product, category):
    """Function that obtains a list of products and elements (sales or searches) IDs
    of a given category
        :param products: list of the products
        :param list_ids_element_product: list of items of the form [id_element, id_product], where
        the element can be a sale or a search
        :param category: string of the category of the products
        :return ids_elements_products_by_category_return: list of items of the form
        [id_element, id_product], where the element can be a sale or a search
    """
    ids_elements_products_by_category_return = []
    for ids_element_product in list_ids_element_product:
        id_product = ids_element_product[1]
        if products[id_product - 1][3] == category:
            ids_elements_products_by_category_return.append(ids_element_product)
    return ids_elements_products_by_category_return


def num_elements_by_product(list_ids_element_product, num_products):
    """Function that obtains how many times occurs an element (sale or search) of a product
        :param list_ids_element_product: list of items of the form [id_element, id_product], where
        the element can be a sale or a search
        :param num_products: number of products (int)
        :return num_elements_by_product_return: list of items of the form
        [id_product, number of elements], where the elements can be sales or searches.
    """
    num_elements_by_product_return = [[index_product + 1, 0] for index_product in range(num_products)]
    for ids_element_product in list_ids_element_product:
        index_product = ids_element_product[1] - 1
        num_elements_by_product_return[index_product][1] += 1
    return num_elements_by_product_return


def num_elements_by_product_from_category(list_ids_element_product, products, category):
    """Function that obtains how many times occurs an element (sale or search) of a product
    according to a given category
        :param list_ids_element_product: list of items of the form [id_element, id_product], where
            the element can be a sale or a search
        :param products: list of products
        :param category: string of category
        :return num_elements_by_product_return: list of items of the form
        [id_product, number of elements], where the elements can be sales or searches.
        """
    num_products = len(products)
    num_elements_by_product_return = [[index_product + 1, 0] for index_product in range(num_products)
                                      if products[index_product][3] == category]
    for ids_element_product in list_ids_element_product:
        for index, item in enumerate(num_elements_by_product_return):
            if item[0] == ids_element_product[1]:
                num_elements_by_product_return[index][1] += 1
                break
    return num_elements_by_product_return


def sort_list(unsorted_list, order, index):
    """Function to order a list respect to a given index
        :param unsorted_list: unsorted list with elements (array{int}) that are lists
        :param order: boolean that indicates ascending (True) or descending order (False)
        :param index: index of the elements according to which the list should be sorted
        :return sorted_list: list sorted in descending order
    """
    sorted_list = sorted(unsorted_list, reverse=order, key=lambda element: element[index])
    return sorted_list


def top_n(sorted_list, n):
    """Function that returns the first n elements of a list
    :param sorted_list: sorted list of elements
    :param n: how many best elements you are looking for
    :return top_n_list: list with the top_n elements
    """
    list_size = len(sorted_list)
    top_n_list = []
    if list_size < n:
        top_n_list = sorted_list
    else:
        for i in range(n):
            top_n_list.append(sorted_list[i])
    return top_n_list


def menu_options(options):
    """Function that returns a list of the possible options that the user can enter
    :param options: list of the options
    :return options_list: string of the possible options separated whit line breaks
    """
    options_list = ''
    index = 1
    for option in options:
        if index % 2:
            vignette = '✦'
        else:
            vignette = '✧'
        options_list += f'{vignette}{index}{vignette} ' + option + '\n'
        index += 1
    return options_list


def print_table(table):
    """Function to print a table
    :param table: list of lists
    :return: None
    """
    col = len(table)
    row = len(table[0])
    table_traspose = [[] for i in range(row)]
    for j in range(col):
        for i in range(row):
            if i + 1 > len(table[j]):
                table_traspose[i].append([None])
            else:
                table_traspose[i].append(table[j][i])
    #print(table_traspose)
    cell_length = 18
    print('\n')
    for i in range(row):
        for j in range(col):
            if i == 0:
                if j > 0:
                    print('\t'*2, end="")
                length_content = len(str(table_traspose[i][j]))
                print(table_traspose[i][j], end=" "*(cell_length - length_content))
            else:
                if j > 0:
                    print('\t'*2, end="")
                length_content = len(str(table_traspose[i][j]))
                print(table_traspose[i][j], end=" " * (cell_length - length_content))
        print('\n')


def sales_incoming_by_month(sales, products, month_format):
    """Function to obtain the number of sales and the incoming of a given month.
    :param sales: list of sales
    :param products: list of products
    :param month_format: string of a month in the format '/mm/'
    :return sales_incoming_return: list of the form [num_sales, incoming]
    """
    ids_sales_products = ids_sales_products_from_month(sales, month_format)
    num_sales = len(ids_sales_products)
    sales_incoming_return = [num_sales, 0]
    for ids_sale_product in ids_sales_products:
        index_product = ids_sale_product[1] - 1
        sales_incoming_return[1] += products[index_product][2]
    return sales_incoming_return


def obtain_monthly_data(sales, products, month_format, categories):
    """Function that classify and obtain the ,monthly top_n of the data.
        :param sales: list of sales
        :param products: list of products
        :param month_format: string of a month in the format '/mm/'
        :param categories: categories of the products
        :return: None
    """
    print(f"\n\tDatos mensuales: \n")

    valid_sales = dp.ventas_no_errores(sales)
    sales_no_refund = sales_without_refund(valid_sales)
    sales_incoming = sales_incoming_by_month(sales_no_refund, products, month_format)
    print("\tVentas e ingresos (sin contar reembolsos): ", sales_incoming, '\n')

    table = []
    ids_sales_no_refund_products = ids_sales_products_from_month(sales_no_refund, month_format)
    print("\tTop 5: Productos más vendidos por categoría ([id_product, num_sales]).")
    for category in categories:
        ids_sales_no_refund_products_by_category = ids_elements_by_category(products,
                                                                  ids_sales_no_refund_products,
                                                                  category)
        # print(category, ids_sales_no_refund_products_by_category)
        num_sales_no_refund_by_product = \
            num_elements_by_product_from_category(ids_sales_no_refund_products_by_category,
                                                                     products,
                                                                     category)
        top_5_most_sold_by_category = top_n(sort_list(num_sales_no_refund_by_product, True, 1), 5)
        if top_5_most_sold_by_category[0][1] == 0:
            print(f"No hubo productos vendidos de la categoría {category} en este mes")
        else:
            column = [category]
            column.extend(top_5_most_sold_by_category)
            table.append(column)
    if len(table) > 0:
        print_table(table)
        num_products = len(products)
        num_sales_no_refund_by_product = num_elements_by_product(ids_sales_no_refund_products,
                                                                 num_products)
        top_5_most_sold = top_n(sort_list(num_sales_no_refund_by_product, True, 1), 5)
        print("\n\tTop 5: Productos más vendidos del mes \n([id_product, num_sales]).")
        for element in top_5_most_sold:
            print(element)

        table = []
        ids_sales_products = ids_sales_products_from_month(valid_sales, month_format)
        print("\n\tTop 5: Productos menos vendidos por categoría ([id_product, num_sales]).")
        for category in categories:
            ids_sales_products_by_category = ids_elements_by_category(products,
                                                                      ids_sales_products,
                                                                      category)
            # print(category, ids_sales_products_by_category)
            num_sales_by_product = \
                num_elements_by_product_from_category(ids_sales_products_by_category,
                                                      products,
                                                      category)
            top_5_least_sold_by_category = top_n(sort_list(num_sales_by_product, False, 1), 5)
            column = [category]
            column.extend(top_5_least_sold_by_category)
            table.append(column)
        if len(table) > 0:
            print_table(table)

        reviews_by_product = []
        for ids_sale_product in ids_sales_products:
            if len(reviews_by_product) > 0:
                counter = 0
                for index, item in enumerate(reviews_by_product):
                    if item[0] == ids_sale_product[1]:
                        reviews_by_product[index][1] += sales[ids_sale_product[0] - 1][2]
                        reviews_by_product[index][2] += 1
                        break
                    else:
                        counter += 1
                if counter == len(reviews_by_product):
                    review = sales[ids_sale_product[0] - 1][2]
                    reviews_by_product.append([ids_sale_product[1], review, 1])
            else:
                review = sales[ids_sale_product[0] - 1][2]
                reviews_by_product.append([ids_sale_product[1], review, 1])

        reviews_average_by_product = []
        for review_by_product in reviews_by_product:
            id_product = review_by_product[0]
            num_reviews = review_by_product[2]
            review_average = review_by_product[1] / num_reviews
            reviews_average_by_product.append([id_product, '{:0.2f}'.format(review_average),
                                               num_reviews])
        print("\n\tProductos con reseñas promedio: \n[id_product, review_average, num_reviews]")
        for element in reviews_average_by_product:
            print(element)
        top_5_best_scored = top_n(sort_list(reviews_average_by_product, True, 1), 5)
        top_5_worst_scored = top_n(sort_list(reviews_average_by_product, False, 1), 5)

        print("\n\tTop 5: Productos mejor reseñados en promedio "
              "\n([id_product, review_average, num_reviews]).")
        for element in top_5_best_scored:
            print(element)

        print("\n\tTop 5: Productos peor reseñados en promedio"
              "\n([id_product, review_average, num_reviews]).")
        for element in top_5_worst_scored:
            print(element)
    else:
        print("No hubo productos vendidos este mes.")


def obtain_2020_data(sales, searches, products, categories, monthly):
    """Function that classify and obtain the yearly top_n of the data.
    :param sales: list of sales
    :param searches: list of searches
    :param products: list of products
    :param categories: categories of the products
    :param monthly: boolean to determine whether data would be in an monthly report
    :return: None
    """
    print(f"\n\tDatos anuales:\n")

    if not monthly:
        valid_sales = dp.ventas_no_errores(sales)
        sales_no_refund = sales_without_refund(valid_sales)

        sales_incoming = [[month_number + 1] for month_number in range(12)]
        for month_number in range(12):
            sales_incoming[month_number].extend(sales_incoming_by_month(sales_no_refund, products,
                                                                        month_format(month_number+1)))

        total_sales = 0
        total_incoming = 0
        for sale_incoming in sales_incoming:
            total_sales += sale_incoming[1]
            total_incoming += sale_incoming[2]

        print("\tCantidad de ventas anual (sin contar reembolsos): ", total_sales)
        print("\tIngreso anual: ", total_incoming)

        top_5_months_most_sales = top_n(sort_list(sales_incoming, True, 1), 5)
        top_5_months_most_incoming = top_n(sort_list(sales_incoming, True, 2), 5)

        print("\n\tVentas e ingresos de cada mes (sin contar reeembolsos): "
              "\n[id_month, num_sales, incoming]")
        for element in sales_incoming:
            print(element)

        print("\n\tTop 5: Meses con mayor número de ventas: \n[id_month, num_sales, incoming]")
        for element in top_5_months_most_sales:
            print(element)

        print("\n\tTop 5: Meses con mayor número de ingresos: \n[id_month, num_sales, incoming]")
        for element in top_5_months_most_incoming:
            print(element)

        products_stock = []

        for product in products:
            products_stock.append([product[0], product[4]])

        top_10_products_in_stock = top_n(sort_list(products_stock, True, 1), 10)

        print("\n\tTop 10: Productos con mayor stock \n([id_product, stock]).")
        for element in top_10_products_in_stock:
            print(element)

        print('\n')

    num_products = len(products)

    table = []
    ids_searches_products = searches
    print("\tTop 10: Productos más buscados por categoría ([id_product, num_searches]).")
    for category in categories:
        ids_searches_products_by_category = ids_elements_by_category(products,
                                                                            ids_searches_products,
                                                                            category)
        # print(category, ids_sales_no_refund_products_by_category)
        num_searches_by_product = \
            num_elements_by_product_from_category(ids_searches_products_by_category,
                                                  products,
                                                  category)
        top_10_most_searched_by_category = top_n(sort_list(num_searches_by_product, True, 1), 10)
        if top_10_most_searched_by_category[0][1] == 0:
            print(f"No hubo productos buscados de la categoría {category} en este año")
        else:
            column = [category]
            column.extend(top_10_most_searched_by_category)
            table.append(column)

    if len(table) > 0:
        print_table(table)
        num_searches_by_product = num_elements_by_product(ids_searches_products, num_products)
        top_10_most_searched = top_n(sort_list(num_searches_by_product, True, 1), 10)
        print("\n\tTop 10: Productos más buscados del año \n([id_product, num_searches]).")
        for element in top_10_most_searched:
            print(element)
    else:
        print("No hubo productos buscados este año.")

    table = []
    print("\n\tTop 10: Productos menos buscados por categoría ([id_product, num_searches]).")
    for category in categories:
        ids_searches_products_by_category = ids_elements_by_category(products,
                                                                  ids_searches_products,
                                                                  category)
        # print(category, ids_sales_products_by_category)
        num_searches_by_product = \
            num_elements_by_product_from_category(ids_searches_products_by_category,
                                                  products,
                                                  category)
        top_10_least_searched_by_category = top_n(sort_list(num_searches_by_product, False, 1), 10)
        column = [category]
        column.extend(top_10_least_searched_by_category)
        table.append(column)
    if len(table) > 0:
        print_table(table)
        num_searches_by_product = num_elements_by_product(ids_searches_products, num_products)
        top_10_least_searched = top_n(sort_list(num_searches_by_product, False, 1), 10)
        print("\n\tTop 10: Productos menos buscados del año \n([id_product, num_searches]).")
        for element in top_10_least_searched:
            print(element)
    else:
        print("No hubo productos buscados este año.")


def obtain_monthly_report(sales, searches, products, month_format, yearly):
    """Function to print an monthly report.
    :param sales: list of sales
    :param searches: list of searches
    :param products: list of products
    :param month_format: string of a month in the format '/mm/'
    :param yearly: boolean to determine whether the report is part of the yearly report
    :return: None
    """
    num_products = len(products)
    categories = []

    for i in range(num_products):
        if products[i][3] in categories:
            continue
        else:
            categories.append(products[i][3])

    obtain_monthly_data(sales, products, month_format, categories)
    if not yearly:
        obtain_2020_data(sales, searches, products, categories, True)


def obtain_yearly_report(sales, searches, products):
    """Function to print the yearly report.
    :param sales: list of sales
    :param searches: list of searches
    :param products: list of products
    :return: None
    """
    num_products = len(products)
    categories = []

    for i in range(num_products):
        if products[i][3] in categories:
            continue
        else:
            categories.append(products[i][3])

    for month_number in range(12):
        print(f"\n\tMes: {months[month_number]}\n")
        obtain_monthly_report(sales, searches, products, month_format(month_number + 1), True)

    obtain_2020_data(sales, searches, products, categories, False)


# obtain_monthly_report(lifestore_sales, lifestore_searches, lifestore_products, '/01/', False)
# obtain_yearly_report(lifestore_sales, lifestore_searches, lifestore_products)
