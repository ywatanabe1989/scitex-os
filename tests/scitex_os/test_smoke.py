"""Smoke tests for scitex-os."""

import socket

import pytest

import scitex_os as sxos


def test_exports():
    for name in ("check_host", "is_host", "verify_host", "mv"):
        assert callable(getattr(sxos, name)), name


def test_is_host_self():
    assert sxos.is_host(socket.gethostname()) is True


def test_is_host_negative():
    assert sxos.is_host("not-a-real-host-1234567890") is False


def test_check_host_returns_bool():
    out = sxos.check_host(socket.gethostname())
    assert isinstance(out, bool)
    assert out is True


def test_verify_host_passes_for_self():
    sxos.verify_host(socket.gethostname())


def test_verify_host_raises_for_other():
    with pytest.raises((AssertionError, SystemExit, RuntimeError, Exception)):
        sxos.verify_host("not-a-real-host-1234567890")


def test_mv_moves_file(tmp_path):
    src = tmp_path / "src.txt"
    dst = tmp_path / "dst"
    src.write_text("hi")
    sxos.mv(str(src), str(dst))
    assert (dst / "src.txt").exists()
    assert not src.exists()
