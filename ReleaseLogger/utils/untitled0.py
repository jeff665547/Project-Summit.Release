import os
from pathlib import Path
import Mdutils as md
import git
import json
import giturlparse as gup
import subprocess

wd = Path(r"C:\Users\jeff\Desktop")
os.chdir(wd)

#%%
def build_index(input):
    res = {}
    for proj in input:
        name = gup.parse(proj['url']).name
        res[name] = proj
    return res
#%%

# Inputs
releaselog_version = "USA-v0.2.15.1"
with open("packages.json") as f:
    package_info = json.load(f)
    param = package_info
    param['input'] = build_index(param['input'])

# Input Transformation
test_spec_version = ".".join(releaselog_version.split(".")[:-1])
reader_msi_version = package_info["bundle"]["reader"]["version"]
server_msi_version = package_info["bundle"]["server"]["version"]
releaselog_version = package_info["bundle"]["logger"]["version"]

git.Repo.clone_from()

# Program
mdFile = md.MdUtils(file_name = releaselog_version, title = "")

mdFile.new_paragraph("Latest Version", bold_italics_code = 'bi')
mdFile.new_paragraph(f"Software Spec (Test) Version: {test_spec_version}", 
                     bold_italics_code='bi')

mdFile.new_paragraph(f"SUMMIT Reader: {reader_msi_version}", 
                     bold_italics_code='b')
mdFile.new_paragraph(f"SUMMIT Server: {server_msi_version}", 
                     bold_italics_code='b')

mdFile.new_paragraph("* [ ] Testing passed.")
mdFile.write("      Date: ____________", bold_italics_code = 'b')
mdFile.write(",   ")
mdFile.new_paragraph("      Sign: ____________", bold_italics_code = 'b')

mdFile.new_paragraph("* [ ] Customers' devices status checked.")
mdFile.write("      Date: ____________", bold_italics_code = 'b')
mdFile.write(",   ")
mdFile.new_paragraph("      Sign: ____________", bold_italics_code = 'b')

mdFile.new_paragraph("* [ ] Softwares installed and operations checked.")
mdFile.write("      Date: ____________", bold_italics_code = 'b')
mdFile.write(",   ")
mdFile.new_paragraph("      Sign: ____________", bold_italics_code = 'b')

mdFile.new_paragraph("*  Content", bold_italics_code = 'b')
mdFile.new_paragraph("    *  Submodule Version")
mdFile.create_md_file()


mdFile.new_paragraph(f"        *  {}: ** **")
git.Repo().
os.chdir(r"C:\Users\jeff\Desktop\example\Summit.Installertu\input\bamboo-lake3")
subprocess.check_output(["git","log", "-1", "--format=%ai", "CN-v0.1.10.2"])
