import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext

from dog import Dog
from cat import Cat
from bird import Bird
from adopter import Adopter
from adoption_center import AdoptionCenter


class PetAdoptionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pet Adoption Management System")
        self.root.geometry("900x650+100+100")

        self.center = AdoptionCenter("Second Chance Adoption Center")
        self._seed_data()

        self._build_menu()
        self._build_widgets()

    def _seed_data(self):
        rex = Dog("Rex", 3, breed="Labrador", trained=True)
        bella = Dog("Bella", 1, breed="Beagle", trained=False)
        whiskers = Cat("Whiskers", 2, breed="Tabby", indoor_pref="Indoor")
        milo = Cat("Milo", 5, breed="Siamese", indoor_pref="Outdoor")
        kiwi = Bird("Kiwi", 1, species="Parrot", can_talk=True)

        for animal in [rex, bella, whiskers, milo, kiwi]:
            self.center.register_animal(animal)

        self.center.register_adopter(Adopter("Jane Doe", "A001", "555-0100"))
        self.center.register_adopter(Adopter("Mark Lee", "A002", "555-0122"))

    def _build_menu(self):
        menubar = tk.Menu(self.root)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Save Data", command=self.save_data)
        file_menu.add_command(label="Load Data", command=self.load_data)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        animal_menu = tk.Menu(menubar, tearoff=0)
        animal_menu.add_command(label="Add Animal", command=self.add_animal)
        animal_menu.add_command(label="View All Animals", command=self.view_animals)
        animal_menu.add_command(label="Search Animal", command=self.search_animal)
        menubar.add_cascade(label="Animals", menu=animal_menu)

        adoption_menu = tk.Menu(menubar, tearoff=0)
        adoption_menu.add_command(label="Adopt Animal", command=self.adopt_animal)
        adoption_menu.add_command(label="Return Animal", command=self.return_animal)
        adoption_menu.add_command(label="View Statistics", command=self.view_statistics)
        adoption_menu.add_command(label="Waiting List", command=self.view_waiting_list)
        menubar.add_cascade(label="Adoptions", menu=adoption_menu)

        self.root.config(menu=menubar)

    def _build_widgets(self):
        title = tk.Label(
            self.root,
            text="Pet Adoption Management System",
            font=("Arial", 18, "bold"),
            pady=10,
        )
        title.pack()

        btn_frame = tk.Frame(self.root, pady=10)
        btn_frame.pack()

        tk.Button(
            btn_frame, text="View All Animals", width=20, command=self.view_animals
        ).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Add Animal", width=20, command=self.add_animal).grid(
            row=0, column=1, padx=5, pady=5
        )
        tk.Button(
            btn_frame, text="Adopt Animal", width=20, command=self.adopt_animal
        ).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(
            btn_frame, text="Search Animal", width=20, command=self.search_animal
        ).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(
            btn_frame, text="View Statistics", width=20, command=self.view_statistics
        ).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(
            btn_frame, text="Waiting List", width=20, command=self.view_waiting_list
        ).grid(row=2, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Save Data", width=20, command=self.save_data).grid(
            row=3, column=0, padx=5, pady=5
        )
        tk.Button(btn_frame, text="Load Data", width=20, command=self.load_data).grid(
            row=3, column=1, padx=5, pady=5
        )

        self.output = scrolledtext.ScrolledText(self.root, width=100, height=20)
        self.output.pack(pady=10)

    def _print(self, text):
        self.output.insert(tk.END, text + "\n")
        self.output.see(tk.END)

    def view_animals(self):
        self.output.delete(1.0, tk.END)
        self._print("=== All Animals ===")
        for animal in self.center.get_animals():
            self._print(animal.get_info())

    def add_animal(self):
        animal_type = simpledialog.askstring("Add Animal", "Type (Dog/Cat/Bird):")
        if not animal_type:
            return
        name = simpledialog.askstring("Add Animal", "Name:")
        if not name:
            return
        try:
            age = int(simpledialog.askstring("Add Animal", "Age:"))
        except (TypeError, ValueError):
            messagebox.showerror("Error", "Age must be a number")
            return

        if animal_type.lower() == "dog":
            breed = simpledialog.askstring("Add Animal", "Breed:")
            animal = Dog(name, age, breed or "Unknown", False)
        elif animal_type.lower() == "cat":
            breed = simpledialog.askstring("Add Animal", "Breed:")
            animal = Cat(name, age, breed or "Unknown", "Indoor")
        elif animal_type.lower() == "bird":
            species = simpledialog.askstring("Add Animal", "Species:")
            animal = Bird(name, age, species or "Unknown", False)
        else:
            messagebox.showerror("Error", "Unknown animal type")
            return

        self.center.register_animal(animal)
        messagebox.showinfo("Success", f"Added {animal_type} '{name}'")

    def search_animal(self):
        name = simpledialog.askstring("Search", "Enter animal name:")
        if not name:
            return
        animal = self.center.find_animal(name)
        self.output.delete(1.0, tk.END)
        if animal:
            self._print("Found:")
            self._print(animal.get_info())
        else:
            self._print(f"Animal '{name}' not found.")

    def adopt_animal(self):
        adopter_id = simpledialog.askstring("Adopt", "Adopter ID (e.g., A001):")
        if not adopter_id:
            return
        animal_name = simpledialog.askstring("Adopt", "Animal name:")
        if not animal_name:
            return
        result = self.center.adopt_animal(adopter_id, animal_name)
        self.output.delete(1.0, tk.END)
        if result:
            self._print(f"Adoption successful: {adopter_id} adopted {animal_name}")
        else:
            self._print(f"Adoption failed for {adopter_id} / {animal_name}")

    def return_animal(self):
        adopter_id = simpledialog.askstring("Return", "Adopter ID:")
        if not adopter_id:
            return
        animal_name = simpledialog.askstring("Return", "Animal name:")
        if not animal_name:
            return
        result = self.center.return_animal(adopter_id, animal_name)
        self.output.delete(1.0, tk.END)
        if result:
            self._print(f"{animal_name} returned by {adopter_id}")
        else:
            self._print("Return failed")

    def view_statistics(self):
        self.output.delete(1.0, tk.END)
        self._print("=== Adoption Statistics ===")
        stats = self.center.get_adoption_statistics()
        for key, value in stats.items():
            self._print(f"  {key}: {value}")

    def view_waiting_list(self):
        self.output.delete(1.0, tk.END)
        self._print("=== Waiting List ===")
        if not self.center._waiting_list:
            self._print("No one in the waiting list.")
            return
        for i, (adopter_id, animal_name) in enumerate(self.center._waiting_list, 1):
            self._print(f"{i}. {adopter_id} waiting for {animal_name}")

    def save_data(self):
        if self.center.save_to_file():
            messagebox.showinfo("Success", "Data saved to shelter_data.txt")
        else:
            messagebox.showerror("Error", "Could not save data")

    def load_data(self):
        if self.center.load_from_file():
            messagebox.showinfo("Success", "Data loaded from shelter_data.txt")
        else:
            messagebox.showerror("Error", "Could not load data")


if __name__ == "__main__":
    root = tk.Tk()
    app = PetAdoptionGUI(root)
    root.mainloop()
