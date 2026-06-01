from pathlib import Path

import pytest
from playwright.sync_api import Browser, Page, expect

from arena_helpers import open_home, open_hooks_demo_logged_in


# =============================
# Visuals, Video, Tracing (TC 018 -> 026)
# =============================
def testcase018(simple_page: Page, tmp_path: Path) -> None:
    simple_page.get_by_role("button", name="Normal State").click()
    expect(simple_page.get_by_text("System Normal")).to_be_visible()
    image_file = tmp_path / "full-page.png"
    simple_page.screenshot(path=str(image_file), full_page=True)
    assert image_file.exists()


def testcase019(simple_page: Page, tmp_path: Path) -> None:
    simple_page.get_by_role("button", name="Normal State").click()
    expect(simple_page.get_by_text("System Normal")).to_be_visible()
    assert len(list(tmp_path.iterdir())) == 0


def testcase020(simple_page: Page, tmp_path: Path) -> None:
    simple_page.get_by_role("button", name="Failure State").click()
    element_file = tmp_path / "failed-element.png"
    try:
        expect(simple_page.get_by_text("System Normal")).to_be_visible(timeout=1000)
    except Exception:
        simple_page.locator("#screenshot-element").screenshot(path=str(element_file))
    assert element_file.exists()


def testcase021(browser: Browser, tmp_path: Path) -> None:
    context = browser.new_context(record_video_dir=str(tmp_path))
    page = context.new_page()
    open_home(page)
    page.get_by_role("button", name="Play Sequence").click()
    expect(page.get_by_text("Sequence complete!")).to_be_visible(timeout=15000)
    page.close()
    context.close()
    assert len(list(tmp_path.glob("*.webm"))) > 0


@pytest.mark.skip(reason="TC-022/023 canh bao: can setup retain-on-failure bang pytest options.")
def testcase022() -> None:
    pass


@pytest.mark.skip(reason="TC-022/023 canh bao: can setup retain-on-failure bang pytest options.")
def testcase023() -> None:
    pass


def testcase024(browser: Browser, tmp_path: Path) -> None:
    trace_file = tmp_path / "trace-always.zip"
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    open_home(page)
    page.locator("input").nth(0).fill("name 1")
    page.locator("input").nth(1).fill("value 1")
    page.get_by_role("button", name="Submit Form").click()
    expect(page.get_by_text("Submitted:")).to_be_visible()
    context.tracing.stop(path=str(trace_file))
    context.close()
    assert trace_file.exists()


def testcase025(browser: Browser, tmp_path: Path) -> None:
    trace_file = tmp_path / "trace-on-fail.zip"
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    open_home(page)
    try:
        page.get_by_role("button", name="Submit Form").click()
        expect(page.get_by_text("Submitted: success")).to_be_visible(timeout=1000)
    except Exception:
        context.tracing.stop(path=str(trace_file))
    finally:
        context.close()
    assert trace_file.exists()


def testcase026(tmp_path: Path) -> None:
    assert len(list(tmp_path.glob("*.zip"))) == 0


# =============================
# Hooks Demo (TC 027 -> 030)
# =============================
@pytest.mark.skip(reason="TC-027/028 la hook-level check tren terminal, khong phai UI assert truc tiep.")
def testcase027() -> None:
    pass


@pytest.mark.skip(reason="TC-027/028 la hook-level check tren terminal, khong phai UI assert truc tiep.")
def testcase028() -> None:
    pass


def testcase029(simple_page: Page) -> None:
    open_hooks_demo_logged_in(simple_page)
    simple_page.locator("input").nth(2).fill("record-auto-1")
    simple_page.get_by_role("button", name="Create Record").click()
    expect(simple_page.get_by_text("record-auto-1")).to_be_visible()


def testcase030(simple_page: Page) -> None:
    open_hooks_demo_logged_in(simple_page)
    simple_page.locator("input").nth(2).fill("record-auto-delete")
    simple_page.get_by_role("button", name="Create Record").click()
    expect(simple_page.get_by_text("record-auto-delete")).to_be_visible()
    simple_page.get_by_role("button", name="Delete").first.click()
    expect(simple_page.get_by_text("record-auto-delete")).to_have_count(0)
