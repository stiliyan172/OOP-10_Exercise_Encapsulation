from html import entities

from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet

class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget < price:
            return f'Not enough budget'
        if len(self.animals) == self.__animal_capacity:
            return f"Not enough space for animal"
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker_name):
        if len(self.workers) == self.__workers_capacity:
            return f'Not enough space for worker'
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker_name == worker:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
            return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        needed_money = 0
        for worker in self.workers:
            needed_money += worker.salary
        if needed_money > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= needed_money
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        needed_money = 0
        for animal in self.animals:
            needed_money += animal.money_for_care
        if needed_money > self.__budget:
            return f"You have no budget to tend the animals. They are unhappy."
        self.__budget -= needed_money
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount


    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        result += self.__build_entity_str(self.animals, 'Lion')
        result += self.__build_entity_str(self.animals, 'Tiger')
        result += self.__build_entity_str(self.animals, 'Cheetah')
        return result.strip()

    def workers_status(self):
        result = f'You have {len(self.workers)} workers\n'
        result += self.__build_entity_str(self.workers, 'Keeper')
        result += self.__build_entity_str(self.workers, 'Caretaker')
        result += self.__build_entity_str(self.workers, 'Vet')
        return result.strip()

    def __build_entity_str(self, entities, entity_type):
        counter = 0
        result = ''
        for entity in entities:
            if entity.__class__.__name__ == entity_type:
                counter += 1
                result += repr(entity) + "\n"
        return f'----- {counter} {entity_type}s:\n' + result


zoo = Zoo("Zootopia", 3000, 5, 8)
# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
# Animal prices
prices = [200, 190, 204, 156, 211, 140]
# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))
# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))
# Tending animals
print(zoo.tend_animals())
# Paying keepers
print(zoo.pay_workers())
# Fireing worker
print(zoo.fire_worker("Adam"))
# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())