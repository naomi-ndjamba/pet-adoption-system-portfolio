class Adopter:
    def __init__(self, name, adopter_id, phone, max_limit=3):
        self._name = name
        self._id = adopter_id
        self._phone = phone
        self._adopted_animals = []
        self._max_limit = max_limit

    def adopt_animal(self, animal):
        if self.can_adopt():
            if animal.is_adopted():
                return False
            self._adopted_animals.append(animal)
            animal.set_adopted(True)
            return True
        return False

    def return_animal(self, animal_name):
        for animal in self._adopted_animals:
            if animal.get_name() == animal_name:
                self._adopted_animals.remove(animal)
                animal.set_adopted(False)
                return True
        return False

    def list_adopted_animals(self):
        print(f"\n--- {self._name}'s Adopted Animals ---")
        if not self._adopted_animals:
            print("No animals adopted yet.")
            return
        for i, animal in enumerate(self._adopted_animals, 1):
            print(f"{i}. {animal.get_info()}")

    def get_adoption_count(self):
        return len(self._adopted_animals)

    def can_adopt(self):
        return len(self._adopted_animals) < self._max_limit

    def get_remaining_limit(self):
        return self._max_limit - len(self._adopted_animals)

    def register(self, *animals):
        if len(animals) == 0:
            print("No animals provided to register.")
            return False
        registered = 0
        for animal in animals:
            if self.adopt_animal(animal):
                registered += 1
        print(f"{self._name} registered {registered} animal(s).")
        return registered > 0

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def get_phone(self):
        return self._phone

    def get_adopted_animals(self):
        return list(self._adopted_animals)

    def get_max_limit(self):
        return self._max_limit

    def __repr__(self):
        return f"Adopter({self._name})"
