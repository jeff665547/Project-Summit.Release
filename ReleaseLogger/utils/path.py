import os
from pathlib import Path

exe_path = Path(__file__).absolute()
proj_dir = Path(os.path.realpath(exe_path.parent / ".."))
input_dir = proj_dir / 'input'

package_file = proj_dir / "packages.json"
