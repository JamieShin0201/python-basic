# 리스트 []

subway1 = 10
subway2 = 20
subway3 = 30

subways = [10, 20, 30]
print(subways)

subways = ["유재석", "조세호", "박명수"]
print(subways)

# 위치 확인
print(subways.index("조세호"))

# 지하철 끝에 추가
subways.append("하하")
print(subways)

# 지하철 중간에 추가
subways.insert(1, "정형돈")
print(subways)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subways.pop())
print(subways)

# 같은 이름의 사람이 몇 명 있는지 확인
subways.append("유재석")
print(subways)
print(subways.count("유재석"))

# 정렬
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형을 함께 사용 가능
mix_list = ["유재석", 20, True]
print(mix_list)

# 리스트 확장
subways.extend(mix_list)
print(subways)
