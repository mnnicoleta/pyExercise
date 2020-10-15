class Student(object):

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        class_name = type(self).__name__
        return '{} ({} {} - {}) [{}]'.format(class_name, self.first_name, self.last_name, self.age, id(self)
                                             )

    def __str__(self):
        return '{} {}, {}'.format(self.first_name, self.last_name, self.age)


anthony = Student('Anthony', 'Hopkins', 21)
print(repr(anthony))
print(str(anthony))


class SchoolBus(Student):

    def __init__(self, students_list=None): self._students = list(students_list) if students_list else []

    def __iter__(self):
        return iter(self._students)

    def __str__(self):
        students2 = [
            '[{}] {} {}, {}'.format(
                index, stud.first_name, stud.last_name, stud.age)
            for index, stud in
            enumerate(self._students)
        ]
        return ' \n'.join(students2)

    def __getitem__(self, index):
        return self._students[index]


students = [
    Student('John', 'Doe', 19),
    Student('Jack', 'Fluffy', 18),
    Student('Matthew', 'Wu', 19),
    Student('Heather', 'Rafferty', 19),
    Student('Randall', 'Blackdall', 20),
    Student('Marissa', 'Raynaud', 19),
    Student('Marlo', 'Ranbot', 19)
]
bus = SchoolBus(students)

# for student in bus.students:
#     print(student)


first_names = [stud.first_name for stud in bus]
print(first_names)

print(bus)

print(bus[2])