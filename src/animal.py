from abc import ABC, abstractmethod
from medical_record import MedicalRecord


class Animal(ABC):
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._health_status = "healthy"
        self._adopted = False
        self._medical_record = MedicalRecord(name)

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_health_status(self):
        return self._health_status

    def is_adopted(self):
        return self._adopted

    def set_health_status(self, status):
        if status in ["healthy", "sick"]:
            self._health_status = status
        else:
            raise ValueError(
                f"Invalid health status: {status!r}. Use 'healthy' or 'sick'."
            )

    def set_adopted(self, adopted):
        self._adopted = adopted

    def get_medical_record(self):
        return self._medical_record

    def add_vaccine(self, vaccine):
        self._medical_record.add_vaccination(vaccine)

    def __str__(self):
        return self.get_info()

    def __repr__(self):
        return f"{self.get_type()}({self._name})"

    def __add__(self, other):
        if not isinstance(other, Animal):
            return NotImplemented
        return (
            f"Paired: {self.get_name()} the {self.get_type()} + "
            f"{other.get_name()} the {other.get_type()}"
        )
