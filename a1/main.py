class Food:
    def calories(self):
        print("Calories for different foods")
    
class Pizza(Food):
    def calories(self):
        print("285")

class Barbacue_Bacon_Burger(Food):
    def calories(self):


        super().calories()
        print("750")