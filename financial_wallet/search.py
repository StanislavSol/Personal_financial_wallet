from financial_wallet.balance import Balance
from financial_wallet.validator import get_valid_value


class SearchByValue(Balance):

    def get_records_by_value(self):
        field = get_valid_value('Поиск')
        recording = get_valid_value(field)
        records = list(filter(lambda item: item[field] == recording, self.current_data))
        if records:
            result = ''
            for item in records:
                row = f"Дата: {item['Дата']}\nКатегория: {item['Категория']}\nСумма: {item['Сумма']}\nОписание: {item['Описание']}\n\n"
                result += row

            return '\n{result}'

        return 'По указанным записям ничего не найдено!'
