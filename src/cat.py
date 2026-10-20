from animal import Animal


class Cat(Animal):
    def __init__(self, name, age, breed, indoor_pref="Indoor"):
        super().__init__(name, age)
        self._breed = breed
        self._indoor_pref = indoor_pref

    def get_breed(self):
        return self._breed

    def get_indoor_pref(self):
        return self._indoor_pref

    def get_type(self):
        return "Cat"

    def make_sound(self):
        return "Meow!"

    def get_info(self):
        status = "Adopted" if self.is_adopted() else "Available"
        return (
            f"Cat {self._name} - {self._breed}, age {self._age}, prefers {self._indoor_pref} - "
            f"{status} - says '{self.make_sound()}'"
        )
