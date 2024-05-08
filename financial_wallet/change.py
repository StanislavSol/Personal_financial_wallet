from financial_wallet.record import Record
from financial_wallet.validator import get_valid_value


class ChangeRecord(Record):

    def request_data_for_chainges(self) -> dict:
        '''Получаем данные для изменения'''
        request_date: str = get_valid_value('Дата')
        data_for_changes: dict = self.request_data(request_date)
        if data_for_changes in self.current_data:
            return data_for_changes

    def delete_data(self) -> str:
        '''Удаляем даннные'''
        data: dict = self.request_data_for_chainges()
        if data:
            self.current_data.remove(data)
            self.write_data()

        return 'Данные успешно удалены.'

    def change_data(self) -> str:
        '''Изменяем данные'''
        data: dict = self.request_data_for_chainges()
        if data:
            date_from_data: str = data['Дата']
            self.current_data.remove(data)
            request_new_data: dict = self.request_data(date_from_data)
            self.add_record(request_new_data)

            return 'Данные успешно изменены.'

        return 'По указанным данным ничего не найдено!'
