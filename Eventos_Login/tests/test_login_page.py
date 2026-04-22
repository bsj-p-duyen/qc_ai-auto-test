"""Playwright + pytest — map `docs/Testcase_Login.md` (ログイン-1, 3–31).

POM: `pages/login_page.py`, `pages/login_credentials.py`.
"""

import pytest
from playwright.sync_api import Page, expect

from pages.login_credentials import login_email, login_password
from pages.login_page import LoginMessages, LoginPage


@pytest.fixture
def login(page: Page) -> LoginPage:
    p = LoginPage(page)
    p.open()
    return p


# --- ログイン-1 ---


def test_tc_log_01_url_contains_login(login: LoginPage, page: Page) -> None:
    """ログイン-1: URL hiển thị chứa /login (portal: …/users/login)."""
    expect(page).to_have_url(LoginPage.url_pattern_demo())
    expect(page).to_have_url(LoginPage.url_pattern_login_path())


# --- ログイン-3 ---


def test_tc_log_03_register_navigates(login: LoginPage, page: Page) -> None:
    """ログイン-3: 新規登録 → 新規登録画面."""
    login.click_register()
    expect(page).to_have_url(LoginPage.url_pattern_register())


# --- ログイン-4 ---


def test_tc_log_04_email_label_and_field(login: LoginPage, page: Page) -> None:
    """ログイン-4: ラベル「メールアドレス」+ textbox."""
    expect(page.get_by_text("メールアドレス").first).to_be_visible()
    expect(login.email_input).to_be_visible()


# --- ログイン-5 ---


def test_tc_log_05_email_input_lowercase(login: LoginPage) -> None:
    """ログイン-5: nhập abc@gmail.com hiển thị đúng."""
    login.fill_email("abc@gmail.com")
    expect(login.email_input).to_have_value("abc@gmail.com")


# --- ログイン-6 ---


def test_tc_log_06_email_preserves_case(login: LoginPage) -> None:
    """ログイン-6: nhập ABC@GMAIL.COM giữ nguyên chữ hoa."""
    login.fill_email("ABC@GMAIL.COM")
    expect(login.email_input).to_have_value("ABC@GMAIL.COM")


# --- ログイン-7 ～ 10 (param) ---


@pytest.mark.parametrize(
    "invalid_email",
    [
        "abc@gmail",
        "abc!@gmail.com",
        "test.abc",
        "@gmail.com",
    ],
)
def test_tc_log_07_to_10_invalid_email_format(
    login: LoginPage, invalid_email: str
) -> None:
    """ログイン-7 ～ 10: email sai định dạng → メールアドレスが正しくありません。"""
    login.fill_email(invalid_email)
    login.fill_password("12345678")
    login.blur_active()
    expect(login.mail_messages().first).to_contain_text(LoginMessages.EMAIL_INVALID)


# --- ログイン-11 ---


def test_tc_log_11_fullwidth_email_invalid(login: LoginPage) -> None:
    """ログイン-11: 全角 → メールアドレスが正しくありません。"""
    login.fill_email("ｔｅｓｔ＠ｇｍａｉｌ．ｃｏｍ")
    login.blur_active()
    expect(login.mail_messages().first).to_contain_text(LoginMessages.EMAIL_INVALID)


# --- ログイン-12 ---


def test_tc_log_12_clear_email_shows_required(login: LoginPage) -> None:
    """ログイン-12: xóa hết nội dung mail → メールアドレスを入力してください。"""
    login.fill_email("a@b.co")
    login.clear_email()
    login.blur_active()
    expect(login.mail_messages().first).to_contain_text(LoginMessages.EMAIL_REQUIRED)


# --- ログイン-13 ---


def test_tc_log_13_password_field_and_toggle_visible(login: LoginPage, page: Page) -> None:
    """ログイン-13: パスワード + textbox + icon (visibility)."""
    expect(page.get_by_text("パスワード").first).to_be_visible()
    expect(login.password_input).to_be_visible()
    expect(login.password_visibility_toggle).to_be_visible()


# --- ログイン-14 ---


def test_tc_log_14_password_masked_and_value_set(login: LoginPage) -> None:
    """ログイン-14: nhập password, type=password (mask)."""
    login.fill_password("secret123")
    expect(login.password_input).to_have_attribute("type", "password")
    expect(login.password_input).to_have_value("secret123")


# --- ログイン-15 ---


def test_tc_log_15_toggle_shows_plain_password(login: LoginPage) -> None:
    """ログイン-15: bấm icon → hiện plain text."""
    login.fill_password("secret123")
    login.toggle_password_visibility()
    expect(login.password_input).to_have_attribute("type", "text")


# --- ログイン-16 ---


def test_tc_log_16_toggle_hides_password_again(login: LoginPage) -> None:
    """ログイン-16: bấm lại icon → mask."""
    login.fill_password("secret123")
    login.toggle_password_visibility()
    login.toggle_password_visibility()
    expect(login.password_input).to_have_attribute("type", "password")


# --- ログイン-17 ---


