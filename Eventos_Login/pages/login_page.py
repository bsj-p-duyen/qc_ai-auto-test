"""Màn hình login: URL, locator, thao tác — theo `docs/Testcase_Login.md`.

Assert nằm ở test; page object chỉ cung cấp locator và hành động UI.
"""

import re
from typing import Any, Dict, Optional

from playwright.sync_api import Locator, Page, Response


class LoginMessages:
    """Chuỗi kỳ vọng (spec / portal) — dùng trong assert phía test."""

    EMAIL_INVALID = "メールアドレスが正しくありません"
    EMAIL_REQUIRED = "メールアドレスを入力してください"
    PASSWORD_REQUIRED = "パスワードを入力してください"
    PASSWORD_LENGTH = "パスワードは8文字以上32文字以下で指定してください"
    LOGIN_FAILED = "ログインできませんでした。入力内容をご確認の上、もう一度お試しください。"


class LoginPage:
    path = "/web/portal/529/event/3988/users/login"
    base_host = "playwright-demo.eventos.work"

    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def url(self) -> str:
        return f"https://{self.base_host}{self.path}"

    @staticmethod
    def url_pattern_demo() -> re.Pattern:
        return re.compile(r"playwright-demo\.eventos\.work")

    @staticmethod
    def url_pattern_login_path() -> re.Pattern:
        return re.compile(r".*/users/login.*")

    @staticmethod
    def url_pattern_register() -> re.Pattern:
        return re.compile(r".*/users/register.*")

    @staticmethod
    def url_pattern_password_reset() -> re.Pattern:
        return re.compile(r".*/users/reset.*")

    def open(self) -> None:
        self.page.goto(self.url, wait_until="networkidle")

    @property
    def body(self) -> Locator:
        return self.page.locator("body")

    @property
    def email_input(self) -> Locator:
        return self.page.locator("#mail_address")

    @property
    def password_input(self) -> Locator:
        return self.page.locator("#password")

    @property
    def login_button(self) -> Locator:
        return self.page.locator("#login_button")

    @property
    def register_button(self) -> Locator:
        return self.page.locator("#register_button")

    @property
    def password_visibility_toggle(self) -> Locator:
        return self.page.get_by_role("button", name="append icon")

    @property
    def forgot_password_control(self) -> Locator:
        return self.page.get_by_text("パスワードを忘れた場合", exact=False)

    def mail_messages(self) -> Locator:
        return self.page.locator("div.v-input:has(#mail_address) .v-messages__message")

    def password_messages(self) -> Locator:
        return self.page.locator("div.v-input:has(#password) .v-messages__message")

    def fill_email(self, value: str) -> None:
        self.email_input.fill(value)

    def fill_password(self, value: str) -> None:
        self.password_input.fill(value)

    def clear_email(self) -> None:
        self.email_input.clear()

    def clear_password(self) -> None:
        self.password_input.clear()

    def blur_active(self) -> None:
        self.page.evaluate(
            "() => { const e = document.activeElement; if (e && e.blur) e.blur(); }"
        )

    def click_login(self) -> None:
        self.login_button.click()

    def click_register(self) -> None:
        self.register_button.click()

    def click_forgot_password(self) -> None:
        self.forgot_password_control.click()

    def toggle_password_visibility(self) -> None:
        self.password_visibility_toggle.click()

    def submit_credentials(self, email: str, password: str) -> None:
        self.fill_email(email)
        self.fill_password(password)
        self.click_login()

    @staticmethod
    def authentication_post_predicate(response: Response) -> bool:
        return (
            response.request.method == "POST"
            and "account_authentication" in response.url
        )

    def expect_authentication_post(self):
        return self.page.expect_response(self.authentication_post_predicate, timeout=30_000)

    @staticmethod
    def parse_auth_json(response: Response) -> Dict[str, Any]:
        return response.json()

    @staticmethod
    def auth_login_failed_message(payload: Dict[str, Any]) -> Optional[str]:
        try:
            for item in payload["error"]["items"]:
                if item.get("key") == "auth_information":
                    msgs = item.get("messages") or []
                    if msgs:
                        return str(msgs[0])
        except (KeyError, TypeError):
            return None
        return None
