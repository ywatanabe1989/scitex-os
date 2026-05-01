#!/usr/bin/env python3
"""Tests for scitex_os._mv.mv."""

import pytest

from scitex_os._mv import mv


class TestMv:
    def test_moves_file_to_existing_dir(self, tmp_path, capsys):
        src = tmp_path / "a.txt"
        src.write_text("hello")
        dst_dir = tmp_path / "dst"
        dst_dir.mkdir()
        ok = mv(str(src), str(dst_dir))
        assert ok is True
        assert not src.exists()
        assert (dst_dir / "a.txt").read_text() == "hello"

    def test_creates_destination_dir_when_missing(self, tmp_path):
        src = tmp_path / "b.txt"
        src.write_text("data")
        dst_dir = tmp_path / "new" / "deep"
        ok = mv(str(src), str(dst_dir))
        assert ok is True
        assert dst_dir.is_dir()
        assert (dst_dir / "b.txt").exists()

    def test_move_directory(self, tmp_path):
        src = tmp_path / "src_dir"
        src.mkdir()
        (src / "inner.txt").write_text("x")
        dst = tmp_path / "dst"
        dst.mkdir()
        ok = mv(str(src), str(dst))
        assert ok is True
        assert (dst / "src_dir" / "inner.txt").read_text() == "x"

    def test_returns_false_on_oserror(self, tmp_path, monkeypatch):
        # Simulate shutil.move raising OSError.
        import shutil

        def boom(*a, **kw):
            raise OSError("simulated")

        monkeypatch.setattr(shutil, "move", boom)
        ok = mv(str(tmp_path / "missing"), str(tmp_path / "dst"))
        assert ok is False


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__), "-v"])

# EOF
