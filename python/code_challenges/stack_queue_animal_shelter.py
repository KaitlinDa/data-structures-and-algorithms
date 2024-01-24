from data_structures.queue import Queue

class Dog:
    def __init__(self, name=""):
        self.species = "dog"
        self.name = name

class Cat:
    def __init__(self, name=""):
        self.species = "cat"
        self.name = name

class AnimalShelter:
    def __init__(self):
        self.animals = Queue()

    def enqueue(self, animal):
        if isinstance(animal, Dog) or isinstance(animal, Cat):
            self.animals.enqueue(animal)

    def dequeue(self, pref):
        if pref not in ["dog", "cat"]:
            return None

        temp_queue = Queue()
        desired_animal = None

        while not self.animals.is_empty():
            animal = self.animals.dequeue()
            if desired_animal is None and animal.species == pref:
                desired_animal = animal
                break
            temp_queue.enqueue(animal)

        while not self.animals.is_empty():
            temp_queue.enqueue(self.animals.dequeue())
        while not temp_queue.is_empty():
            self.animals.enqueue(temp_queue.dequeue())

        return desired_animal