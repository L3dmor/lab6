from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def person_method():
        pass


class Supervisor(Person):
    def __init__(self):
        self.name = "Basic Supervisor Name"

    def person_method(self):
        print("I am a supervisor")


class Merchandiser(Person):
    def __init__(self):
        self.name = "Basic Merchandiser Name"

    def person_method(self):
        print("I am a merchandiser")


class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == "Supervisor":
            return Supervisor()
        if person_type == "Merchandiser":
            return Merchandiser()
        print("Invalid Type")
        return -1

if __name__ == "__main__":
    person = PersonFactory.build_person("Supervisor")
    person.person_method()
    person = PersonFactory.build_person("Merchandiser")
    person.person_method()
