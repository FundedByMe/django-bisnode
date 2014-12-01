from datetime import datetime, date


def bisnode_date_to_date(bisnode_date):
    if len(bisnode_date) == 6:
        bisnode_date += '01'
    try:
        formatted_datetime = datetime.strptime(bisnode_date, "%Y%m%d")
    except ValueError:
        return None
    return formatted_datetime.date()


def format_bisnode_amount(amount):
    return amount * 1000 if amount else amount


def get_node_value(parent, node_name, value_type):
    default = '' if value_type is str else None
    node = getattr(parent, node_name, None)
    node_value = getattr(node, 'value', node)
    if node_value is None:
        return default
    if value_type is date:
        return bisnode_date_to_date(node_value)
    return value_type(node_value)
