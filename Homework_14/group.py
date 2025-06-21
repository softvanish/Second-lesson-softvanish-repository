from group_limit_exception import GroupLimitReachedException


class Group:

    def __init__(self, number, student_limit=10):
        self.number = number
        self.group = set()
        self.student_limit = student_limit

    def add_student(self, student):
        if len(self.group) >= self.student_limit:
            raise GroupLimitReachedException(f"Group limit {self.student_limit} reached", self.number)
        self.group.add(student)

    def delete_student(self, last_name):
        for student in self.group.copy():
            if student.last_name == last_name:
                self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student) + "\n"
        return f'Number:{self.number}\n{all_students} '
