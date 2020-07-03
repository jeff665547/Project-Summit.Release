import os
os.chdir(r"C:\Users\jeff\Desktop\Centrillion\cen_work_material\Summit.Release\ReleaseLogger")
import json
import giturlparse as gup
import utils.path as sipath
import utils.packages as sipack


def build_index(input):
    res = {}
    for proj in input:
        name = gup.parse(proj['url']).name
        res[name] = proj
    return res

if __name__ == "__main__":
    
    print("Parse packege file")
    with open(sipath.package_file) as packages_file:
        packages_data = json.load(packages_file)
        param = packages_data
        param['input'] = build_index(param['input'])
    
    print("Clone changelog")
    sipack.update_all(param['input'])
    
    print("Compare difference with previous version changelog")
    
    print("Generate release log")
    
    