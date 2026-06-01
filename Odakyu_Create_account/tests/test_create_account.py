import re

import pytest
from playwright.sync_api import Browser, Page, expect

from pages.create_account import login_email, login_password


# =============================
# Open Create Account Screen
# =============================
def goto_create_account_screen(page: Page) -> None:
    page.goto("https://admin.odakyu.bravesoft.vn/login")
    page.locator('input[name="email"]').fill(login_email())
    page.locator('input[name="password"]').fill(login_password())
    page.get_by_role("button", name="ログイン").click()
    expect(page).to_have_url(re.compile(r".*/account-management(?:/|\\?|$)"))
    page.locator("button.common-submit-btn.primary").click()
    expect(page.locator(".modify-account-modal")).to_be_visible() 


@pytest.fixture(scope="module")
def create_account_page(browser: Browser):
    context = browser.new_context()
    page = context.new_page()
    goto_create_account_screen(page)
    yield page
    context.close()

# =============================
# TEST CASES
# =============================
def test_create_account_1(create_account_page: Page) -> None:
    expect(create_account_page.locator(".title-confirm")).to_have_text("新規アカウント追加")


def test_create_account_3(create_account_page: Page) -> None:
    assert "/account-management" in create_account_page.url

def test_create_account_4(create_account_page: Page) -> None:
    expect(
        create_account_page.get_by_text(
            re.compile(r"アカウント名\s*\*\s*（255文字以内）")
        )
    ).to_be_visible()

def test_create_account_5(create_account_page: Page) -> None:
    # Trên màn có 2 chỗ "メールアドレス" (cột bảng + nhãn form). Nhãn form có dấu *.
    expect(
        create_account_page.locator(".modify-account-modal").get_by_text(
            re.compile(r"メールアドレス\s*\*")
        )
    ).to_be_visible()

def test_create_account_7(create_account_page: Page) -> None:
    create_account_page.locator('.modify-account-modal input[name="email"]').fill("trucly@bravesoft-vn.com.vn")
    expect(create_account_page.locator('.modify-account-modal input[name="email"]')).to_have_value("trucly@bravesoft-vn.com.vn")


def test_create_account_8(create_account_page: Page) -> None:
    expect(
        create_account_page.get_by_text(
            re.compile(r"パスワード\s*\*\s*（半角英数字 8文字以上32文字以内）")
        )
    ).to_be_visible()

def test_create_account_9(create_account_page: Page) -> None:
    expect(create_account_page.locator(".modify-account-modal").get_by_placeholder("**********")).to_be_visible()

def test_create_account_10(create_account_page: Page) -> None:
    create_account_page.get_by_placeholder("**********").fill("パスワード")
    expect(create_account_page.get_by_placeholder("**********")).to_have_value("*****")

def test_create_account_11(create_account_page: Page) -> None:
    create_account_page.locator('.modify-account-modal input[name="password"]').fill("12345678")