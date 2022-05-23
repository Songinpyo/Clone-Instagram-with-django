django = MTV

Model : "회원이라는 모델을 만들면 그 내부에 ID, PW, E-mail 등이 있다."
라고 field를 정해주는 것

View : Controller -> 데이터 처리

Template : 화면을 보이는 부분, html, css

Setting.py : 기본적인 설정을 위해 많이 바뀌는 곳

manage.py : django framework를 쓸 때, 장고를 관리하는 명령어를 통해서 장고를 띄우거나,
장고 DB를 만들거나, 모델에서 객체를 만들거나, DB랑 마이그레이션 할 때 등에 사용되는 소스

# 1. manage.py 실행 - 장고 실행

IP 주소의 의미 : xxx.xxx.xxx.xxx 이런 식으로 나타난다.
well-known ip 주소 : 127.0.0.1 - loop back or Local host
어떤 컴퓨터가 127.0.0.1 무언가를 보내면 다시 컴퓨터로 돌아온다. [자기자신]

127.0.0.1:8000 뒤에 포트번호 8000이 붙는데, 포트번호는 IP주소가 같을 때,
무엇으로 접근할지 나누어주는 것 Ex) 내 IP 주소에 django, react 모두 제공시

그래서 주어진 ip주소로 접속하고 새로고침 하면 아래와 같은 코드가 뜬다.
```python
[22/May/2022 20:16:57] "GET / HTTP/1.1" 200 10697
[22/May/2022 20:17:00] "GET / HTTP/1.1" 200 10697
[22/May/2022 20:17:03] "GET / HTTP/1.1" 200 10697
```
내가 접속하는 행위는 GET을 통해서 접근하는 것이고, http 200 은 성공을 의미한다.
이런것을 http 상태 코드 라고 한다.


# 2. 장고에 내가 만든 페이지를 띄워보자

templates 폴더에 하위 폴더를 만들어보자. - pyostagram
그 안에 main.html 만들어서 이런저런 내용 집어넣기

이 main.html을 보여주기 위해서는 View에서 처리를 해서,
사용자에게 보여줄 수 있도록 해야한다. 그러려면 url을 만들어야한다.
urls.py

urls.py 가보면 이미 admin은 생성하지 않아도 만들어져 있다.
```python
path('admin/', admin.site.urls)
# ip 주소 뒤에 admin을 입력하면, 뒤에 거를 불러온다.
```

그 뒤에 실행해야하는 것이 바로 view이다.
views.py를 생성해야한다.

그전에, django REST framework 를 설치해야한다.
REST란, Get 호출은 조회다, Post는 업데이트다, Put은 입력이다
이런식으로 표준을 정해주는 행위를 말한다.
pip install djangorestframework

views.py 내에 내가 원하는 함수를 생성해주고,
urls.py 에서 import 한다.
그리고, 내가 입력한 주소에 지금은 None, main.html 이 불러와진다.

왜 templates 안에 또, pyostagram이라는 폴더를 만들었을까??
A) 또 폴더를 만들어서 여러개의 앱을 만들 수 있다.
앱은 터미널에서 python manage.py startapp 앱이름 하면된다.

나중에 feed에 쓸 content 앱을 미리 만들어보자
python manage.py startapp content
나는 아나콘다 가상환경이라, 아나콘다 프롬프트로 경로에 접근해서 입력

기본 만들어져 있던 폴더는 앱으로 취급 않주기 때문에,
setting.py에서 installed_apps 에 추가해주어야한다.

클론 코딩을 할 때, 무엇부터 할지 막막하지만
저자는 동작하지 않더라도, 메인화면부터 레이아웃을 만든다고한다.

# 메인화면 클론 코딩

getbootstrap.kr 에서 시작하기 위한 기본 소스를 가져온다.
이미 만들어진 디자인을 가져다 쓸 수 있는 웹 디자인 프레임 워크이다.
djangoProject의 main.html에 스타터템플릿을 붙여넣는다.

# 상단바 만들기
인스타그램처럼 상단에 붙어서 움직일 수 있고 누르면 이동가능한것을 네비바 라고 한다.
예시한번 보고 만들고 싶으면 만드는 법을 찾는다

네비바의 경우 문서-컴포넌트-내비게이션 바 에 있다.
검색창을 만들어야 할거 같은데, 구조를 살펴보면
<div> 시작
</div> 끝
구조로 이루어져 있다.

근데 <div style="">를 통해서 css 스타일을 먹일수가 있다.
나는 색깔을 부여해본다.

가로로 정렬하려면 div 안에 div들을 넣고 flex-direction을 사용한다.

그래서 상단바를 만들기 위해서, body에 네비바 코드를 불러오고 내가 필요한 검색창만 남기고 다 지운다.
Navibar 위치에, <img src="">를 이용해서 인스타 로고를 넣는다. 이미지에도 css먹일 수 있다.

검색에 버튼도 날리고, 이제 우측 아이콘들을 넣어줘야 하는데,
구글 머티리얼 아이콘 사용 (무료 아이콘) https://material.io/

머티리얼 아이콘 쓰려면 구글 폰트 가이드 https://developers.google.com/fonts/docs/getting_started
에서 Using via Google Fonts 에 나오는 코드를 우리꺼에 넣어줘야한다.

근데 outlined는 따로하고 뭐 겁나 헷갈리니까, 그냥 이거 복붙하셈
  <link
    href="https://fonts.googleapis.com/css?family=Material+Icons|Material+Icons+Outlined|Material+Icons+Two+Tone|Material+Icons+Round|Material+Icons+Sharp"
    rel="stylesheet">

