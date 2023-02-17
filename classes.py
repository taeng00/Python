# 클래스 - 설계

class Student:  # 클래스는 대문자로 시작

    def __init__(self, name, major, is_graduated):
        self.name = name
        self.major = major
        self.is_graduated = is_graduated

    def study(self):
        print(f'{self.name} 학생은 공부중입니다')

    def edit_major(self, new_major):
        student_1.major = new_major
        print(f'{student_1.major}로 전공이 변경 되었습니다.')

# 인스턴스 - 실체화된 사물


student_1 = Student('김멋사', '정보보호학과')

student_1.edit.major = '기계공학과'

print(student_1.major)


# student_1_name = student_1.name
# print(student_1_name)

# student_1_graduated = student_1.is_graduated
# print(student_1_graduated)

# student_1.study()


# 상속

class ForeignStudent(Student):

    def __init__(self, name, major, country):
        super().__init__(name, major)
        self.country = country

    def study(self):  # 오버라이딩
        print(f'{self.name} is studying now')


foreign_stud_1 = ForeignStudent('이테킷', '국어국문학과', '미국')
foreign_stud_1.study()

# print(foreign_stud_1.name)
# print(foreign_stud_1.major)
# print(foreign_1.country)
# print(foreign_stud_1.is_graduated)
# foreign_1.study()
