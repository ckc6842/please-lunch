# -*- coding: utf-8 -*-
# Statement for enabling the development environment
DEBUG = True
WTF_CSRF_ENABLED = True
# Define the application directory
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example

if sys.platform == 'win32':
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost/please-lunch'
    # celery db config
    CELERY_BROKER_URL = 'sqla+' + SQLALCHEMY_DATABASE_URI
    CELERY_RESULT_BACKEND = 'db+mysql+pymysql://root:1234@localhost/please-lunch'
else:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:n6!cfe5!73@localhost/please_lunch'
    # celery db config
    CELERY_BROKER_URL = 'sqla+' + SQLALCHEMY_DATABASE_URI
    CELERY_RESULT_BACKEND = 'db+mysql+pymysql://root:n6!cfe5!73@localhost/please_lunch'

DATABASE_CONNECT_OPTIONS = {}

# UPLOAD_FOLDER
UPLOAD_FOLDER = 'app/static/uploads/'

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "d41d8cd98f00b204e9800998ecf8427e"

# Secret key for signing cookies
SECRET_KEY = "super-secret"

SECURITY_REGISTERABLE =  True  # 회원가입 기능 켜기/끄기
SECURITY_CONFIRMABLE = False  # 이메일 인증 기능 켜기/끄기
SECURITY_TRACKABLE = True  # 로그인 추적 기능 켜기/끄기
SECURITY_RECOVERABLE = True  # 비밀번호 초기화 기능 켜기/끄기
SECURITY_CHANGEABLE = True # 비밀번호 바꾸기 기능 켜기/끄기
SECURITY_SEND_REGISTER_EMAIL = False  # 회원가입 인증 메일 보내기 기능 켜기/끄기
SECURITY_PASSWORD_HASH = 'bcrypt'  # 비밀번호 암호화 Hash algorithm  설정
SECURITY_PASSWORD_SALT = 'X2LGFS1AI39VRWYCYMXG3L5F4GS8EE35WUB0YSVPX7SUFWP70ETI1G2ZV2LLQGJ8'  # 비밀번호 암호화 SALT 값
SECURITY_URL_PREFIX = ''  # flask-security 뷰 앞에 붙는 URL prefix
SECURITY_POST_LOGIN_VIEW = '/'  # 로그인 후 이동하는 뷰 설정
SECURITY_POST_REGISTER_VIEW = '/' # 회원가입 후 이동하는 뷰 설정

# flask-security 메시지 override
SECURITY_MSG_EMAIL_NOT_PROVIDED =('이메일을 입력해주세요.', 'error')
SECURITY_MSG_UNAUTHORIZED = ('당신은 이 페이지에 접근할 권한이 없습니다.', 'error')
SECURITY_MSG_CONFIRM_REGISTRATION = ('감사합니다. 인증 절차에 관한 안내가 %(email)로 보내졌습니다.', 'success')
SECURITY_MSG_EMAIL_CONFIRMED = ('감사합니다 당신의 이메일이 인증되었습니다.', 'success')
SECURITY_MSG_ALREADY_CONFIRMED= ('당신의 이메일은 이미 인증되었습니다.', 'info')
SECURITY_MSG_INVALID_CONFIRMATION_TOKEN = ('잘못된 인증 토큰입니다.', 'error')
SECURITY_MSG_EMAIL_ALREADY_ASSOCIATED = ('%(email)이 이미 당신에 계정에 연관되어 있습니다.', 'error')
SECURITY_MSG_PASSWORD_MISMATCH = ('비밀번호가 서로 일치하지 않습니다', 'error')
SECURITY_MSG_RETYPE_PASSWORD_MISMATCH = ('비밀번호가 서로 일치하지 않습니다.', 'error')
SECURITY_MSG_INVALID_REDIRECT = ('도메인 바깥으로의 이동은 금지되었습니다.', 'error')
SECURITY_MSG_PASSWORD_RESET_REQUEST = ('비밀번호 초기화에 대한 안내가 %(email)로 보내졌습니다', 'info')
SECURITY_MSG_PASSWORD_RESET_EXPIRED = ('%(within) 내에 비밀번호를 교체하지 않으셔서, 새로운 안내가 %(email)로 보내졌습니다..', 'error')
SECURITY_MSG_INVALID_RESET_PASSWORD_TOKEN = ('잘못된 비밀번호 초기화 토큰입니다..', 'error')
SECURITY_MSG_CONFIRMATION_REQUIRED = ('이메일 인증이 필요합니다.', 'error')
SECURITY_MSG_CONFIRMATION_REQUEST = ('감사합니다. 인증 절차에 관한 안내가 %(email)로 보내졌습니다.', 'info')
SECURITY_MSG_CONFIRMATION_EXPIRED = ('%(within) 시간 내에 이메일은 인증하지 않으셨습니다. 당신의 이메일을 인증하기 위한 '
                                     '새로운 안내가 %(email)로 보내졌습니다', 'error')
