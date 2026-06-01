from playwright.sync_api import Dialog, Page, expect


BASE_URL = "https://bsv-nhungnguyen.github.io/"


def open_home(page: Page) -> None:
    page.goto(BASE_URL)
    expect(page.get_by_text("Playwright test 08.05.2026")).to_be_visible()


def click_load_nested_frames(page: Page) -> None:
    page.get_by_role("button", name="Load Nested Frames").click()


def open_modal(page: Page) -> None:
    page.get_by_role("button", name="Open In-page Modal").click()
    expect(page.get_by_text("Secure Confirmation")).to_be_visible()


def open_hooks_demo_logged_in(page: Page) -> None:
    expect(page.get_by_text("Hooks Demo")).to_be_visible()
    page.locator("input").nth(0).fill("admin")
    page.locator("input").nth(1).fill("password123")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Logged in as")).to_be_visible()


def trigger_dialog_and_handle(
    page: Page, trigger_button_name: str, action: str = "accept", prompt_text: str = ""
) -> str:
    dialog_message = {"value": ""}

    def on_dialog(dialog: Dialog) -> None:
        dialog_message["value"] = dialog.message
        if action == "accept":
            dialog.accept(prompt_text)
        else:
            dialog.dismiss()

    page.once("dialog", on_dialog)
    page.get_by_role("button", name=trigger_button_name).click()
    return dialog_message["value"]
