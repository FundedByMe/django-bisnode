from datetime import datetime


def bisnode_date_to_date(bisnode_date):
    if len(bisnode_date) == 6:
        bisnode_date += '01'
    formatted_datetime = datetime.strptime(bisnode_date, "%Y%m%d")
    return formatted_datetime.date()


def k_number_to_number(number):
    return number * 1000
