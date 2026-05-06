---
description: |
  [TOPIC] Public Python API of scitex-os
  [DETAILS] Host-check trio (`check_host`, `is_host`, `verify_host`) and the path-aware safe `mv`.
tags: [scitex-os-python-api]
---

# Python API

```python
import scitex_os
```

## `check_host(name: str) -> None`

Hard host gate. Raises `RuntimeError` if `socket.gethostname()` does
not match `name`. Use at the top of host-specific scripts.

```python
scitex_os.check_host("bm198")
```

## `is_host(name: str) -> bool`

Boolean form of `check_host`. Returns `True` when the current host
matches `name`.

```python
if scitex_os.is_host("bm198"):
    ...
```

## `verify_host(name: str) -> None`

Soft form. Emits a `UserWarning` instead of raising — useful for
optional fast-paths that have a degraded fallback.

```python
scitex_os.verify_host("bm198")  # warn-only
```

## `mv(src, dst)`

Path-aware safe move. Atomic `os.rename` when src and dst are on the
same filesystem; falls back to `shutil.copy2` + `os.unlink` across
devices to avoid `OSError: [Errno 18] Invalid cross-device link`.

```python
scitex_os.mv("/tmp/data.csv", "/mnt/results/data.csv")
```

Accepts `str` or `pathlib.Path` for both arguments.

## See also

- [01_installation.md](01_installation.md)
- [02_quick-start.md](02_quick-start.md)
