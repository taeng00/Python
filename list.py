# 리스트

mbti = ['INFP', 'ENFP', 'ISTJ', 'ESTP']  # 리스트 생성

print(mbti)
print(mbti[0])  # 첫번째거 출력

mbti[0] = 'INFJ'  # 첫번째거 변경

print(mbti)
print(mbti[0])


my_list = [123, 'apple']
print(my_list)

colors = ['red', 'blue', 'green']

# 수정
# colors[2] = 'black'
# print(colors)

# 추가1
# colors.append('purple')
# print(colors)

# 추가2 원하는 위치에
# colors.insert(1, 'yellow')
# print(colors)

# 제거
# del colors[0]
# print(colors)

# 제거2
# colors.pop(0)
# print(colors)

# 제거와 동시에 반환 (pop)
# color = colors.pop(0)
# print(colors)
# print(color)

# 제거3 특정한 것을 지정해서 제거
# colors.remove('blue')
# print(colors)


# 리스트 정렬
# colors = ['blue', 'red', 'gray', 'black', 'yellow', 'orange']

# 정렬 1
# colors.sort()
# print(colors)

# 역순 정렬
# colors.sort(reverse=True)
# print(colors)

# 원본데이터 유지
# sorted(colors)
# print(colors)

# 정렬 2
# print(sorted(colors))


# 길이 - 요소의 개수
# print(len(colors))

# 가장 마지막 인덱스에 존재하는것 참조
# print(colors[-1])


# 리스트 슬라이싱

# colors = ['blue', 'red', 'gray', 'black', 'yellow', 'orange']
# colors_2 = colors[:] #범위를 지정해서 리스트 변수로 지정

# print(colors[1:5]) # 1~4까지 출력
# print(colors[:4])
# print(colors[2:]) # 2부터 끝까지
# print(colors[-5:])

"""
scores = [88, 100, 96, 43, 65, 78]
scores.sort(reverse=True)
# print(scores)
for score in scores:
    if score >= 80:
        print(score)
    else:
        print("Fail")
"""

scores = [88, 100, 96, 43, 65, 78]

# max_val = max(scores)
# min_val = min(scores)
sum_val = sum(scores)
avg_val = sum(scores) / len(scores)
print(avg_val)

max_val = max(scores)
min_val = min(scores)
sum_val = sum(scores)  # for문으로도 구할 수 있으나 너무 길어짐
print(max_val, '', min_val, '', sum_val)
