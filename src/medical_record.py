from datetime import date


class MedicalRecord:
    def __init__(self, animal_name: str):
        self._record_id = f"MR_{animal_name}_{id(self)}"
        self._date_created = date.today().isoformat()
        self._vaccinations = []
        self._health_notes = ""
        self._last_checkup = date.today().isoformat()

    def get_record_id(self) -> str:
        return self._record_id

    def get_date_created(self) -> str:
        return self._date_created

    def get_vaccinations(self):
        return list(self._vaccinations)

    def get_health_notes(self) -> str:
        return self._health_notes

    def get_last_checkup(self) -> str:
        return self._last_checkup

    def add_vaccination(self, vaccine: str) -> bool:
        if vaccine in self._vaccinations:
            return False
        self._vaccinations.append(vaccine)
        return True

    def update_health_notes(self, notes: str) -> None:
        self._health_notes += f"\n- {notes}"

    def update_last_checkup(self, checkup_date: str) -> None:
        self._last_checkup = checkup_date

    def get_info(self) -> str:
        vaccination_list = (
            ", ".join(self._vaccinations) if self._vaccinations else "No vaccinations"
        )
        lines = [
            f"Medical Record: {self._record_id}",
            f"Created: {self._date_created}",
            f"Last Checkup: {self._last_checkup}",
            f"Vaccinations: {vaccination_list}",
            f"Health Notes: {self._health_notes.strip() if self._health_notes else 'None'}",
        ]
        return "\n".join(lines)

    def __str__(self) -> str:
        return self.get_info()
