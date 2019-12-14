"""A module that represents the valid food types."""

# The set of valid food items
FOODS = {'beef', 'pork', 'chicken', 'onion', 'pepper', 'tomato'}

# The set vegetables
VEGGIES = {'onion', "pepper", 'tomato'}

# The calories for each food item (a dictionary, where
# key = food name (string) and value = calories (int)
CALORIES = {
    'beef': 200,
    'chicken': 140,
    'pork': 100,
    'onion': 30,
    'pepper': 25,
    'tomato': 10,
}

# Implement Food class here
class Food:
    _slots_ = ['name', 'vegetable', 'calories']
    def _init_(self, name, vegetable, calories):
        self.name = name
        self.vegetable = vegetable
        self.calories = calories
    def _str_(self):
        print("This food is a " + self.name)

def main():
    Food()
if __name__ == "__main__":
    main()
