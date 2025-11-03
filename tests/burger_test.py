

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from unittest.mock import Mock 

class TestBurger:
    def test_bune_default_none(self):
        burger = Burger()
        assert burger.bun == None

    def test_ingredients_default_list_empty(self):
        burger = Burger()
        assert burger.ingredients == []
     
    def test_set_buns_true(self):
        bun = Bun('Вкусная булка',100)
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun
    
    def test_add_ingredient_true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE,'секретный ингредиент',20)
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert burger.ingredients[0].type == INGREDIENT_TYPE_SAUCE
        assert burger.ingredients[0].name == 'секретный ингредиент'
        assert burger.ingredients[0].price == 20

    def test_remove_ingredient_true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE,'секретный ингредиент',20)
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    
   
    def test_move_ingredient(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE,'секретный ингредиент',20)
        ingredient1 = Ingredient(INGREDIENT_TYPE_FILLING,'секретный ингредиент1',25)
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient1)
        burger.move_ingredient(0,1)
        assert burger.ingredients[1].type == INGREDIENT_TYPE_SAUCE
        assert burger.ingredients[1].name == 'секретный ингредиент'
        assert burger.ingredients[1].price == 20

    
    def test_get_price(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100  
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 20 
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 220

    def test_get_receipt(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Вкусная булка"
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = "секретный ингредиент"
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.get_price = Mock(return_value=220)
        burger.add_ingredient(mock_ingredient)   
        assert burger.get_receipt() == '(==== Вкусная булка ====)\n= sauce секретный ингредиент =\n(==== Вкусная булка ====)\n\nPrice: 220'
