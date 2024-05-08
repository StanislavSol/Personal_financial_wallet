import prompt
from re import fullmatch


DANGER = 'Неверный формат!'
DATE_PATTERN = '\d{4}-\d{2}-\d{2}'


def is_valid(value, field):
    conditions = {
        'Дата': fullmatch(DATE_PATTERN, value) is None,
        'Категория': value not in ('Доход', 'Расход'),
        'Сумма': not value.isdigit(),
        'Описание': False,
        'Поиск': value not in ('Дата', 'Категория', 'Сумма'),
    }
    return conditions[field]


def get_valid_value(field):
    messages = {
        'Дата': 'Укажите дату(в формате "%Y-%m-%d"): ',
        'Категория': 'Укажите категорию из списка -> (Доход, Расход): ',
        'Сумма': 'Укажите сумму (Введите числовое значение): ',
        'Описание': 'Добавьте описание: ',
        'Поиск': 'Укажите поле для поиска(Дата/Категория/Сумма): ',
    }

    value = prompt.string(messages[field]).capitalize()
    condition = is_valid(value, field)

    while condition:
        value = prompt.string(f'{DANGER} {messages[field]}').capitalize()
        condition = is_valid(value, field)

    return value
