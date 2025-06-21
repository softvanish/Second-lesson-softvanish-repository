from human import Human


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)

        self.record_book = record_book

    def __str__(self):
        person_info = super().__str__()
        return f"{person_info}, {self.record_book}"

    def __hash__(self):
        return hash(str(self))
