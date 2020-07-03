import os
os.chdir(r"C:\Users\jeff\Desktop\Centrillion\cen_work_material\Summit.Release\ReleaseLogger")
import subprocess as sp
import git
import json
import giturlparse as gup
import utils.sh as sish
from utils import path

git.Repo.remote()

def update_module(mod: git.Repo, param: dict):
    mod.git.clean("-df")
    mod.git.checkout("--", ".")
    mod.remote().fetch()
    mod.git.checkout(param["version"])
    if(param['submodule_update']):
        mod.git.submodule('init')
        mod.git.submodule('update')

    
def update_all(packages: dict):
    sish.clean_dir(path.input_dir)
    for name, pack_param in packages.items():
        url = pack_param["url"]
        repo = git.Repo.clone_from(url, path.input_dir / name)
        update_module(mod=repo, param=pack_param)
        

if __name__ == "__main__":
    with open(path.package_file) as packages_file:
        packages_data = json.load(packages_file)
        print(packages_data)
        update_all(packages_data)