---
name: scitex-os
description: Host-check helpers + safe file move. `check_host(name)` raises if not on the named machine; `is_host(name)` is the boolean version; `verify_host(...)` emits a warning. `mv(src, dst)` is a path-aware safe rename (atomic when same filesystem, copy+unlink across devices). Drop-in replacement for `socket.gethostname() == 'X'` checks at the top of host-specific scripts.
primary_interface: python
interfaces:
  python: 2
  cli: 0
  mcp: 0
  skills: 2
  hook: 0
  http: 0
canonical-location: scitex-os/src/scitex_os/_skills/scitex-os/SKILL.md
tags: [scitex-os, scitex-package]
---

> **Interfaces:** Python ⭐⭐ · CLI — · MCP — · Skills ⭐⭐ · Hook — · HTTP —

# scitex-os

Host-check helpers + safe file move. `check_host(name)` raises if not on the named machine; `is_host(name)` is the boolean version; `verify_host(...)` emits a warning. `mv(src, dst)` is a path-aware safe rename (atomic when same filesystem, copy+unlink across devices). Drop-in replacement for `socket.gethostname() == 'X'` checks at the top of host-specific scripts.

See README.md and the package's public `__init__.py` for the full
function list. This skill leaf exists so agents discover the package
exists and roughly what shape it has — refer to the source for
signatures.
