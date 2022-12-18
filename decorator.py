from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def get_structure(self):
        pass

    @abstractmethod
    def get_calories(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


class Dish(Food):

    def get_structure(self):
        return 'Potato'

    def get_calories(self):
        return 120

    def get_cost(self):
        return 45


class Decorator(Food):
    def __init__(self, decorated_dish):
        self.decorated_dish = decorated_dish

    def get_structure(self):
        self.decorated_dish.get_structure()

    def get_calories(self):
        self.decorated_dish.get_calories()

    def get_cost(self):
        self.decorated_dish.get_cost()


class Cutlet(Decorator):

    def __init__(self, decorated_dish):
        Decorator.__init__(self, decorated_dish)

    def get_structure(self):
        return self.decorated_dish.get_structure() + ' with cutlet'

    def get_calories(self):
        return self.decorated_dish.get_calories() + 210

    def get_cost(self):
        return self.decorated_dish.get_cost() + 120


class Compote(Decorator):

    def __init__(self, decorated_dish):
        Decorator.__init__(self, decorated_dish)

    def get_structure(self):
        return self.decorated_dish.get_structure() + ' and compote'

    def get_calories(self):
        return self.decorated_dish.get_calories() + 30

    def get_cost(self):
        return self.decorated_dish.get_cost() + 15


dish1 = Dish()
print('Structure: ' + dish1.get_structure() +
      '; Calories: ' + str(dish1.get_calories()) + '; Cost: ' + str(dish1.get_cost()))
dish2 = Cutlet(dish1)
print('Structure: ' + dish2.get_structure() +
      '; Calories: ' + str(dish2.get_calories()) + '; Cost: ' + str(dish2.get_cost()))
dish3 = Compote(dish2)
print('Structure: ' + dish3.get_structure() +
      '; Calories: ' + str(dish3.get_calories()) + '; Cost: ' + str(dish3.get_cost()))
