import os
from collections import defaultdict, deque
from dog import Dog
from cat import Cat
from bird import Bird


class AdoptionCenter:
    def __init__(self, name):
        self._name = name
        self._animals = []
        self._adopters = []
        self._adoption_records = []
        self._waiting_list = deque()
        self._data_file = "shelter_data.txt"

    def add_animal(self, animal):
        try:
            if animal is None:
                raise ValueError("Animal cannot be None")
            self._animals.append(animal)
            print(f"Added {animal.get_type()} '{animal.get_name()}' to {self._name}")
        except Exception as e:
            print(f"Error adding animal: {e}")

    def register_animal(self, animal):
        self.add_animal(animal)

    def remove_animal(self, animal_name):
        try:
            for animal in self._animals:
                if animal.get_name() == animal_name:
                    if animal.is_adopted():
                        raise ValueError(
                            f"Cannot remove '{animal_name}' - it is adopted!"
                        )
                    self._animals.remove(animal)
                    print(f"Removed '{animal_name}' from {self._name}")
                    return True
            raise ValueError(f"'{animal_name}' not found in the shelter")
        except ValueError as e:
            print(f"Error: {e}")
            return False

    def register_adopter(self, adopter):
        try:
            if adopter is None:
                raise ValueError("Adopter cannot be None")
            self._adopters.append(adopter)
            print(f"Registered adopter: {adopter.get_name()} (ID: {adopter.get_id()})")
        except Exception as e:
            print(f"Error registering adopter: {e}")

    def adopt_animal(self, adopter_id, animal_name):
        try:
            adopter = None
            for a in self._adopters:
                if a.get_id() == adopter_id:
                    adopter = a
                    break

            if not adopter:
                raise ValueError(f"Adopter with ID '{adopter_id}' not found")

            animal = None
            for a in self._animals:
                if a.get_name() == animal_name:
                    animal = a
                    break

            if not animal:
                raise ValueError(f"Animal '{animal_name}' not found in the shelter")

            if animal.is_adopted():
                raise ValueError(f"'{animal_name}' is already adopted")

            if animal.get_health_status() == "sick":
                raise ValueError(
                    f"Cannot adopt '{animal_name}' - it is sick. Please get it vaccinated first!"
                )

            if not adopter.can_adopt():
                raise ValueError(f"{adopter.get_name()} has reached the adoption limit")

            result = adopter.adopt_animal(animal)
            if result:
                self._adoption_records.append(
                    f"{adopter.get_name()} adopted {animal_name}"
                )
            return result

        except ValueError as e:
            print(f"Adoption failed: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error during adoption: {e}")
            return False

    def return_animal(self, adopter_id, animal_name):
        try:
            adopter = None
            for a in self._adopters:
                if a.get_id() == adopter_id:
                    adopter = a
                    break

            if not adopter:
                raise ValueError(f"Adopter with ID '{adopter_id}' not found")

            result = adopter.return_animal(animal_name)
            if not result:
                raise ValueError(
                    f"'{animal_name}' not found in {adopter.get_name()}'s adopted animals"
                )
            return result

        except ValueError as e:
            print(f"Return failed: {e}")
            return False

    def count_animals_by_type(self):
        counts = defaultdict(int)
        for animal in self._animals:
            counts[animal.get_type()] += 1
        return dict(counts)

    def find_animal(self, animal_name):
        for animal in self._animals:
            if animal.get_name() == animal_name:
                return animal
        return None

    def find_animals_by_breed(self, breed):
        results = []
        for animal in self._animals:
            if isinstance(animal, Dog) and animal.get_breed().lower() == breed.lower():
                results.append(animal)
            elif (
                isinstance(animal, Cat) and animal.get_breed().lower() == breed.lower()
            ):
                results.append(animal)
            elif (
                isinstance(animal, Bird)
                and animal.get_species().lower() == breed.lower()
            ):
                results.append(animal)
        return results

    def calculate_average_age(self):
        if not self._animals:
            return 0
        total = sum(animal.get_age() for animal in self._animals)
        return total / len(self._animals)

    def vaccinate_all_sick_animals(self):
        print("\n=== Vaccinating Sick Animals ===")
        vaccinated = 0
        for animal in self._animals:
            if animal.get_health_status() == "sick":
                animal.set_health_status("healthy")
                animal.add_vaccine("Standard Vaccine")
                vaccinated += 1
                print(f"{animal.get_name()} has been vaccinated and is now healthy!")
        if vaccinated == 0:
            print("No sick animals to vaccinate.")
        else:
            print(f"{vaccinated} animals vaccinated.")

    def list_available_animals(self):
        print(f"\n=== Available Animals in {self._name} ===")
        available = [a for a in self._animals if not a.is_adopted()]
        if not available:
            print("No animals available for adoption.")
            return
        for animal in available:
            print(f"  {animal.get_info()}")

    def list_all_animals(self):
        print(f"\n=== All Animals in {self._name} ===")
        if not self._animals:
            print("No animals in the shelter.")
            return
        for animal in self._animals:
            print(f"  {animal.get_info()}")

    def get_adoption_statistics(self):
        total = len(self._animals)
        adopted = sum(1 for a in self._animals if a.is_adopted())
        available = total - adopted
        sick = sum(1 for a in self._animals if a.get_health_status() == "sick")

        stats = {
            "total_animals": total,
            "adopted": adopted,
            "available": available,
            "sick": sick,
            "adoption_rate": f"{(adopted/total*100):.1f}%" if total > 0 else "N/A",
        }
        return stats

    def display_specific_animal_info(self, animal):
        print("\n--- Specific Animal Information ---")
        if isinstance(animal, Dog):
            print("This is a DOG")
            print(f"Breed: {animal.get_breed()}")
            print(f"Trained: {'Yes' if animal.is_trained() else 'No'}")
        elif isinstance(animal, Cat):
            print("This is a CAT")
            print(f"Breed: {animal.get_breed()}")
            print(f"Preference: {animal.get_indoor_pref()}")
        elif isinstance(animal, Bird):
            print("This is a BIRD")
            print(f"Species: {animal.get_species()}")
            print(f"Can Talk: {'Yes' if animal.can_talk() else 'No'}")
        else:
            print("Unknown animal type")
        print(f"Health: {animal.get_health_status()}")
        print(f"Adopted: {'Yes' if animal.is_adopted() else 'No'}")

    def describe_all_animals(self):
        return [animal.get_info() for animal in self._animals]

    def generate_report(self):
        lines = []
        lines.append(f"Shelter: {self._name}")
        lines.append(f"Total Animals: {len(self._animals)}")
        lines.append(f"Total Adopters: {len(self._adopters)}")

        adopted = sum(1 for a in self._animals if a.is_adopted())
        available = len(self._animals) - adopted
        lines.append(f"Adopted: {adopted}")
        lines.append(f"Available: {available}")

        lines.append("\nAnimals by Type:")
        for animal_type, count in self.count_animals_by_type().items():
            lines.append(f"  {animal_type}: {count}")

        return "\n".join(lines)

    def save_to_file(self, filename=None):
        if filename is None:
            filename = self._data_file
        try:
            with open(filename, "w") as f:
                for animal in self._animals:
                    f.write(
                        f"{animal.get_type()}|{animal.get_name()}|{animal.get_age()}|"
                        f"{animal.get_health_status()}|{animal.is_adopted()}\n"
                    )
            print(f"Data saved to {filename}")
            return True
        except IOError as e:
            print(f"Error saving file: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False

    def load_from_file(self, filename=None):
        if filename is None:
            filename = self._data_file
        try:
            if not os.path.exists(filename):
                raise FileNotFoundError(f"File {filename} not found")

            with open(filename, "r") as f:
                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) != 5:
                        raise ValueError(f"Invalid data format in line: {line}")

                    animal_type, name, age, health, adopted = parts
                    age = int(age)
                    adopted = adopted == "True"

                    if animal_type == "Dog":
                        animal = Dog(name, age, "Unknown", False)
                    elif animal_type == "Cat":
                        animal = Cat(name, age, "Unknown", "Indoor")
                    elif animal_type == "Bird":
                        animal = Bird(name, age, "Unknown", False)
                    else:
                        raise ValueError(f"Unknown animal type: {animal_type}")

                    animal.set_health_status(health)
                    animal.set_adopted(adopted)
                    self._animals.append(animal)

            print(f"Loaded {len(self._animals)} animals from {filename}")
            return True
        except FileNotFoundError as e:
            print(f"{e}")
            return False
        except ValueError as e:
            print(f"Invalid data: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False

    def add_to_waiting_list(self, adopter_id, animal_name):
        self._waiting_list.append((adopter_id, animal_name))
        print(f"Added to waiting list: {adopter_id} wants {animal_name}")
        return True

    def process_waiting_list(self):
        if not self._waiting_list:
            print("Waiting list is empty.")
            return False

        adopter_id, animal_name = self._waiting_list.popleft()
        print(f"Processing: {adopter_id} wants {animal_name}")
        return self.adopt_animal(adopter_id, animal_name)

    def view_waiting_list(self):
        print(f"\n=== Waiting List ({len(self._waiting_list)} entries) ===")
        if not self._waiting_list:
            print("No one in the waiting list.")
            return
        for i, (adopter_id, animal_name) in enumerate(self._waiting_list, 1):
            print(f"{i}. {adopter_id} waiting for {animal_name}")

    def get_name(self):
        return self._name

    def get_animals(self):
        return list(self._animals)

    def get_adopters(self):
        return list(self._adopters)
