class Fridge:
    isOpened = False
    list = []

    def open(self):
        self.isOpened = True
        print("냉장고 문이 열렸습니다")

    def close(self):
        self.isOpened = False
        print("냉장고 문이 닫혔습니다")

    def status(self):
        if self.isOpened:
            print("냉장고 문이 닫혀있습니다.")
        else:
            print("냉장고 문이 열려있습니다. 문을 닫아 주세요!")

    def put(self, food):
        if not self.isOpened:
            print("냉장고 문이 닫혀있습니다.")
        else:
            self.list.append(food)
            print("음식을 냉장고에 성공적으로 넣었습니다.")
            print(f"현재 냉장고 음식 현황: {self.list}")

class Food:
    pass
