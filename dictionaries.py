# 딕셔너리

student = {
    "student_no": "20231231",
    "major": "English",
    "grade": 3
}


print(student["student_no"])

# student["student_no"] = "20230101"

# print(student)
# print(student["student_no"])


# 추가

# student["gpa"] = 4.5 #마지막에 추가됨
# print(student)


# 수정

# student["gpa"] = 4.3
# print(student)

# 삭제

# del student["grade"]
# print(student)

# 데이터 접근

# print(student.get("major"))
# print(student.get("gpa","해당 키-값 쌍이 없습니다"))
# #get("키","x") x의 자리에는 키에 해당한 키-값 쌍이 없다면 x를 출력

# 딕셔너리의 키를 반환

# print(list(student.keys()))

# 딕셔너리의 값을 반환

# print(list(student.values()))

# 딕셔너리 반복문
tech = {
    "HTML": "Advanced",
    "JavaScript": "Intermediate",
    "Python": "Expert",
    "GO": "Novice"
}
# for i in tech:
#  print(i) #key 값만 포함 시킴

# for key, value in tech:
#  print(f'{key} - "{value}')
# ValueError: too many values to unpack (expected 2)

# for key , value in tech.items():
#  print(f'{key} - {value}')

# for value in tech.values():
#    print(value)

# for key in tech.keys():
#    print(key)


# 중첩

"""
student_1 = {
  "student_no" : "1",
  "gpa" : "4.3"
}

student_2 = {
  "student_no" : "2",
  "gpa" : "3.8"
}

"""
# students = [student_1, student_2]
# print(students)

# for student in students:
#  print(student)

"""for student in students:
  student['graduated'] = False
  print(student['student_no'])
  print(student)
"""
# student = {
#  "subjects": ["회계원리","중국어회화"]
# }

# print(student["subjects"])
# subjects_list = student["subjects"]
# for subject in subjects_list:
#  print(subject)

# 딕셔너리 안에 딕셔너리
student = {
    "scholarship": {
        "name": "국가장학금",
        "amount": "1000000"
    }
}
print(student)

print(student["scholarship"])

for key in student.keys():
    print(key)

for value in student.values():
    print(value)

for value in student.values():
    for value_2 in value.values():
        print(value_2)
