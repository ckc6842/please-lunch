# please-lunch.
식사 메뉴 예측 웹 어플리케이션.
프로젝트 폴더 구성을 위해 
https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications
를 참고함.

## 라이브러리 일치 시키기
pip install -r requirements.txt

## 엔드포인트 정의서 
https://docs.google.com/spreadsheets/d/1DLHkjEcVZYrWwVgOTowgxalZ-kyOdSre150GHR_l5_Q/edit?usp=sharing
(You should login Google!)

## 가입 시 메일 보내는 기능 없음.
가상환경 설치 후 flask-security 의 utils.py 에 send_email method의  mail.send(msg) 부분을 주석 처리할 것.
안 하면 회원가입 할 때 메일주소가 제대로 설정 안 되있어서 오류남.


