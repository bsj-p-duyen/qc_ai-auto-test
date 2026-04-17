"""Pytest hooks: ảnh màn hình khi test fail (fixture `page` từ pytest-playwright)."""

from __future__ import annotations

import re
from pathlib import Path


def _screenshot_dir() -> Path:
    return Path(__file__).resolve().parent.parent / "reports" / "screenshots"


def _safe_stem(nodeid: str) -> str:
    stem = re.sub(r"[^\w\-.]+", "_", nodeid)
    return stem[:200] if len(stem) > 200 else stem


def pytest_exception_interact(node, call, report):
    """Chụp full page trước khi teardown — `page` vẫn mở."""
    if call.when != "call":
        return
    page = getattr(node, "funcargs", {}).get("page")
    if page is None:
        return
    try:
        dest = _screenshot_dir()
        dest.mkdir(parents=True, exist_ok=True)
        path = dest / f"{_safe_stem(node.nodeid)}.png"
        page.screenshot(path=str(path), full_page=True)
    except Exception:
        pass