def test_tc_log_17_empty_password_message(login: LoginPage) -> None:
    """ログイン-17: không nhập password → パスワードを入力してください。"""
    login.fill_email("a@b.co")
    login.clear_password()
    login.blur_active()
    expect(login.password_messages().first).to_contain_text(LoginMessages.PASSWORD_REQUIRED)


# --- ログイン-18 ---


def test_tc_log_18_password_too_short(login: LoginPage) -> None:
    """ログイン-18: ≤8 ký tự (7) → パスワードは8文字以上…"""
    login.fill_email(login_email())
    login.fill_password("1234567")
    login.blur_active()
    expect(login.password_messages().first).to_contain_text(LoginMessages.PASSWORD_LENGTH)


# --- ログイン-19 ---


def test_tc_log_19_password_too_long(login: LoginPage) -> None:
    """ログイン-19: ≥32 ký tự → パスワードは8文字以上…"""
    login.fill_email(login_email())
    login.fill_password("x" * 33)
    login.blur_active()
    expect(login.password_messages().first).to_contain_text(LoginMessages.PASSWORD_LENGTH)


# --- ログイン-20 ～ 25 ---


@pytest.mark.parametrize(
    "password_sample",
    [
        "12345678",
        "AbCdEfGh",
        "!@#$%^&*",
        "1234AbCd",
        "1234!@#$",
        "AbCd!@#$",
    ],
)
def test_tc_log_20_to_25_password_patterns_no_length_error(
    login: LoginPage, password_sample: str
) -> None:
    """ログイン-20 ～ 25: đủ 8 ký tự đúng rule độ dài → không báo lỗi độ dài password."""
    login.fill_email(login_email())
    login.fill_password(password_sample)
    login.blur_active()
    expect(login.password_messages()).to_have_count(0)


# --- ログイン-26 ---


def test_tc_log_26_login_button_visible(login: LoginPage) -> None:
    """ログイン-26: nút ログイン hiển thị (spec: ban đầu 非活性 — portal có thể vẫn clickable)."""
    expect(login.login_button).to_be_visible()
    expect(login.login_button).to_contain_text("ログイン")


# --- ログイン-27 ---


def test_tc_log_27_wrong_password_api_message(login: LoginPage, page: Page) -> None:
    """ログイン-27: đúng mail đăng ký + sai pass → không đăng nhập + message API."""
    login.fill_email(login_email())
    login.fill_password("definitely_wrong_password_123")
    with login.expect_authentication_post() as resp_info:
        login.click_login()
    resp = resp_info.value
    assert resp.status == 422
    payload = LoginPage.parse_auth_json(resp)
    msg = LoginPage.auth_login_failed_message(payload)
    assert msg is not None
    assert LoginMessages.LOGIN_FAILED in msg
    expect(page).to_have_url(LoginPage.url_pattern_login_path())


# --- ログイン-28 ---


def test_tc_log_28_unregistered_email_api_message(login: LoginPage, page: Page) -> None:
    """ログイン-28: mail chưa đăng ký + pass đúng format → 422 + cùng message nghiệp vụ."""
    login.fill_email("not_registered_eventos_3988@example.com")
    login.fill_password(login_password())
    with login.expect_authentication_post() as resp_info:
        login.click_login()
    resp = resp_info.value
    assert resp.status == 422
    payload = LoginPage.parse_auth_json(resp)
    msg = LoginPage.auth_login_failed_message(payload)
    assert msg is not None
    assert LoginMessages.LOGIN_FAILED in msg
    expect(page).to_have_url(LoginPage.url_pattern_login_path())


# --- ログイン-29 ---


def test_tc_log_29_successful_login(login: LoginPage, page: Page) -> None:
    """ログイン-29: đúng mail + đúng pass → API 200 và rời màn /users/login."""
    login.fill_email(login_email())
    login.fill_password(login_password())
    with login.expect_authentication_post() as resp_info:
        login.click_login()
    resp = resp_info.value
    snippet = ""
    try:
        snippet = resp.text()[:800]
    except Exception:
        snippet = "(không đọc được body)"
    assert resp.status == 200, (
        f"ログイン-29: account_authentication mong HTTP 200, thực tế {resp.status}. "
        "Kiểm tra user có quyền portal 529/event/3988 hoặc LOGIN_EMAIL / LOGIN_PASSWORD. "
        f"Body (rút gọn): {snippet}"
    )
    expect(page).not_to_have_url(LoginPage.url_pattern_login_path(), timeout=20_000)


# --- ログイン-30 ---


def test_tc_log_30_forgot_password_link_visible(login: LoginPage) -> None:
    """ログイン-30: link パスワードを忘れた場合 hiển thị (gạch chân thường gắn với CSS)."""
    expect(login.forgot_password_control).to_be_visible()


# --- ログイン-31 ---


def test_tc_log_31_forgot_password_navigates(login: LoginPage, page: Page) -> None:
    """ログイン-31: パスワードを忘れた場合 → màn reset."""
    login.click_forgot_password()
    expect(page).to_have_url(LoginPage.url_pattern_password_reset())