SECURITY_MSG_LOGIN_EXPIRED = ('%(within) 동안 로그인하지 않으셨습니다. 로그인을 위한 새로운 안내사항이 %(email)로 보내졌습니다.', 'error')
SECURITY_MSG_LOGIN_EMAIL_SENT = ('로그인을 위한 안내가 %(email)로 보내졌습니다.', 'success')
SECURITY_MSG_INVALID_LOGIN_TOKEN = ('잘못된 로그인 토큰입니다.', 'error')
SECURITY_MSG_DISABLED_ACCOUNT = ('사용할 수 없는 계정입니다.', 'error')
SECURITY_MSG_INVALID_EMAIL_ADDRESS = ('잘못된 이메일 주소입니다', 'error')
SECURITY_MSG_PASSWORD_NOT_PROVIDED = ('비밀번호가 입력되지 않았습니다', 'error')
SECURITY_MSG_PASSWORD_NOT_SET = ('사용자에게 아무 비밀번호도 설정되지 않았습니다', 'error')
SECURITY_MSG_PASSWORD_INVALID_LENGTH = ('비밀번호는 6자리 이상으로 설정하셔야 합니다.', 'error')
SECURITY_MSG_USER_DOES_NOT_EXIST = ('사용자가 존재하지 않습니다.', 'error')
SECURITY_MSG_INVALID_PASSWORD = ('잘못된 비밀번호입니다.', 'error')
SECURITY_MSG_PASSWORDLESS_LOGIN_SUCCESSFUL = ('성공적으로 로그인하셨습니다', 'success')
SECURITY_MSG_PASSWORD_RESET = ('감사합니다. 비밀번호 초기화가 완료되었고, 자동으로 로그인 됩니다.', 'success')
SECURITY_MSG_PASSWORD_IS_THE_SAME = ('당신의 새 비밀번호는 옛날 비밀번호와 달라야 합니다.', 'error')
SECURITY_MSG_PASSWORD_CHANGE = ('비밀번호를 성공적으로 바꾸셨습니다.', 'success')
SECURITY_MSG_LOGIN = ('이 페이지에 접근하시려면 로그인 해주세요.', 'info')
SECURITY_MSG_REFRESH = ('페이지에 접근하기 위해서 재인증해주세요.', 'info')


# Flask-SocialBlueprint social apps ID
# https://github.com/wooyek/flask-social-blueprint
SOCIAL_BLUEPRINT = {
    # https://developers.facebook.com/apps/
    "flask_social_blueprint.providers.Facebook": {
        # App ID
	# localhost testing  App ID
        #'consumer_key': '705027926296962',
	# Server 용 App ID
	'consumer_key': '684002831732805',
        # localhost testing App Secret
	# 'consumer_secret': '17dce6b2f16facdc6f88dff167938c1a'
	# server App secret
	'consumer_secret':'51d173f01a0290682be0af5db48550a6'
    },
    # https://apps.twitter.com/app/new
    "flask_social_blueprint.providers.Twitter": {
        # Your access token from API Keys tab
        'consumer_key': 'Us0qHlRupn9cRr2LgLanZQsCt',
        # access token secret
        'consumer_secret': 'jAm1UZEp4ckJAD9yErbUi7EBk0ayUbMPGwNIb7904Dq8bgROui'
    },
    # https://console.developers.google.com/project
    "flask_social_blueprint.providers.Google": {
        # Client ID
        'consumer_key': '435223545504-bgbqpavf8q157l8u5v2otvfg4khaqgeg.apps.googleusercontent.com',
        # Client secret
        'consumer_secret': '_GH1tElWK9tyk5KdppMZ5w3w'
    },
    # https://github.com/settings/applications/new
    "flask_social_blueprint.providers.Github": {
        # Client ID
        'consumer_key': 'c74d8b2d5b6448db33a5',
        # Client Secret
        'consumer_secret': '5e9e8e889dfe76a20e781a98eb0eb772c5f3ca30'
    },
}
