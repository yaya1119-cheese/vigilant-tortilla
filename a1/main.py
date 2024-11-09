
class Food:
    def __init__(self, name, calories):
        self.name = name            
        self.calories = calories    

    def get_calories(self):
        return self.calories

    def set_calories(self, calories):
        self.calories = calories

    
    
   
        

class Pizza(Food):


    def get_calories(self):
        return f"{self.name} has {self.calories} calories."


class Burger(Food):


 
    def get_calories(self):
        return f"{self.name} has {self.calories} calories."



pepperoni_pizza = Pizza("Pizza", 285)
cheeseburger = Burger("Cheeseburger", 750)


print(pepperoni_pizza.get_calories()) 
print(cheeseburger.get_calories())   
