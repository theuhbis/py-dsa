import pathlib
import sys
import pytest

cwd = pathlib.Path.cwd()

sys.path.append(str(cwd.parent))

pytest.main()
