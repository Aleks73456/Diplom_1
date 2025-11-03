from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.database import Database
import pytest

class TestDatabase:

    def test_database_bun_default_list(self):
        database = Database()
        assert isinstance(database.buns, list)

    def test_database_ingredients_default_list(self):
        database = Database()
        assert isinstance(database.ingredients, list)

    
    @pytest.mark.parametrize(
    'name,price',            
    [
        ["black bun", 100],   
        ["white bun", 200],  
        ["red bun", 300]
    ]
)
    def test_available_buns(self,name,price):
        database = Database()
        bun = Bun(name, price)
        database.buns.append(bun)
        assert bun in database.available_buns()
        
    
    ingredients = [
        [INGREDIENT_TYPE_SAUCE, "hot sauce", 100],   
        [INGREDIENT_TYPE_SAUCE, "sour cream", 200],  
        [INGREDIENT_TYPE_SAUCE, "chili sauce", 300],
        [INGREDIENT_TYPE_FILLING, "cutlet", 100],
        [INGREDIENT_TYPE_FILLING, "dinosaur", 200],
        [INGREDIENT_TYPE_FILLING, "sausage", 300]
    ]
    
    @pytest.mark.parametrize('type,name,price',ingredients)
    def test_available_ingridenets(self,type,name,price):
        database = Database()
        ing = Ingredient(type,name,price)
        database.ingredients.append(ing)
        assert ing in database.available_ingredients()

    