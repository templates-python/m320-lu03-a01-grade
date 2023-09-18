class GradeList:
    """
    Eine Liste von Notenwerte.
    Die Liste ist auf MAX_GRADE_COUNT Elemente begrenzt. Zudem dürfen die
    Notenwerte nur im Bereich 1.0 ... 6.0 liegen.
    Beide Zusicherungen werden in der Methode add_grade überprüft.
    """

    def __init__(self):
        """
        Definiert den Range der Liste und erstellt eine leere Liste.
        """
        self._MAX_GRADE_COUNT = 5
        self._grades = []

    def add_grade(self, grade):
        """
        Fügt einen Notenwert der Liste zu.
        Der Wert muss im Bereich 1.0 ... 6.0 liegen.
        Es können maximal MAX_GRADE_COUNT Elemente der Liste zugefügt werden.
        :param grade: ein Notenwert
        """
        elements = self.current_grade_count
        if elements < self._MAX_GRADE_COUNT:
            self._grades.append(grade)
        else:
            print('FEHLER: Zu viele Werte eingegeben\n')

    @property
    def max_grade_count(self):
        """
        Liefert die maximale Grösse der Liste.
        :return: Grösse der Liste
        """
        return self._MAX_GRADE_COUNT

    @property
    def current_grade_count(self):
        """
        Liefert die aktuelle Anzahl der in der Liste abgelegten Notenwerte.
        :return: Anzahl Notenwerte
        """
        return len(self._grades)

    def take_grade(self, index: int):
        """
        Liefert den durch index bezeichneten Notenwert aus der Liste.
        :param index: Position des Notenwertes
        :return: Notenwert
        """
        return self._grades[index]

    def remove_grade(self, index: int):
        """
        Entfernt an der Stelle index einen Wert.
        :param index: Position die entfernt wird
        """
        self._grades.pop(index)

    def print(self):
        """
        Gibt alle Notenwert am Stdout aus.
        """
        r = range(self.current_grade_count)
        for i in r:
            print(f'{i + 1}. Note: {self._grades[i]}')

def main():
    demo = GradeList()
    demo.add_grade(4.5)
    demo.add_grade(5.0)
    demo.add_grade(3.5)
    demo.add_grade(4.0)
    demo.add_grade(4.5)
    demo.print()
    # und einen nächsten Wert einfügen, der zu einem Overflow führen wird.
    print("\nund nun einen weiteren Wert zufügen")
    demo.add_grade(3.5)
    demo.print()

    print("\nLösche Wert an 2. Stelle")
    demo.remove_grade(1)  # Index beginnt bei 0
    demo.print()

    # und nun einen Wert zufügen der eine ungültige Note darstellt.
    print("\nund nun eine ungültige Note zufügen")
    demo.add_grade(7.0)
    demo.print()

    # und nun einen Wert an einer Stelle lesen, die es nicht gibt
    print("\nNote an Position 8 lesen ")
    print(demo.take_grade(8))

    print(f"\nListe umfasst zur Zeit {demo.current_grade_count} Noten")
    print(f"Note an 3. Stelle ist {demo.take_grade(2)}")
    print(f"Grösse der Liste beträgt {demo.max_grade_count}\n")
    demo.print()


if __name__ == '__main__':
    main()
