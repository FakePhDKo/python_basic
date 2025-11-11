import time, os

content = """Hello! Welcome to my demofile.txt!
This file is for testing purposes
Good Luck!"""

file = 'file.txt'

with open(file, 'w') as fd:
    fd.write(content)

time.sleep(5)

if os.path.exists(file):
    ans = input("Really? (y/n): ")
    if ans.lower().startswith('y'):
        os.remove(file)
