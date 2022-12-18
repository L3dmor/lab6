from abc import ABC, abstractmethod


class KitchenSystem:

    def __init__(self):
        self.observers = set()

    def add(self, observer):
        self.observers.add(observer)

    def delete(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.make_dish()


class AbstractObserver(ABC):
    @abstractmethod
    def make_dish(self):
        pass


class Dish(AbstractObserver):

    def __init__(self, name):
        self.name = name

    def make_dish(self):
        print(f"Dish {self.name} is ready")


if __name__ == "__main__":
    dish1 = Dish('№1')
    dish2 = Dish('№2')
    dish3 = Dish('№3')
    dish4 = Dish('№4')
    dish_system = KitchenSystem()
    dish_system.add(dish3)
    dish_system.add(dish2)
    dish_system.add(dish1)
    dish_system.add(dish4)
    dish_system.notify()
    print(f"--------Dish {dish1.name} is served to the guest--------")
    dish_system.delete(dish1)
    dish_system.notify()
    print(f"--------Dish {dish2.name} is served to the guest--------")
    dish_system.delete(dish2)
    dish_system.notify()
    print(f"--------Dish {dish3.name} is served to the guest--------")
    dish_system.delete(dish3)
    dish_system.notify()
    print(f"--------All dishes are served--------")
    dish_system.delete(dish4)
    dish_system.notify()



