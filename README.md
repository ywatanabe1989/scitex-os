# scitex-os

<p align="center">
  <a href="https://scitex.ai">
    <img src="docs/scitex-logo-blue-cropped.png" alt="SciTeX" width="400">
  </a>
</p>

<p align="center"><b>Host check + safe file move helpers — zero-dep, pure stdlib.</b></p>

<p align="center">
  <a href="https://scitex-os.readthedocs.io/">Full Documentation</a> · <code>pip install scitex-os</code>
</p>

<!-- scitex-badges:start -->
<p align="center">
  <a href="https://pypi.org/project/scitex-os/"><img src="https://img.shields.io/pypi/v/scitex-os.svg" alt="PyPI"></a>
  <a href="https://pypi.org/project/scitex-os/"><img src="https://img.shields.io/pypi/pyversions/scitex-os.svg" alt="Python"></a>
  <a href="https://github.com/ywatanabe1989/scitex-os/actions/workflows/test.yml"><img src="https://github.com/ywatanabe1989/scitex-os/actions/workflows/test.yml/badge.svg" alt="Tests"></a>
  <a href="https://github.com/ywatanabe1989/scitex-os/actions/workflows/install-test.yml"><img src="https://github.com/ywatanabe1989/scitex-os/actions/workflows/install-test.yml/badge.svg" alt="Install Test"></a>
  <a href="https://codecov.io/gh/ywatanabe1989/scitex-os"><img src="https://codecov.io/gh/ywatanabe1989/scitex-os/graph/badge.svg" alt="Coverage"></a>
  <a href="https://scitex-os.readthedocs.io/en/latest/"><img src="https://readthedocs.org/projects/scitex-os/badge/?version=latest" alt="Docs"></a>
  <a href="https://www.gnu.org/licenses/agpl-3.0"><img src="https://img.shields.io/badge/license-AGPL_v3-blue.svg" alt="License: AGPL v3"></a>
</p>
<!-- scitex-badges:end -->

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

<details open>
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

## Architecture

```
scitex_os/
├── _host.py              ← is_host / check_host / verify_host
├── _move.py              ← `mv` (shutil.move + mkdir(target.parent))
└── __init__.py           ← public surface (zero deps beyond stdlib)
```

## Demo

```mermaid
flowchart LR
    A[script.py] -->|is_host| B{hostname<br/>matches?}
    B -- yes --> C[sxos.mv src → tgt<br/>auto mkdir parent]
    B -- no --> D[skip / raise]
```

```python
import scitex_os as sxos

if sxos.is_host("compute-01"):
    sxos.mv("results/run.csv", "/shared/runs/2026-05-07/run.csv")
# parent dir is auto-created; cross-filesystem moves are handled.
```

```bash
$ python -c "import scitex_os; print(scitex_os.is_host('laptop'))"
True
```

## Part of SciTeX

`scitex-os` is part of [**SciTeX**](https://scitex.ai). Install via
the umbrella with `pip install scitex[os]` to use as
`scitex.os` (Python) or `scitex os ...` (CLI).

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
