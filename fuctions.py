# 함수
# 매개변수(파라미터), 인자(인수)

# 'name' = 파라미터 #정의를 내릴 때
# 함수를 실행할 때는 인자(인수)
"""
def print_name(name):
    print(f'학생의 이름은 {name} 입니다') #name = 매개변수(파라미터) 

print_name("김멋사") # "김멋사" 는 인자(인수)
print_name("이멋사")
"""
"""
def print_ex_string():
    print('예시 문자열입니다')

print_ex_string()
"""

"""
def print_name_age(name,age):
    print(f'이름은 {name}이고 나이는 {age}살 입니다.')
print_name_age("김멋사","24")
print_name_age() #안돼
#TypeError: print_name_age() missing 2 required positional arguments: 'name' and 'age' 
"""

"""
def order_coffee(qty,option='hot'): #option에 hot이라는 기본값을 줌. 기본값을 지정할 때는 기본값이 없는 파라미터 뒤에 위치 시켜야됨
    print(f'{qty}잔 / {option}')

order_coffee(3,'iced')
order_coffee(3)
order_coffee(option='iced',qty=5) #기본값 있어서 ㄱㅊ
"""

"""
def get_id(email):
    
    if email.endswith('@test.com'): #endswith = 해당 값으로 끝나는지 검증
        email_id =email.removesuffix('@test.com')
        print(email_id)
        return email_id
    else:
        print('처리할 수 없는 이메일 주소입니다')
        
user_id = get_id('user@test.com') #return을 통해 값을 반환 받을 때 활용
print(user_id)
"""
