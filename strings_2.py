score = "점수:90"
print(score.removeprefix("점수:"))  # .removeprefix = ()안에 변수에서 삭제하고 싶은 부분 삭제

score_2 = "75점"
print(score_2.removesuffix("점"))  # .removesuffix = ()안에 변수에서 삭제하고자 하는 부분을 삭제

city = "서울 중구"
print(city.replace("서울", "서울시"))

si_1 = "용인"
gu_1 = "기흥"
address_1 = f"{si_1}시 {gu_1}구"
print(address_1)

si_2 = "서울"
gu_2 = "종로"

# 서울시 종로구
# 용인시 기흥구
# (시의 이름)시 (구의 이름)구

print(f"{si_1}시 {gu_1}구")
print(f"{si_2}시 {gu_2}구")
