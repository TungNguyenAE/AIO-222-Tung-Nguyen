from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        self._name = name
        self._yob = yob
        self._grade = grade

    def describe(self):
        print(f"Student Name: {
              self._name} - YoB: {self._yob} - Grade: {self._grade}")


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        self._name = name
        self._yob = yob
        self._subject = subject

    def describe(self):
        print(f"Teacher Name: {
              self._name} - YoB: {self._yob} - Subject: {self._subject}")


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        self._name = name
        self._yob = yob
        self._specialist = specialist

    def describe(self):
        print(f"Doctor Name: {
              self._name} - YoB: {self._yob} - Specialist: {self._specialist}")


class Ward():
    def __init__(self, name: str):
        self.__name = name
        self.__listPeople = list()

    def add_person(self, person: Person):
        self.__listPeople.append(person)

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for p in self.__listPeople:
            p. describe()

    def count_doctor(self):
        counter = 0
        for p in self.__listPeople:
            if hasattr(p, '_specialist'):
                counter += 1
        return counter

    def sort_age(self):
        return self.__listPeople.sort(key=lambda x: x._yob, reverse=True)

    def compute_average(self):
        teachers = []
        for p in self.__listPeople:
            if hasattr(p, '_subject'):
                teachers.append(p._yob)
        return sum(teachers)/len(teachers)


# Testcase:
if __name__ == "__main__":

    # 2(a)
    student1 = Student(name="studentA", yob=2010, grade="7")
    student1.describe()

    teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
    teacher1.describe()

    doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
    doctor1.describe()

    # 2(b)
    print()
    teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
    doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
    ward1 = Ward(name="Ward1")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    ward1.describe()

    # 2(c)
    print(f"\nNumber of doctors : {ward1.count_doctor()}")

    # 2(d)

    print("\nAfter sorting Age of Ward1 people")
    ward1 . sort_age()
    ward1 . describe()

    # 2(e)
    print(f"\nAverage year of birth ( teachers ): {ward1 . compute_average()}")
