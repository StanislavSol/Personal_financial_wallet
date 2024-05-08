from financial_wallet.balance import Balance
from financial_wallet.record import Record
from financial_wallet.change import ChangeRecord
from financial_wallet.search import SearchByValue


def command_handler(command: str = 'balance'):
    balance_display_commands: dict = {
        'balance': Balance().current_balance,
        'income': Balance().current_income,
        'consumption': Balance().current_consumption,
    }
    actions_with_the_wallet: dict = {
        'add_entry': Record().add_record,
        'change_entry': ChangeRecord().change_data,
        'delete_entry': ChangeRecord().delete_data,
        'find_entry': SearchByValue().get_records_by_value,
    }

    if command in balance_display_commands:
        return balance_display_commands[command]

    return actions_with_the_wallet[command]()
