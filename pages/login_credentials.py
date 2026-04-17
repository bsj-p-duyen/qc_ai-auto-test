"""Thông tin đăng nhập dùng cho automation — ưu tiên biến môi trường."""

import os

# Mặc định theo yêu cầu; override: LOGIN_EMAIL, LOGIN_PASSWORD
DEFAULT_LOGIN_EMAIL = "kimtran@bravesoft.com.vn"
DEFAULT_LOGIN_PASSWORD = "brave0404"


def login_email() -> str:
    return os.environ.get("LOGIN_EMAIL", DEFAULT_LOGIN_EMAIL)


def login_password() -> str:
    return os.environ.get("LOGIN_PASSWORD", DEFAULT_LOGIN_PASSWORD)
