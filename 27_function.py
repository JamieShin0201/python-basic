def open_account():
    print("새로운 계좌가 생성되었습니다.")


def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money


def withdraw(balance, money):
    if balance < money:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

    print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
    return balance - money


def withdraw_night(balance, money):
    commission = 100
    if balance < money + commission:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return commission, balance

    return commission, balance - money - commission


open_account()

balance = 0
balance = deposit(balance, 1000)
print(balance)

balance = withdraw(balance, 2000)
print(balance)

balance = withdraw(balance, 500)
print(balance)

commission, balance = withdraw_night(balance, 2000)
print("수수료는 {0}원이며, 잔액은 {1}원입니다".format(commission, balance))

commission, balance = withdraw_night(balance, 400)
print("수수료는 {0}원이며, 잔액은 {1}원입니다".format(commission, balance))
