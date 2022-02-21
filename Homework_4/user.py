from human import Human
from datetime import datetime


class User(Human):
    def __init__(self, first_name, last_name, birth_date):
        super().__init__(first_name, last_name, birth_date)
        self._age = None

    @property
    def age(self):
        if self._age:
            return self._age
        year_of_birth = int(self.birth_date.year)
        current_year = datetime.datetime.now().year
        return current_year - year_of_birth
