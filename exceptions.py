# Exceptions(예외)

a = 10
b = 0

a / b


fruits = ['apple', 'banana', 'strawberry']
# fruits[3] #IndexError: list index out of range

try:
    fruits[3]
except:
    print('인덱스를 참조 할 수 없습니다')
else:
    print("정상 수행")

try:
    fruits[3]
except:
    print('인덱스를 참조 할 수 없습니다')
finally:
    print("명령 수행")

print(fruits)
