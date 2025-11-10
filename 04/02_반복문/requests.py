import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1/cmd.php'

while True:
    cmd = input('[root@localhost ~]')
    params = {'cmd': cmd}

    resp = requests.get(url, params=params)
    soup = BeautifulSoup(resp.text, 'html.parser')
    print(soup.pre)