# scitex-os

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
