class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print('{0} 유닛이 생성 되었습니다.'.format(self.name))
        print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))


marine1 = Unit('마린1', 40, 5)
marine2 = Unit('마린2', 40, 5)
tank1 = Unit('탱크1', 150, 35)

# TypeError: missing arguments
# marine3 = Unit('마린')

wraith1 = Unit('레이스', 80, 5)
print('유닛 이름 : {0}, 공격력 : {1}'.format(wraith1.name, wraith1.damage))

wraith2 = Unit('레이스', 80, 5)
wraith2.clocking = True

if wraith2.clocking:
    print('{0}는 현재 클로키 상태입니다.'.format(wraith2.name))
