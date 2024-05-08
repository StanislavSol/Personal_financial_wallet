from personal_financial.balance import Balance


def test_balance():
    assert Balance().current_balance == 148636
    assert Balance().current_income == 190400
    assert Balance()current_consumption == 41764
    assert len(Balance().self.current_data) == 19
