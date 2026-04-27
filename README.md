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


Host check + safe file move helpers, extracted from the [SciTeX](https://github.com/ywatanabe1989/scitex-python) ecosystem as a standalone, zero-dep package.

## Install

```bash
pip install scitex-os
```

## API

```python
import scitex_os as sxos

sxos.is_host("hostname")          # bool
sxos.check_host("hostname")       # bool
sxos.verify_host("hostname")      # raises if mismatch

sxos.mv(src, tgt)                 # shutil.move with mkdir(tgt)
```

## Status

Standalone fork of `scitex.os`. Pure stdlib — zero deps. The umbrella package's
`scitex.os` import path is preserved via a `sys.modules`-alias bridge. 7/7 smoke
tests pass.

## License

AGPL-3.0-only (see [LICENSE](./LICENSE)).
