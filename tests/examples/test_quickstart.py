#!/usr/bin/env python3
"""Compile-only smoke test for examples/quickstart.py."""

import py_compile
from pathlib import Path

EXAMPLE = Path(__file__).resolve().parents[2] / "examples" / "quickstart.py"


def test_quickstart_example_file_exists_on_disk():
    # Arrange
    expected = EXAMPLE
    # Act
    found = expected.is_file()
    # Assert
    assert found, f"missing example: {expected}"


def test_quickstart_example_compiles_without_syntax_error():
    # Arrange
    target = str(EXAMPLE)
    # Act
    result = py_compile.compile(target, doraise=True)
    # Assert
    assert result is not None


# EOF
