from praktikum.bun import Bun

class TestBun:
    def test_name_of_bun_true(self):
        bun = Bun('Вкусная булка',100)
        assert bun.name == 'Вкусная булка'

    def test_price_of_bun_true(self):
        bun = Bun('Вкусная булка',100)
        assert bun.price == 100

    def test_get_name_true(self):
        bun = Bun('Вкусная булка',100)
        assert bun.get_name() == 'Вкусная булка'
       

    def test_get_price_true(self):
        bun = Bun('Вкусная булка',100)
        assert bun.get_price() == 100
        