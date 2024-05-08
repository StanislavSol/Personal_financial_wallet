import csv
from datetime import datetime
from financial_wallet.balance import Balance, PATH_FILE
from financial_wallet.validator import get_valid_value


class Record(Balance):

    def request_data(self, current_date=None) -> dict:
        '''Запрашиваем данные у пользователя для записи в файл'''
        if current_date is None:
            now: datetime = datetime.now()
            current_date: str = now.strftime("%Y-%m-%d")

        category: str = get_valid_value('Категория')
        money: int = get_valid_value('Сумма')
        description: str = get_valid_value('Описание')
        data: dict = {
            'Дата': current_date,
            'Категория': category,
            'Сумма': money,
            'Описание': description,
        }

        return data

    def write_data(self):
        '''Записываем даннные в файл'''
        columns: list[str] = [
            'Дата',
            'Категория',
            'Сумма',
            'Описание'
        ]
        with open(PATH_FILE, 'w', encoding='utf-8') as file:
            writer = csv.DictWriter(
                file,
                fieldnames=columns,
                delimiter=';',
                quoting=csv.QUOTE_NONNUMERIC
            )
            writer.writeheader()
            writer.writerows(self.current_data)

    def add_record(self, data_for_record=None) -> str:
        '''Передаем данные на запись в файл'''
        if data_for_record is None:
            data_for_record: dict = self.request_data()
        self.current_data.append(data_for_record)
        self.write_data()
        return 'Данные успешно добавлены!'
