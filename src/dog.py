from animal import Animal


class Dog(Animal):
    def __init__(self, name, age, breed, trained=False):
        super().__init__(name, age)
        self._breed = breed
        self._trained = trained

    def get_breed(self):
        return self._breed

    def is_trained(self):
        return self._trained

    def get_type(self):
        return "Dog"

    def make_sound(self):
        return "Woof!"

    def get_info(self):
        status = "Adopted" if self.is_adopted() else "Available"
        trained_str = "trained" if self._trained else "untrained"
        return (
            f"Dog {self._name} - {self._breed}, age {self._age}, {trained_str} - "
            f"{status} - says '{self.make_sound()}'"
        )
