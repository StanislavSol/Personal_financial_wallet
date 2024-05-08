from financial_wallet.balance import Balance
from financial_wallet.validator import get_valid_value


class SearchByValue(Balance):

    def get_records_by_value(self) -> str:
        '''Запрашиваем данные у пользователя
        для поиска в файле, выводим результат'''
        field: str = get_valid_value('Поиск')
        recording = get_valid_value(field)
        records: list[dict] = list(
            filter(
                lambda item: item[field] == recording,
                self.current_data
            )
        )
        if records:
            result: str = ''
            for item in records:
                row: str = f"Дата: {item['Дата']}\n"\
                        f"Категория: {item['Категория']}\n"\
                        f"Сумма: {item['Сумма']}\n"\
                        f"Описание: {item['Описание']}\n\n"
                result += row

            return f'\n{result}'

        return 'По указанным записям ничего не найдено!'
