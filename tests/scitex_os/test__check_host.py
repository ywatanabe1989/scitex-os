#!/usr/bin/env python3
"""Tests for scitex_os._check_host."""

import socket

import pytest

from scitex_os._check_host import check_host, is_host, verify_host


class TestCheckHost:
    def test_returns_true_when_keyword_in_hostname(self, monkeypatch):
        monkeypatch.setattr(socket, "gethostname", lambda: "ywata-note-win")
        assert check_host("ywata") is True

    def test_returns_false_when_keyword_absent(self, monkeypatch):
        monkeypatch.setattr(socket, "gethostname", lambda: "ywata-note-win")
        assert check_host("nope") is False

    def test_is_host_is_alias(self):
        assert is_host is check_host


class TestVerifyHost:
    def test_returns_none_on_match(self, monkeypatch, capsys):
        monkeypatch.setattr(socket, "gethostname", lambda: "ywata-note-win")
        assert verify_host("ywata") is None
        assert "successed" in capsys.readouterr().out

    def test_sys_exits_on_mismatch(self, monkeypatch, capsys):
        monkeypatch.setattr(socket, "gethostname", lambda: "ywata-note-win")
        with pytest.raises(SystemExit) as exc:
            verify_host("nope")
        assert exc.value.code == 1
        assert "failed" in capsys.readouterr().out
