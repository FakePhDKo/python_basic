from curses.ascii import isdigit

def check(pass1):
    index = 2
    first = 0
    pass_list = list(pass1)

    for i in range((len(pass1) - 1)):
        if pass_list[i].isdigit():
            first += int(pass_list[i]) * index
            if index == 9:
                index = 1
            index += 1

    second = first % 11
    result = (11 - second) % 10

    if result == int(pass1[13]):
        return print("유요한 주민번호 입니다.")
    else:
        return print("유요하지 않은 주민번호입니다.")


password = input("주민번호를 입력하세요: ")
check(password)


