def get_id(email):

    if email.endswith('@test.com'):  # endswith = 해당 값으로 끝나는지 검증
        email_id = email.removesuffix('@test.com')
        print(email_id)
        return email_id
    else:
        print('처리할 수 없는 이메일 주소입니다')
