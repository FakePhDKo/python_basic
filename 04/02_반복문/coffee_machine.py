coffee = 5

while True:
    money = input("돈을 넣어 주세요: ")

    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

    if int(money) == 300:
        print("커피를 줍니다.")
        coffee -= 1
        print(f"남은 커피 {coffee}개")

    elif int(money) > 300:
        print(f"거스름돈 {int(money) - 300}을 주고 커피를 줍니다.")
        coffee -= 1
        print(f"남은 커피 {coffee}개")

    elif int(money) < 300:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print(f"남은 커피 {coffee}개")




