from builtins import int


class GradeList:
    def __init__(self):
        self._MAX_GRADE_COUNT = 5
        self._grades = []

    def add_grade(self, grade: float) -> None:
        if grade < 1.0 or grade > 6.0:
            raise GradeRangeError(grade)
        elements = self.get_current_grade_count()
        if elements >= self._MAX_GRADE_COUNT:
            raise Overflow('Fehler: Zu viele Werte eingegeben\n')
        self._grades.append(grade)

    def get_max_grade_count(self) -> int:
        return self._MAX_GRADE_COUNT

    def get_current_grade_count(self) -> int:
        return len(self._grades)

    def get_grade(self, index: int) -> float:
        return self._grades[index]

    def remove_grade(self, index: int) -> None:
        self._grades.pop(index)

    def print(self) -> None:
        r = range(self.get_current_grade_count())
        for i in r:
            print(f"{i + 1}. Note: {self._grades[i]}")


class Overflow(RuntimeError):
    pass


class GradeRangeError(RuntimeError):

    def __init__(self, grade: int):
        message = f'Fehler: Der Notenwert muss im Bereich 1.0 bis 6.0 liegen. Er beträgt jedoch {grade}.'
        super().__init__(self, message)


if __name__ == '__main__':
    demo = GradeList()
    try:
        demo.add_grade(4.5)
        demo.add_grade(5.0)
        demo.add_grade(3.5)
        demo.add_grade(4.0)
        demo.add_grade(0.5)
        # und einen nächsten Wert einfügen, der zu einem Overflow führen wird.
        demo.add_grade(3.5)
    except GradeRangeError as ge:
        print(ge)
    except Overflow as of:
        print(of)
    demo.print()

    print('\nLösche Wert an 2. Stelle')
    demo.remove_grade(1)  # Index beginnt bei 0
    demo.print()

    # und nun einen Wert an einer Stelle lesen, die es nicht gibt
    try:
        print(f'\n8. Note = {demo.get_grade(8)}')
    except IndexError:
        print(f'Falscher Index; gültig sind Werte von 0 bis {demo.get_max_grade_count() - 1}')

    print(f'\nListe umfasst zur Zeit {demo.get_current_grade_count()} Noten')
    print(f'Note an 3. Stelle ist {demo.get_grade(2)}')
    print(f'Grösse der Liste beträgt {demo.get_max_grade_count()}\n')
    demo.print()