from financial_wallet.record import Record
from financial_wallet.validator import get_valid_value
import prompt


class ChangeRecord(Record):

    def request_data_for_chainges(self):
        request_date = get_valid_value('Дата')
        data_for_changes = self.request_data(request_date)
        if data_for_changes in self.current_data:
            return data_for_changes

    def delete_data(self):
        data = self.request_data_for_chainges()
        if data:
            self.current_data.remove(data)
            self.write_data()

        return 'Данные успешно удалены.'

    def change_data(self):
        data = self.request_data_for_chainges()
        if data:
            date_from_data = data['Дата']
            self.current_data.remove(data)
            request_new_date = self.request_data(date_from_data)
            add_new_data = self.add_record(request_new_date)

            return 'Данные успешно изменены.'

        return 'По указанным данным ничего не найдено!'
