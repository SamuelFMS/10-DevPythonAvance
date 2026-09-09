from business.student_business import StudentBusiness
from daos.address_dao import AddressDao
from models.student import Student


def tests():
    print("Executing tests for student")

    # Creation d'un cours
    student = Student("FirstNameTest", "LastNameTest", 20)
    address_dao = AddressDao()
    address = address_dao.get_all()[0]
    student.address = address
    assert student.address is not None
    new_student_id = StudentBusiness.add_student(student)
    assert new_student_id != 0
    assert student.student_nbr == new_student_id

    #Recuperation du cours dans la base de donnée
    read_student = StudentBusiness.get_student_by_id(new_student_id)
    assert read_student is not None
    assert read_student.student_nbr == new_student_id
    assert read_student.first_name == 'FirstNameTest'
    assert read_student.last_name == 'LastNameTest'
    assert read_student.age == 20
    assert read_student.address == address

    #Edition du student
    read_student.first_name = 'NewFirstName'
    read_student.last_name = 'NewLastName'
    read_student.age = 21
    assert StudentBusiness.update_student(read_student)
    edited_student = StudentBusiness.get_student_by_id(read_student.student_nbr)
    assert edited_student.first_name == 'NewFirstName'
    assert edited_student.last_name == 'NewLastName'
    assert edited_student.age == 21

    #Suppression du cours que nous venons de créer
    assert StudentBusiness.delete_student(read_student)

    #Verifie que get_all n'est pas vide
    list_student:list|None = StudentBusiness.get_all_students()
    assert list_student is not None
    assert len(list_student) > 0


if __name__ == '__main__':
    # tests unitaires
    tests()