# 파일 읽기

# f = open('literature\poem.txt', 'r', encoding='UTF-8')  # 읽기모드
# C:\Users\user\Desktop\멋사\literature\poem.txt
# literature\poem.txt

# print(f.read())
# print(f.readline())
# print(f.readlines())

# f.close()

# with open('literature\poem.txt', 'r', encoding='UTF-8') as f:
#    print(f.read())


# 파일 쓰기

# 쓰기모드 # w를 a로 바꿔서 출력하면 원본 안날아가고 덮어쓰기
f = open('literature\poem2.txt', 'w', encoding='UTF-8')

f.write("새로운 글이 작성 되었습니다. \n 새로운 글이 작성 되었습니다.")

f.close()
