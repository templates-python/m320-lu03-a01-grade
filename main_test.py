import pytest

from main import GradeList, ListIndexException, ListRangeException, ValueRangeException

class TestGrade:

    @pytest.fixture
    def grades(self):
        gl = GradeList()
        gl.add_grade(4.5)
        return gl


    def test_list_index_ok(self, grades):
        assert grades.take_grade(0) == 4.5

    def test_list_index_exception(self, grades):
        with pytest.raises(ListIndexException):
            grades.take_grade(4)

    def test_value_range_ok(self, grades):
        grades.add_grade(5.0)
        assert grades.take_grade(1) == 5.0

    def test_value_range_low(self, grades):
        with pytest.raises(ValueRangeException):
            grades.add_grade(0.5)

    def test_value_range_high(self, grades):
        with pytest.raises(ValueRangeException):
            grades.add_grade(6.5)

    def test_numer_too_large(self, grades):
        with pytest.raises(ListRangeException):
            for cnt in range(6):
                grades.add_grade(5.0)