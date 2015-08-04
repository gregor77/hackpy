## hackpy
hacking with python

1. Installation (Windows 환경)
 1. 파이썬 다운로드 후 설치
 2. command에서 python과 pip 명령어를 사용하기 위해서, 환경변수 추가
  - PATH에 C:\Python27;C:\Python27\Scripts; 추가

 * [참조]
  + [Python 공식 홈페이지](http://python.org)
  + [Python 매뉴얼](https://docs.python.org/)
  + [PyPI 홈페이지](https://pypi.python.org/pypi/)
  + [Python 설치 Stackoverflow](http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows)
2. requests 패키지

  ```
  $pip install requests
  ```
1. Response 확인
 * res = request.get(url)
 * res.content
   * Response 데이터 확인 (디코딩 x)
 * res.text
   * Response 데이터 확인 (디코딩 o)
 * res.json()
   * Response 데이터가 json 일 경우, python 자료형으로 변환
 * res.headers
   * Response에 넘어온 헤더 확인
 * res.url
   * dir(res)
2. 파라미터 전송
 * res = requests.get(url, params={'key1':'value1'm 'key2':'value2'})
   * python의 dict 자료형으로 파라미터 정보를 세팅해서 전달
   
   ```
   $res.url을 입력하면, queryString이 조립된 형태의 url을 확인할 수 있다.
   ```
   * ex) requests.get('http://www.naver.com', params={'hello':'world'})
 * res = requests.post(url, data={'key1':'value1'm 'key2':'value2'})
   * 단 post로 전송한 경우, $res.url로 확인하더라도 data 보이지 않는다.
   * post는 기본적으로 get()을 포함한다. 따라서 get 전송방식을 post를 활용해서 사용 가능하다.
   
   ```
   $res =requests.post('http://cykor.kr/sdsds/sds.php', params={'id':'admin', 'pw':'123'}, data={id':'test', 'pw':'456'}).content
   ```
  * get, post 방식의 value가 모두 전달된 것을 확인할 수 있다.
3. 헤더 전송
  * res = requests.get(url, headers={'User-Agent':'python-hacking'})
4. requests 실습
  * get, post 방식으로 전달받은 파라미터 (id, pw)를 출력하는 페이지 하나 생성
  
  ```
  $requests.get('http://cykor.kr/sdsds/sds.php', params={'id':'admin', 'pw':'123'}).content
  $requests.post('http://cykor.kr/sdsds/sds.php', data={'id':'admin', 'pw':'123'}).content
  ```
  
3. BeatifulSoup 패키지

  ```
  $pip install BeautifulSoup
  ```
