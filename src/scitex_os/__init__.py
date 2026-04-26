#!/usr/bin/env python3
"""scitex-os — host check + safe file mv (standalone, pure stdlib)."""

__version__ = "0.1.0"

from ._check_host import check_host, is_host, verify_host
from ._mv import mv

__all__ = [
    "check_host",
    "is_host",
    "mv",
    "verify_host",
]
