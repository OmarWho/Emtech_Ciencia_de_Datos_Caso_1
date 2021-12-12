from lifestore_file import lifestore_products, lifestore_sales

"""
    Features of every data with which we work:
    
    - product = [id_product, name, price, category, stock]
    - sale = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
    - search = [id_search, id_product]
"""


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


def id_sales_from_month(sales, month):
    """Function to select the sales IDs of a given month
        :param sales: list of sales
        :param month: string of a month in the format '/mm/'
        :return id_sales_return: list of sales IDs of the month
    """
    id_sales_return = []
    for sale in sales:
        if month in sale[3]:
            id_sales_return.append(sale[0])
    return id_sales_return


def id_sales_from_2020(sales):
    """Function to select the sales IDs of the year 2020
        :param sales: list of sales
        :return id_sales_return: list of sales IDs of the year 2020
    """
    id_sales_return = []
    for month_number in range(12):
        month_format_string = month_format(month_number + 1)
        id_sales_month = id_sales_from_month(sales, month_format_string)
        id_sales_return.append(id_sales_month)
    return id_sales_return


ventas_validas = sales_without_refund(lifestore_sales)
print(id_sales_from_2020(ventas_validas))
for month_num in range(12):
    sales_month = id_sales_from_month(ventas_validas, month_format(month_num + 1))
    print(len(sales_month), sales_month)


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
    size_list = len(sorted_list)
    top_n_list = []
    if size_list < n:
        top_n_list = sorted_list
    else:
        for i in range(n):
            top_n_list.append(sorted_list[i])
    return top_n_list








