"""scitex-os quickstart: hostname checks + safe file move."""

import socket
import tempfile
from pathlib import Path

import scitex_os


def main():
    # 1. check_host / is_host: substring match against the local hostname.
    me = socket.gethostname()
    print("local hostname:", me)

    # check_host returns True if 'keyword' appears in hostname.
    assert scitex_os.check_host(me) is True
    assert scitex_os.is_host(me) is True
    assert scitex_os.check_host("__definitely_not_my_host__") is False
    print("check_host(self) -> True; check_host(garbage) -> False")

    # 2. mv: safe file/dir move that auto-creates the target dir.
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        src = td / "hello.txt"
        src.write_text("greetings from scitex_os\n")
        dst = td / "subdir"

        scitex_os.mv(str(src), str(dst))
        moved = dst / "hello.txt"
        print(f"\nmv {src} -> {dst}: exists={moved.exists()}")
        assert moved.exists()
        assert moved.read_text().startswith("greetings")
        assert not src.exists()


if __name__ == "__main__":
    main()
