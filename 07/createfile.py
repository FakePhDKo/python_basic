import os, time

data = """반갑습니다. python 개발자 여러분 한살 더 드셨죠!
올 한해는... 행복 가득한 한해가 되었으면 합니다!
"""

if not os.path.isdir('/root/test'):
    os.mkdir('/root/test')

file = "/root/test/test.txt"

with open(file, "w") as fd:
    fd.write(data)

print(open(file).read())

time.sleep(5)

if os.path.exists("/root/test/test.txt"):
    ans = input("이 파일을 삭제하시겠습니까? (y/n): ")
    if ans.lower().startswith("y"):
        os.remove("/root/test/test.txt")
