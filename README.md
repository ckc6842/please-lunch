# 점심을 부탁해
점심 메뉴를 추천해주는 Web Application.

## db 업그레이드.
models.py 를 수정한 후
데이터베이스의 'alembic_version' 테이블을 삭제하고
db.bat 을 실행하면 자동으로 db 최신화가 가능하다.

## 가상환경 유지
pip install -r requirements.txt
새로운 라이브러리 flask-classy가 추가됨.
pip install flask-classy

## flask-classy 사용법
https://pythonhosted.org/Flask-Classy/

1. View
from flask_classy import FlaskView
class FooView(FlaskView):
    pass

2. init
FooView.register(app)

3. url_for(뷰클래스이름:메서드이름) 

4. class의 get method 가 get요청 post method가 각각 post 요청.

4. 자세한 사용법은 views 폴더에 있는 코드 참고.

   
