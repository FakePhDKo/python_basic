marks = [90, 25, 67, 45, 80]

for num, mark in enumerate(marks):
    i = num + 1
    if mark >= 60:
        print(f"{i}번째 학생: 합격")
    else:
        print(f"{i}번째 학생: 불합격")
