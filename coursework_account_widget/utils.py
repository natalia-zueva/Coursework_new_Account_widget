import json
from datetime import datetime
import os

def load_data(path):
    """Возвращает данные из файла json в виде списка"""
    if not os.path.exists(path):
        return []

    with open(path, "r", encoding="utf-8") as file:
        operations = json.load(file)
        return operations


def sorted_by_state(operations_data):
    """Создаем список выполненных операций"""
    sort_by_state = []
    for item in operations_data:
        if 'state' in item and item['state'] == "EXECUTED":
            sort_by_state.append(item)
    return sort_by_state


def sorted_by_date(operations_executed):
    """Сортируем выполненные операции по дате и возвращаем 5 последних операций"""
    sort_by_date = sorted(operations_executed, key=lambda x: x['date'], reverse=True)
    return sort_by_date[:5]


def format_data(sorted_list):
    """Форматируем дату и выводим необходимые данные об операции"""
    result_data = []
    for item in sorted_list:
        date = datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = item['description']
        if 'from' in item:
            sender_card = item['from'].split()
            card = sender_card.pop(-1)
            card_info = ' '.join(sender_card)
            card = f'{card[:4]} {card[4:6]}** **** {card[-4:]}'
            from_to = '->'
        else:
            card_info = 'Новый счет'
            card = ''
            from_to = ':'
        sender_bill = item['to'].split()
        bill = sender_bill.pop(-1)
        bill_info = ' '.join(sender_bill)
        bill = f'**{bill[-4:]}'
        operation_sum = item['operationAmount']['amount']
        operation_currency = item['operationAmount']['currency']['name']

        result_data.append(f"""{date} {description}
{card_info} {card} {from_to} {bill_info} {bill}
{operation_sum} {operation_currency}
""")
    return result_data

