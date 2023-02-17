print('=============================')
print('회원가입')
print('=============================')

register = False

while not register:
    print('회원가입을 진행 하시겠습니까?\n y:진행 \t n:취소')
    register_input = input('>> ')
    register_input = register_input.lower()

    if register_input == 'y':
        register = True
        print('=============================')
        print('회원가입이 진행 됩니다')
        print('=============================')
    elif register_input == 'n':
        print('=============================')
        print('회원가입이 취소 됩니다')
        print('=============================')
        exit()

print('입력 값을 확인해주세요')

users = []

while True:

    user = {}

    username = input('ID: ')
    while True:
        password = input('PW: ')
        password_confirm = input('PW 확인: ')
        if password == password_confirm:
            break
        else:
            print('패스워드가 일치하지 않습니다. ')
    name = input('이름')
    while True:
        birth_date = input('생년월일(6자리): ')
        if len(birth_date) == 6:
            break
        else:
            print('생년월일의 입력값이 올바르지 않습니다')
    email = input('이메일: ')

    user['username'] = username
    user['password'] = password
    user['name'] = name
    user['birth_date'] = birth_date
    user['email'] = email

    users.append(user)
    print(user)

    print("==========================")
    print(f"{user['name']}님 가입을 환영합니다!")
    print("==========================")

    print('회원가입을 추가로 진행 하시겠습니까? \n y:진행 \t:취소')
    register_another_input = input('>>')
    register_another_input.lower()

    if register_another_input == 'y':
        pass
    elif register_another_input == 'n':
        exit()
