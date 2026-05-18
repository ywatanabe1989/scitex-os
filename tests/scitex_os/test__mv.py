#!/usr/bin/env python3
"""Tests for scitex_os._mv.mv.

PA-306: no `monkeypatch`. ``shutil.move`` is swapped via a
``swap_shutil_move`` fixture that records the real callable and
restores it on teardown.

TQ cleanup: every test follows Arrange / Act / Assert with a single
assertion. Multi-fact scenarios are split into sibling tests sharing
a fixture so the failing-line tells you which contract regressed.
"""

import shutil
from typing import Any, Callable

import pytest

from scitex_os._mv import mv

# ---------------------------------------------------------------------------
# swap_shutil_move fixture (replaces monkeypatch.setattr(shutil, ...))
# ---------------------------------------------------------------------------


@pytest.fixture
def swap_shutil_move():
    """Yield a setter that swaps ``shutil.move`` and auto-restores."""
    saved: list[Callable[..., Any]] = [shutil.move]

    def _set(fn: Callable[..., Any]) -> None:
        shutil.move = fn  # type: ignore[assignment]

    try:
        yield _set
    finally:
        shutil.move = saved[0]  # type: ignore[assignment]


# ---------------------------------------------------------------------------
# mv — move a file into an existing destination directory
# ---------------------------------------------------------------------------


class TestMvFileIntoExistingDir:
    @pytest.fixture
    def _moved(self, tmp_path):
        # Arrange
        src = tmp_path / "a.txt"
        src.write_text("hello")
        dst_dir = tmp_path / "dst"
        dst_dir.mkdir()
        # Act
        ok = mv(str(src), str(dst_dir))
        return ok, src, dst_dir

    def test_returns_true_on_successful_move(self, _moved):
        # Arrange
        ok, _src, _dst_dir = _moved
        # Act
        result = ok
        # Assert
        assert result is True

    def test_source_path_no_longer_exists_after_move(self, _moved):
        # Arrange
        _ok, src, _dst_dir = _moved
        # Act
        still_there = src.exists()
        # Assert
        assert still_there is False

    def test_destination_file_holds_original_contents(self, _moved):
        # Arrange
        _ok, _src, dst_dir = _moved
        # Act
        contents = (dst_dir / "a.txt").read_text()
        # Assert
        assert contents == "hello"


# ---------------------------------------------------------------------------
# mv — auto-creates a missing destination directory
# ---------------------------------------------------------------------------


class TestMvCreatesDestinationDir:
    @pytest.fixture
    def _moved(self, tmp_path):
        # Arrange
        src = tmp_path / "b.txt"
        src.write_text("data")
        dst_dir = tmp_path / "new" / "deep"
        # Act
        ok = mv(str(src), str(dst_dir))
        return ok, dst_dir

    def test_returns_true_when_destination_dir_did_not_exist(self, _moved):
        # Arrange
        ok, _dst_dir = _moved
        # Act
        result = ok
        # Assert
        assert result is True

    def test_destination_directory_is_created_on_demand(self, _moved):
        # Arrange
        _ok, dst_dir = _moved
        # Act
        is_dir = dst_dir.is_dir()
        # Assert
        assert is_dir is True

    def test_moved_file_lands_inside_new_destination_directory(self, _moved):
        # Arrange
        _ok, dst_dir = _moved
        # Act
        landed = (dst_dir / "b.txt").exists()
        # Assert
        assert landed is True


# ---------------------------------------------------------------------------
# mv — moving a directory tree
# ---------------------------------------------------------------------------


class TestMvDirectoryTree:
    @pytest.fixture
    def _moved(self, tmp_path):
        # Arrange
        src = tmp_path / "src_dir"
        src.mkdir()
        (src / "inner.txt").write_text("x")
        dst = tmp_path / "dst"
        dst.mkdir()
        # Act
        ok = mv(str(src), str(dst))
        return ok, dst

    def test_returns_true_when_directory_move_succeeds(self, _moved):
        # Arrange
        ok, _dst = _moved
        # Act
        result = ok
        # Assert
        assert result is True

    def test_inner_file_is_preserved_under_destination(self, _moved):
        # Arrange
        _ok, dst = _moved
        # Act
        inner = (dst / "src_dir" / "inner.txt").read_text()
        # Assert
        assert inner == "x"


# ---------------------------------------------------------------------------
# mv — error path: shutil.move raises OSError
# ---------------------------------------------------------------------------


class TestMvOserrorPath:
    def test_returns_false_when_shutil_move_raises_oserror(
        self, tmp_path, swap_shutil_move
    ):
        # Arrange
        def boom(*args, **kwargs):
            raise OSError("simulated")

        swap_shutil_move(boom)
        # Act
        ok = mv(str(tmp_path / "missing"), str(tmp_path / "dst"))
        # Assert
        assert ok is False


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__), "-v"])

# EOF
