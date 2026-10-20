from dog import Dog
from cat import Cat
from bird import Bird
from adopter import Adopter
from adoption_center import AdoptionCenter


def line(char="-", n=60):
    print(char * n)


def main():
    center = AdoptionCenter("Second Chance Adoption Center")

    rex = Dog("Rex", 3, breed="Labrador", trained=True)
    bella = Dog("Bella", 1, breed="Beagle", trained=False)
    whiskers = Cat("Whiskers", 2, breed="Tabby", indoor_pref="Indoor")
    milo = Cat("Milo", 5, breed="Siamese", indoor_pref="Outdoor")
    kiwi = Bird("Kiwi", 1, species="Parrot", can_talk=True)

    for animal in [rex, bella, whiskers, milo, kiwi]:
        center.register_animal(animal)

    rex.get_medical_record().add_vaccination("Rabies")
    rex.get_medical_record().add_vaccination("Distemper")
    rex.get_medical_record().update_health_notes("Annual checkup passed.")
    kiwi.get_medical_record().add_vaccination("Avian flu")

    jane = Adopter("Jane Doe", "A001", "555-0100")
    mark = Adopter("Mark Lee", "A002", "555-0122")
    center.register_adopter(jane)
    center.register_adopter(mark)

    center.adopt_animal("A001", "Rex")
    center.adopt_animal("A001", "Whiskers")
    center.adopt_animal("A002", "Kiwi")

    line("=")
    print("POLYMORPHISM -- describe_all_animals()")
    line()
    for description in center.describe_all_animals():
        print(" •", description)

    line("=")
    print("EXPLICIT TYPE CHECK -- display_specific_animal_info()")
    line()
    for animal in center.get_animals():
        center.display_specific_animal_info(animal)

    line("=")
    print("BASIC ALGORITHMS")
    line()
    print(f" • calculate_average_age()        -> {center.calculate_average_age():.1f}")
    print(f" • find_animal('Bella')           -> {center.find_animal('Bella')}")
    print(f" • count_animals_by_type()        -> {center.count_animals_by_type()}")
    print(
        f" • find_animals_by_breed('Beagle')-> {center.find_animals_by_breed('Beagle')}"
    )

    line("=")
    print("ADOPTION STATISTICS -- get_adoption_statistics()")
    line()
    print(center.get_adoption_statistics())

    center.list_available_animals()

    line("=")
    print("COMPOSITION -- Rex's MedicalRecord (owned exclusively by Rex)")
    line()
    print(rex.get_medical_record())

    line("=")
    print("AGGREGATION -- Jane's adopted animals")
    line()
    jane.list_adopted_animals()

    line("=")
    print("FULL REPORT -- generate_report()")
    line()
    print(center.generate_report())
    line("=")

    line("=")
    print("POLYMORPHISM VARIANT 2 -- Method Overloading (Adopter.register)")
    line()
    print("Registering multiple animals at once:")
    jane.register(bella, milo)

    line("=")
    print("POLYMORPHISM VARIANT 3 -- Operator Overloading (Animal.__add__)")
    line()
    paired = rex + whiskers
    print(f"Using '+' operator: {paired}")
    line("=")

    line("=")
    print("FILE SAVE/LOAD -- save_to_file() and load_from_file()")
    line()
    center.save_to_file()
    center.load_from_file()

    line("=")
    print("QUEUE ADT -- Waiting List")
    line()
    center.add_to_waiting_list("A001", "Bella")
    center.add_to_waiting_list("A002", "Milo")
    center.add_to_waiting_list("A003", "Kiwi")
    center.view_waiting_list()
    print("\nProcessing next in queue:")
    center.process_waiting_list()
    line("=")


if __name__ == "__main__":
    main()
