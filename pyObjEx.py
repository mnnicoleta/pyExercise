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


class LoggingMixin:

    def __init__(self, *args, **kwargs):
        class_name = type(self).__name__
        print('Initializing object of type {}'.format(class_name))

        return super().__init__(*args, **kwargs)

    def __getitem__(self, index):
        print('Getting key ' + str(index))

        return super().__getitem__(index)


class LoggingSchoolBus(LoggingMixin, SchoolBus):
    pass


print("Mixins=========================")
bus = LoggingSchoolBus(students)
print(bus)
print(bus[1])


class StudentsCollection:

    def __init__(self, students_list=None):
        self._students = list(students_list) if students_list else []

    def __iter__(self):
        return iter(self._students)

    def __getitem__(self, index):
        return self._students[index]


class SchoolBusPrinter():
    def __str__(self):
        students = [
            '[{}] {} {}, {}'.format(
                index, stud.first_name, stud.last_name, stud.age)
            for index, stud in
            enumerate(self._students)
        ]
        return ' \n'.join(students)


class SchoolBus(StudentsCollection, SchoolBusPrinter):
    pass


class LoggingSchoolBus(LoggingMixin, SchoolBus):
    pass


print("------SchoolBus(students)")
simple_bus = SchoolBus(students)
print(simple_bus)
print(simple_bus[3])

print("########SchoolBus(students)")
logging_bus = LoggingSchoolBus(students)
print(logging_bus)
print(logging_bus[4])
