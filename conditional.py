# 조건문

"""
if False:
    print("True")
else:
    print("False")
"""

"""
if 4 > 3:
    print("a")  # True일 때 출력
else:
    print("b")  # False일 때 출력
"""

"""
value = input("값을 입력 해 주십시오: ")
# 입력 값을 string(문자열) 타입으로 처리
if int(value) > 10:
    print("a")
else:
    print("b")
"""
"""
value = input("값을 입력 해 주십시오: ")
value = value.upper()

if value == "ESFP":
    print("ESFP")  # 대소문자를 구분하기 때문에 값이 나오지 않음
else:
    print("nothing")
"""

day = input("요일을 입력해 주세요(0~6): ")

if day == "0":
    print("휴무")
elif day == "6":
    print("단축영업")
else:
    print("정상영업")
