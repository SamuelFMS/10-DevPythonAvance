from datetime import date

from business.course_business import CourseBusiness
from business.student_business import StudentBusiness
from models.course import Course
from models.student import Student


def test_add_course():
    """Vérifie qu'un cours peut être ajouté en BDD."""
    course = Course(
        "Test Course",
        date(2026, 1, 1),
        date(2026, 5, 1)
    )

    teacher = CourseBusiness.get_course_by_id(1).teacher
    assert teacher is not None
    assert teacher.id is not None

    course.teacher = teacher

    course_id = CourseBusiness.add_courses(course)

    assert course_id is not None
    assert course_id > 0
    assert course.id == course_id

    # Nettoyage
    CourseBusiness.delete_course(course)


def test_get_course_by_id():
    """Vérifie qu'un cours ajouté peut être récupéré."""
    course = Course(
        "Test Read",
        date(2026, 1, 1),
        date(2026, 5, 1)
    )
    course.teacher = CourseBusiness.get_course_by_id(1).teacher

    course_id = CourseBusiness.add_courses(course)

    read_course: Course | None = CourseBusiness.get_course_by_id(course_id)

    assert read_course is not None
    assert read_course.id == course_id
    assert read_course.name == "Test Read"
    assert read_course.start_date == date(2026, 1, 1)
    assert read_course.end_date == date(2026, 5, 1)

    # Nettoyage
    CourseBusiness.delete_course(course)


def test_update_course():
    """Vérifie qu'un cours peut être modifié."""
    course = Course(
        "Before Update",
        date(2026, 1, 1),
        date(2026, 5, 1)
    )
    course.teacher = CourseBusiness.get_course_by_id(1).teacher

    CourseBusiness.add_courses(course)

    course.name = "After Update"
    course.start_date = date(2026, 2, 1)
    course.end_date = date(2026, 6, 1)

    result = CourseBusiness.update_course(course)

    assert result is True

    updated_course = CourseBusiness.get_course_by_id(course.id)

    assert updated_course is not None
    assert updated_course.name == "After Update"
    assert updated_course.start_date == date(2026, 2, 1)
    assert updated_course.end_date == date(2026, 6, 1)

    # Nettoyage
    CourseBusiness.delete_course(course)


def test_assign_students_to_course():
    """Vérifie que des étudiants peuvent être affectés à un cours."""
    course = Course(
        "Test Students",
        date(2026, 1, 1),
        date(2026, 5, 1)
    )
    course.teacher = CourseBusiness.get_course_by_id(1).teacher

    CourseBusiness.add_courses(course)

    students: list[Student] = StudentBusiness.get_all_students()

    assert len(students) >= 3

    for student in students[:3]:
        assert student.student_nbr is not None
        CourseBusiness.assign_student_to_course(student, course)

    assert len(course.students_taking_it) == 3

    # Encore mieux : vérifier en relisant depuis la BDD
    saved_course = CourseBusiness.get_course_by_id(course.id)

    assert saved_course is not None
    assert len(saved_course.students_taking_it) == 3

    CourseBusiness.delete_course(course)


def test_delete_course():
    """Vérifie qu'un cours peut être supprimé."""
    course = Course(
        "Test Delete",
        date(2026, 1, 1),
        date(2026, 5, 1)
    )
    course.teacher = CourseBusiness.get_course_by_id(1).teacher

    CourseBusiness.add_courses(course)

    course_id = course.id

    result = CourseBusiness.delete_course(course)

    assert result is True

    deleted_course = CourseBusiness.get_course_by_id(course_id)

    assert deleted_course is None


def test_get_all_courses():
    """Vérifie que la récupération de tous les cours fonctionne."""
    courses: list[Course] | None = CourseBusiness.get_all_course()

    assert courses is not None
    assert len(courses) > 0


def tests():
    print("Executing tests for Course")

    test_add_course()
    test_get_course_by_id()
    test_update_course()
    test_assign_students_to_course()
    test_delete_course()
    test_get_all_courses()

    print("All Course tests passed!")


if __name__ == "__main__":
    tests()