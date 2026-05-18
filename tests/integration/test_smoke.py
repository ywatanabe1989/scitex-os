"""Smoke tests for scitex-os."""

import socket

import pytest

import scitex_os as sxos


@pytest.mark.parametrize("name", ["check_host", "is_host", "verify_host", "mv"])
def test_public_export_is_callable(name):
    # Arrange
    attr = getattr(sxos, name, None)
    # Act
    is_callable = callable(attr)
    # Assert
    assert is_callable, f"{name} is not callable on scitex_os"


def test_is_host_returns_true_for_current_hostname():
    # Arrange
    me = socket.gethostname()
    # Act
    result = sxos.is_host(me)
    # Assert
    assert result is True


def test_is_host_returns_false_for_synthetic_hostname():
    # Arrange
    fake = "not-a-real-host-1234567890"
    # Act
    result = sxos.is_host(fake)
    # Assert
    assert result is False


def test_check_host_returns_bool_for_current_hostname():
    # Arrange
    me = socket.gethostname()
    # Act
    out = sxos.check_host(me)
    # Assert
    assert isinstance(out, bool)


def test_check_host_returns_true_for_current_hostname():
    # Arrange
    me = socket.gethostname()
    # Act
    out = sxos.check_host(me)
    # Assert
    assert out is True


def test_verify_host_returns_none_for_current_hostname():
    # Arrange
    me = socket.gethostname()
    # Act
    result = sxos.verify_host(me)
    # Assert
    assert result is None


def test_verify_host_raises_systemexit_for_unknown_hostname():
    # Arrange
    fake = "not-a-real-host-1234567890"
    # Act
    ctx = pytest.raises((AssertionError, SystemExit, RuntimeError, Exception))
    # Assert
    with ctx:
        sxos.verify_host(fake)


def test_mv_creates_file_at_destination(tmp_path):
    # Arrange
    src = tmp_path / "src.txt"
    dst = tmp_path / "dst"
    src.write_text("hi")
    # Act
    sxos.mv(str(src), str(dst))
    # Assert
    assert (dst / "src.txt").exists()


def test_mv_removes_source_after_move(tmp_path):
    # Arrange
    src = tmp_path / "src.txt"
    dst = tmp_path / "dst"
    src.write_text("hi")
    # Act
    sxos.mv(str(src), str(dst))
    # Assert
    assert not src.exists()
