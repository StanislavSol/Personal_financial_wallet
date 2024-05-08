import csv
import prompt
from datetime import datetime


PATH_FILE = '/home/ss/Personal_financial_wallet/financial_wallet/data.csv'

class Balance:

    def __init__(self):
        self.current_consumption = self.get_balance_data('Расход')
        self.current_income = self.get_balance_data('Доход')
        self.current_balance = self.current_income - self.current_consumption
        self.current_data = self.get_data()

    def get_data(self):
        with open(PATH_FILE, 'r', encoding='utf-8') as file:
            rows = csv.DictReader(file, delimiter=';', quotechar='"')
            return sorted(rows, key=lambda item: item['Дата'])

    def get_balance_data(self, category):
        current_value = 0
        rows = self.get_data()
        for row in rows:
            if row['Категория'] == category:
                current_value += int(row['Сумма'])
        return current_value
