from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
 

class TestIngredient:
    def test_type_of_ingredient_true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE,'секретный ингредиент',20)
        assert ingredient.type == INGREDIENT_TYPE_SAUCE

    def test_name_of_ingredient_true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE,'секретный ингредиент',20)
        assert ingredient.name == 'секретный ингредиент'

    def test_price_of_ingredient_true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE,'секретный ингредиент',20)
        assert ingredient.price == 20

    def test_get_price_of_ingredient(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE,'секретный ингредиент',20)
        assert ingredient.get_price() == 20


    def test_get_name_of_ingredient(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE,'секретный ингредиент',20)
        assert ingredient.get_name() == 'секретный ингредиент'

    def test_get_type_of_ingredient(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE,'секретный ингредиент',20)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
