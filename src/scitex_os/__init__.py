#!/usr/bin/env python3
"""scitex-os — host check + safe file mv (standalone, pure stdlib)."""

try:
    from importlib.metadata import version as _v, PackageNotFoundError
    try:
        __version__ = _v("scitex-os")
    except PackageNotFoundError:
        __version__ = "0.0.0+local"
    del _v, PackageNotFoundError
except ImportError:  # pragma: no cover — only on ancient Pythons
    __version__ = "0.0.0+local"
from ._check_host import check_host, is_host, verify_host
from ._mv import mv

__all__ = [
    "check_host",
    "is_host",
    "mv",
    "verify_host",
]
