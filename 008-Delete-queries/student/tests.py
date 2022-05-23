import pytest
from student.models import Student
from django.db import IntegrityError
from student.forms import StudentForm

@pytest.mark.parametrize(
    "age",
    [
        (9),
        (21),
    ],
)
def test_student_age(db, age):
    with pytest.raises(IntegrityError):
        Student.objects.create(firstname="fname", surname="sname", age=age, classroom=100, teacher="sir")

def test_student_form():

    data = {
        'firstname':'asd',
        'surname':'asd',
        'age':'30',
        'classroom':'100',
        'teacher':'sir'
    }

    form = StudentForm(data=data)
    assert False == form.is_valid()