import csv


PATH_FILE: str = '/home/ss/Personal_financial_wallet/financial_wallet/data.csv'


class Balance:

    def __init__(self):
        '''Инициализируем данные баланса и записи'''
        self.current_consumption: str = self.get_balance_data('Расход')
        self.current_income: str = self.get_balance_data('Доход')
        self.current_balance: str = \
            self.current_income - self.current_consumption
        self.current_data: list[dict] = self.get_data()

    def get_data(self) -> list:
        '''Получаем список записей из файла'''
        with open(PATH_FILE, 'r', encoding='utf-8') as file:
            rows = csv.DictReader(file, delimiter=';', quotechar='"')
            return sorted(rows, key=lambda item: item['Дата'])

    def get_balance_data(self, category: str) -> int:
        '''Получаем данные баланса'''
        current_value: int = 0
        rows: list[dict] = self.get_data()
        for row in rows:
            if row['Категория'] == category:
                current_value += int(row['Сумма'])
        return current_value
