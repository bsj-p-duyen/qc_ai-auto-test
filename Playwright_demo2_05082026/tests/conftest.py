"""Fixture chung + chup hinh evidence khi testcase fail."""

from __future__ import annotations

import re
from pathlib import Path

import pytest
from playwright.sync_api import Browser, Page

from arena_helpers import open_home


def _screenshot_dir() -> Path:
    return Path(__file__).resolve().parent.parent / "reports" / "screenshots"


def _safe_stem(nodeid: str) -> str:
    stem = re.sub(r"[^\w\-.]+", "_", nodeid)
    return stem[:200] if len(stem) > 200 else stem


def save_failure_screenshot(node, page: Page) -> None:
    dest = _screenshot_dir()
    dest.mkdir(parents=True, exist_ok=True)
    path = dest / f"{_safe_stem(node.nodeid)}.png"
    page.screenshot(path=str(path), full_page=True)
    print(f"\n[EVIDENCE] Da luu screenshot fail: {path}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture()
def simple_page(browser: Browser, request) -> Page:
    context = browser.new_context()
    page = context.new_page()
    open_home(page)
    yield page

    report = getattr(request.node, "rep_call", None)
    if report is not None and report.failed:
        try:
            save_failure_screenshot(request.node, page)
        except Exception as exc:
            print(f"\n[EVIDENCE] Khong chup duoc screenshot: {exc}")

    context.close()
