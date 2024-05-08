import prompt
from re import fullmatch


DANGER: str = 'Неверный формат!'


def is_valid(value: str, field: str) -> str:
    '''Получаем резултат условия по запросу'''
    conditions: dict = {
        'Дата': fullmatch(r'\d{4}-\d{2}-\d{2}', value) is None,
        'Категория': value not in ('Доход', 'Расход'),
        'Сумма': not value.isdigit(),
        'Описание': False,
        'Поиск': value not in ('Дата', 'Категория', 'Сумма'),
    }
    return conditions[field]


def get_valid_value(field: str) -> str:
    '''Получаем валидное значение у пользователя'''
    messages: dict = {
        'Дата': 'Укажите дату(в формате "%Y-%m-%d"): ',
        'Категория': 'Укажите категорию из списка -> (Доход, Расход): ',
        'Сумма': 'Укажите сумму (Введите числовое значение): ',
        'Описание': 'Добавьте описание: ',
        'Поиск': 'Укажите поле для поиска(Дата/Категория/Сумма): ',
    }

    value: str = prompt.string(messages[field]).capitalize()
    condition: bool = is_valid(value, field)

    while condition:
        value: str = prompt.string(f'{DANGER} {messages[field]}').capitalize()
        condition: bool = is_valid(value, field)

    return value
