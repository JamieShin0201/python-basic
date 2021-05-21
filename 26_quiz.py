from random import *

passengers = [randint(5, 50) for _ in range(50)]

index = 0
count = 0
for passenger in passengers:
    index += 1
    if 5 < passenger < 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(index, passenger))
        count += 1
        continue

    print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(index, passenger))

print("총 탑승 승객 : {0}분".format(count))

count = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 < time < 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        count += 1
        continue

    print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0}분".format(count))
