# python pdfjail.py <password> <directory>
# Based on code from: https://www.reddit.com/r/Python/comments/t32z2o/simple_code_to_unlock_all_readonly_pdfs_in/

import sys
import glob
import pikepdf

def unlock_pdf(file, password):
    try:
        pdf = pikepdf.open(file ,allow_overwriting_input=True, password=password)
        pdf.save(file)
    except:
        return 0
    else:
        return 1

def require_password(file):
    try:
        pdf = pikepdf.open(file)
    except:
        return 1
    else:
        return 0
    
def print_files(files):
    for file in files:
        print(f"\t{file}")

password = sys.argv[1]
directory = sys.argv[2]
files = glob.glob(f"{directory}/**/*.pdf", recursive = True)
ignored = []
unlocked = []
failed = []

for file in files:
    if not require_password(file):
        ignored.append(file)
        continue

    if unlock_pdf(file, password):
        unlocked.append(file)
    else:
        failed.append(file)

print(f"ignored {len(ignored)} files")
print(f"unlocked {len(unlocked)} files")
print_files(unlocked)
print(f"failed {len(failed)} files")
print_files(failed)



