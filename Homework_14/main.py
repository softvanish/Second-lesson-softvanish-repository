from student import Student
from group import Group
from group_limit_exception import GroupLimitReachedException


def main():
    st1 = Student('Male', 20, 'John', 'Smith', 'AN145')
    st2 = Student('Female', 22, 'Anna', 'Brown', 'AN145')
    st3 = Student('Male', 23, 'Mike', 'Johnson', 'AN145')
    st4 = Student('Female', 21, 'Emily', 'Davis', 'AN145')
    st5 = Student('Male', 24, 'Alex', 'Miller', 'AN145')
    st6 = Student('Female', 22, 'Olivia', 'Wilson', 'AN145')    # Для теста я добавил больше студентов. Если задокументировать последнего,
    st7 = Student('Male', 25, 'Daniel', 'Anderson', 'AN145')    # то ошибку не выдаст, ведь максимум студентов 10
    st8 = Student('Female', 23, 'Sophia', 'Thomas', 'AN145')
    st9 = Student('Male', 21, 'David', 'Moore', 'AN145')
    st10 = Student('Female', 24, 'Grace', 'Taylor', 'AN145')
    st11 = Student('Male', 26, 'Brian', 'Clark', 'AN145')

    gr = Group('PD1')

    try:
        gr.add_student(st1)
        gr.add_student(st2)
        gr.add_student(st3)
        gr.add_student(st4)
        gr.add_student(st5)
        gr.add_student(st6)
        gr.add_student(st7)
        gr.add_student(st8)
        gr.add_student(st9)
        gr.add_student(st10)
        gr.add_student(st11)

    except GroupLimitReachedException as error:
        print(error)
    except Exception as error:
        print(error)

    print(gr)

    '''вторая проверка'''

    # st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    # st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    # gr = Group('PD1')
    # gr.add_student(st1)
    # gr.add_student(st2)
    # print(gr)
    # assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
    # assert gr.find_student('Jobs2') is None
    #
    # gr.delete_student('Taylor')
    # print(gr)  # Only one student


if __name__ == '__main__':
    main()

# from test import show_data_from_test
#
# print(__name__)
# show_data_from_test()
