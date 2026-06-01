from playwright.sync_api import Page, expect

from arena_helpers import (
    click_load_nested_frames,
    open_modal,
    trigger_dialog_and_handle,
)


# =============================
# Frames & Iframes (TC 001 -> 005)
# =============================
def testcase001(simple_page: Page) -> None:
    frame = simple_page.frame_locator("iframe").first
    frame.locator("input").first.fill("Duyên")
    frame.get_by_role("button", name="Submit").click()
    expect(frame.get_by_text("Success: Hello Duyên!")).to_be_visible()


def testcase002(simple_page: Page) -> None:
    click_load_nested_frames(simple_page)
    frame_a = simple_page.frame_locator("iframe").nth(1)
    expect(frame_a.get_by_text("Iframe A")).to_be_visible()
    expect(frame_a.get_by_role("button", name="Open Iframe B")).to_be_visible()


def testcase003(simple_page: Page) -> None:
    click_load_nested_frames(simple_page)
    frame_a = simple_page.frame_locator("iframe").nth(1)
    frame_a.get_by_role("button", name="Open Iframe B").click()
    frame_b = simple_page.frame_locator("iframe").nth(2)
    expect(frame_b.get_by_text("Iframe B")).to_be_visible()


def testcase004(simple_page: Page) -> None:
    click_load_nested_frames(simple_page)
    frame_a = simple_page.frame_locator("iframe").nth(1)
    frame_a.get_by_role("button", name="Open Iframe B").click()
    frame_b = simple_page.frame_locator("iframe").nth(2)
    frame_b.get_by_role("button", name="Open Iframe C").click()
    frame_c = simple_page.frame_locator("iframe").nth(3)
    expect(frame_c.get_by_text("Iframe C")).to_be_visible()


def testcase005(simple_page: Page) -> None:
    click_load_nested_frames(simple_page)
    frame_a = simple_page.frame_locator("iframe").nth(1)
    frame_a.get_by_role("button", name="Open Iframe B").click()
    frame_b = simple_page.frame_locator("iframe").nth(2)
    frame_b.get_by_role("button", name="Open Iframe C").click()
    frame_c = simple_page.frame_locator("iframe").nth(3)
    frame_c.get_by_role("button", name="Click button").click()
    expect(frame_c.get_by_text("Iframe C Clicked!")).to_be_visible()


# =============================
# Windows, Popup, Modal (TC 006 -> 010)
# =============================
def testcase006(simple_page: Page) -> None:
    with simple_page.context.expect_page() as new_page_info:
        simple_page.get_by_role("button", name="Open New Tab").click()
    new_tab = new_page_info.value
    new_tab.wait_for_load_state("domcontentloaded")
    new_tab.get_by_role("link", name="Get started").click()
    expect(new_tab.get_by_text("Installation")).to_be_visible()


def testcase007(simple_page: Page) -> None:
    with simple_page.context.expect_page() as popup_info:
        simple_page.get_by_role("button", name="Open Popup Window").click()
    popup = popup_info.value
    popup.wait_for_load_state("domcontentloaded")
    expect(popup.get_by_text("Popup Activated")).to_be_visible()


def testcase008(simple_page: Page) -> None:
    open_modal(simple_page)
    expect(simple_page.get_by_text("Secure Confirmation")).to_be_visible()


def testcase009(simple_page: Page) -> None:
    open_modal(simple_page)
    simple_page.locator("input").last.fill("123456")
    simple_page.get_by_role("button", name="Confirm").click()
    expect(simple_page.get_by_text("Verified: 123456")).to_be_visible()


def testcase010(simple_page: Page) -> None:
    open_modal(simple_page)
    simple_page.locator("input").last.fill("cancel-code")
    simple_page.get_by_role("button", name="Cancel").click()
    expect(simple_page.get_by_text("Verified: cancel-code")).to_have_count(0)


# =============================
# Native Dialogs (TC 011 -> 017)
# =============================
def testcase011(simple_page: Page) -> None:
    message = trigger_dialog_and_handle(simple_page, "Trigger Alert", "accept")
    assert message == "This is a browser alert!"


def testcase012(simple_page: Page) -> None:
    trigger_dialog_and_handle(simple_page, "Trigger Alert", "accept")
    expect(simple_page.get_by_text("Trigger Alert")).to_be_visible()


def testcase013(simple_page: Page) -> None:
    message = trigger_dialog_and_handle(simple_page, "Trigger Confirm", "accept")
    assert message == "Continue?"


def testcase014(simple_page: Page) -> None:
    trigger_dialog_and_handle(simple_page, "Trigger Confirm", "accept")
    expect(simple_page.get_by_text("Confirmed")).to_be_visible()


def testcase015(simple_page: Page) -> None:
    trigger_dialog_and_handle(simple_page, "Trigger Confirm", "dismiss")
    expect(simple_page.get_by_text("Cancelled")).to_be_visible()


def testcase016(simple_page: Page) -> None:
    trigger_dialog_and_handle(simple_page, "Trigger Prompt", "accept", "hello prompt")
    expect(simple_page.get_by_text("hello prompt")).to_be_visible()


def testcase017(simple_page: Page) -> None:
    trigger_dialog_and_handle(simple_page, "Trigger Prompt", "dismiss")
    expect(simple_page.get_by_text("Dismissed")).to_be_visible()
