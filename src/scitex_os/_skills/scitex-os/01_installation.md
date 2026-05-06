---
description: |
  [TOPIC] Installing scitex-os
  [DETAILS] pip install (standalone vs umbrella) and how to verify the install.
tags: [scitex-os-installation]
---

# Installation

## pip install

```bash
pip install scitex-os
```

Requires Python >= 3.9. Pure stdlib — no heavy deps.

## Standalone vs umbrella

`scitex-os` is a standalone package, but it is also part of the
[scitex umbrella](https://pypi.org/project/scitex/):

```python
# Standalone — pip install scitex-os
import scitex_os
scitex_os.check_host("bm198")

# Umbrella — pip install scitex
import scitex
scitex.os.check_host("bm198")
```

`pip install scitex-os` alone does **not** expose the `scitex`
namespace. To get both paths, install both:
`pip install scitex scitex-os` (or `pip install scitex[os]`).

## Verify

```python
import scitex_os
print(scitex_os.__version__)
print(scitex_os.is_host("localhost"))   # bool
```

## See also

- [02_quick-start.md](02_quick-start.md)
- [03_python-api.md](03_python-api.md)
