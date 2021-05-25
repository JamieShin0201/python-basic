import sys

print('Python', 'Java', 'JavaScript', sep=',', end='?')
print('무엇이 더 재밌을까요?')

print('Python', 'Java', 'JavaScript', file=sys.stdout)
print('Python', 'Java', 'JavaScript', file=sys.stderr)

# 시험 성적
scores = {'수학': 0, '영어': 50, '코딩': 100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
for num in range(1, 21):
    print('대기번호 : ' + str(num).zfill(3))

answer = input('아무 값이나 입력하세요 : ')  # 사용자 입력은 문자열로 받아진다.
print('입력하신 값은 ' + answer + '입니다.')
print(type(answer))
