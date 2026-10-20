from animal import Animal


class Bird(Animal):
    def __init__(self, name, age, species, can_talk=False):
        super().__init__(name, age)
        self._species = species
        self._can_talk = can_talk

    def get_species(self):
        return self._species

    def can_talk(self):
        return self._can_talk

    def get_type(self):
        return "Bird"

    def make_sound(self):
        return "Tweet!" if not self._can_talk else "Hello there!"

    def get_info(self):
        status = "Adopted" if self.is_adopted() else "Available"
        talk_str = "can talk" if self._can_talk else "cannot talk"
        return (
            f"Bird {self._name} - {self._species}, age {self._age}, {talk_str} - "
            f"{status} - says '{self.make_sound()}'"
        )
