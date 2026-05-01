# scitex-os

<!-- scitex-badges:start -->
[![PyPI](https://img.shields.io/pypi/v/scitex-os.svg)](https://pypi.org/project/scitex-os/)
[![Python](https://img.shields.io/pypi/pyversions/scitex-os.svg)](https://pypi.org/project/scitex-os/)
[![Tests](https://github.com/ywatanabe1989/scitex-os/actions/workflows/test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-os/actions/workflows/test.yml)
[![Install Test](https://github.com/ywatanabe1989/scitex-os/actions/workflows/install-test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-os/actions/workflows/install-test.yml)
[![Coverage](https://codecov.io/gh/ywatanabe1989/scitex-os/graph/badge.svg)](https://codecov.io/gh/ywatanabe1989/scitex-os)
[![Docs](https://readthedocs.org/projects/scitex-os/badge/?version=latest)](https://scitex-os.readthedocs.io/en/latest/)
[![License: AGPL v3](https://img.shields.io/badge/license-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
<!-- scitex-badges:end -->

<p align="center">
  <a href="https://scitex.ai">
    <img src="docs/scitex-logo-blue-cropped.png" alt="SciTeX" width="400">
  </a>
</p>

<p align="center"><b>Host check + safe file move helpers — zero-dep, pure stdlib.</b></p>

<p align="center">
  <a href="https://scitex-os.readthedocs.io/">Full Documentation</a> · <code>pip install scitex-os</code>
</p>

---

## Installation

```bash
pip install scitex-os
```

## Quick Start

```python
import scitex_os as sxos

if sxos.is_host("compute-01"):
    sxos.mv(src, tgt)
```

## 1 Interfaces

<details>
<summary><strong>Python API</strong></summary>

<br>

```python
import scitex_os as sxos

sxos.is_host("hostname")          # bool
sxos.check_host("hostname")       # bool
sxos.verify_host("hostname")      # raises if mismatch

sxos.mv(src, tgt)                 # shutil.move with mkdir(tgt)
```

</details>

## Status

Standalone fork of `scitex.os`. Pure stdlib — zero deps. The umbrella package's
`scitex.os` import path is preserved via a `sys.modules`-alias bridge.

## Part of SciTeX

`scitex-os` is part of [**SciTeX**](https://scitex.ai).

>Four Freedoms for Research
>
>0. The freedom to **run** your research anywhere — your machine, your terms.
>1. The freedom to **study** how every step works — from raw data to final manuscript.
>2. The freedom to **redistribute** your workflows, not just your papers.
>3. The freedom to **modify** any module and share improvements with the community.
>
>AGPL-3.0 — because we believe research infrastructure deserves the same freedoms as the software it runs on.

## License

AGPL-3.0-only (see [LICENSE](./LICENSE)).

---

<p align="center">
  <a href="https://scitex.ai" target="_blank"><img src="docs/scitex-icon-navy-inverted.png" alt="SciTeX" width="40"/></a>
</p>
