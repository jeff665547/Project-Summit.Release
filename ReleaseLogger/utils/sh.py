import os
from pathlib import Path
import shutil as sh  # using rmtree

def clean_dir(dir: str):
    path = Path(dir)
    if(not path.is_dir()):
        path.mkdir()
    elif(path.is_dir()):
        import stat
        if not os.access(path, os.W_OK):
            os.chmod(path, stat.S_IWUSR)
        sh.rmtree(path)
        path.mkdir()
    else:
        raise RuntimeError('not directory')
