# 반복문

i = 0
sum = 0

# for i in range (1,101): #1부터 100까지 실행
#    print(i)

for i in range(1, 101):
    sum = sum + i

print(sum)

"""
while True: #while을 다룰 때는 범위 설정 필수 아니면 무한루프
    print("while loop")
"""

progress = 0

while progress < 100:

    progress = progress + 1
    print(f"{progress}% completed")
