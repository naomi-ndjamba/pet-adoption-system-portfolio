# 🐾 Pet Adoption Management System

An advanced, console and GUI-based Python application developed for an Object-Oriented Programming course. This project demonstrates the practical application of advanced OOP principles, data structures, and file handling to manage an animal shelter's daily operations. 

**Grade Achieved:** 93%

## 📌 Project Overview
The Pet Adoption Management System allows shelter staff to register animals, manage their medical histories, register potential adopters, and process adoptions. The application is built with a scalable architecture that separates the data models from the user interface, providing both a terminal-based version (`main.py`) and a full Graphical User Interface (`gui.py`).

## ✨ Key Features
*   **Advanced OOP Architecture:** Utilizes **Inheritance** (`Animal` superclass with `Dog`, `Cat`, and `Bird` subclasses), **Composition** (`Animal` owns a `MedicalRecord`), and **Aggregation** (`Adopter` collects `Animal` objects).
*   **Polymorphism (3 Variants):**
    *   *Method Overriding:* Subclasses override `make_sound()` and `get_info()`.
    *   *Method Overloading:* The `Adopter.register()` method accepts multiple arguments.
    *   *Operator Overloading:* The `__add__` method allows combining two animals into a paired record using the `+` operator.
*   **Graphical User Interface (GUI):** A fully functional desktop application built with Python's `tkinter` library, featuring menu bars, action buttons, and dialog boxes.
*   **Data Persistence:** Implements File I/O to save animal data to `shelter_data.txt` and load it back into the system upon startup.
*   **Custom Data Structures:** Uses a **Queue** (First-In-First-Out) to manage a waiting list for adopters when an animal is unavailable.
*   **Robust Exception Handling:** Extensive use of `try/except` blocks to gracefully handle missing files, invalid data formats, and invalid adoption attempts (e.g., adopting a sick animal).

## 🛠️ Tech Stack
*   **Language:** Python 3
*   **GUI Framework:** Tkinter
*   **Data Storage:** Text Files (`.txt`)

## 📂 Repository Structure
```text
pet-adoption-system/
├── src/
│   ├── animal.py            # Abstract base class
│   ├── dog.py               # Inherits from Animal
│   ├── cat.py               # Inherits from Animal
│   ├── bird.py              # Inherits from Animal
│   ├── medical_record.py    # Composed into Animal
│   ├── adopter.py           # Manages adopted animals
│   ├── adoption_center.py   # Core logic, file I/O, and Queue ADT
│   ├── main.py              # Console-based application
│   └── gui.py               # Tkinter Graphical User Interface
├── shelter_data.txt         # Generated data file
└── README.md

## 🚀 How to Run

### Prerequisites
Make sure you have Python 3 installed on your system. No external packages are required (Tkinter comes pre-installed with standard Python).

1. **Clone the repository:**
   ```bash
   git clone https://github.com/naomi-ndjamba/pet-adoption-system-portfolio.git
   cd pet-adoption-system-portfolio

2. Run the Graphical Interface (Recommended):
Navigate into the src folder and run the GUI file:
cd src
python gui.py

3. Run the Console Version:
If you want to see the terminal-based version:
cd src
python main.py
