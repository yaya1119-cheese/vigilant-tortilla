
class Food:
    def __init__(self, name, calories):
        self._name = name            
        self._calories = calories    

    def get_calories(self):
        return f"{self._name} has {self._calories} calories."


class Pizza(Food):


    def get_calories(self):
        return f"{self._name} has {self._calories} calories."


class Burger(Food):


 
    def get_calories(self):
        return f"{self._name} has {self._calories} calories."



pepperoni_pizza = Pizza("Pizza", 285)
cheeseburger = Burger("Cheeseburger", 750)


print(pepperoni_pizza.get_calories()) 
print(cheeseburger.get_calories())   