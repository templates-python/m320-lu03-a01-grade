import pytest

from main import GradeList

@pytest.mark.xfail
def test_main():
    demo = GradeList()
    demo.add_grade(4.5)
    demo.add_grade(5.0)
    demo.add_grade(3.5)
    demo.add_grade(4.0)
    demo.add_grade(4.5)
    demo.add_grade(5.5)
