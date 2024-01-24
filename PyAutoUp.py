# Author: Zakaria Dahbi
# Auto-upgrade outdated python packages in a conda environment

import os

try:
    import pandas as pd
except ImportError:
    os.system("pip install pandas")

# colors for fancy printing
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# # reading and preprocessing the outdated packages list
os.system("pip list --outdated > outdated_packages.txt")
os.system("cat outdated_packages.txt | sed -E 's/ +/,/g' > packages.csv")
packages_metada = pd.read_csv("packages.csv", sep=',').drop(index=0, columns = 'Type')
os.system("rm packages.csv")

# print some info
print(bcolors.BOLD + bcolors.OKGREEN +"\n#####################################################"+ bcolors.ENDC)
print(bcolors.BOLD + bcolors.OKGREEN + "#      You have " + bcolors.WARNING + "30" + bcolors.ENDC + bcolors.BOLD + bcolors.OKGREEN + " outdated (Python) packages!      #" + bcolors.ENDC)
print(bcolors.BOLD + bcolors.OKGREEN +"#####################################################\n"+ bcolors.ENDC)

# # looping and upgrading the packages using conda
for package in range(1, len(packages_metada) + 1):
    pack_name = packages_metada["Package"][package]
    pack_old = packages_metada["Version"][package]
    pack_new = packages_metada["Latest"][package]
    print(bcolors.BOLD + bcolors.HEADER + "\n#####################################################" + bcolors.ENDC)
    print(f"   Upgrading " + bcolors.WARNING + bcolors.BOLD +f"{pack_name}:" + bcolors.OKCYAN + bcolors.BOLD + f" v{pack_old}" + bcolors.ENDC + " ----> " + bcolors.BOLD + bcolors.OKGREEN + f" v{pack_new}" + bcolors.ENDC)
    print(bcolors.BOLD + bcolors.HEADER + "-----------------------------------------------------" + bcolors.ENDC)
    print(bcolors.WARNING + bcolors.BOLD + f"                 PROGRESS: {round((package*100)/(len(packages_metada) + 1), 2)}%" + bcolors.ENDC)
    print(bcolors.BOLD + bcolors.HEADER + "#####################################################\n" + bcolors.ENDC)
    os.system(f"conda install -y {pack_name}={pack_new}")

# the upgrade is finished
print(bcolors.BOLD + bcolors.OKGREEN +"\n#####################################################"+ bcolors.ENDC)
print(bcolors.BOLD + bcolors.OKGREEN + "#      Done! The upgrade process is finished!       #" + bcolors.ENDC)
print(bcolors.BOLD + bcolors.OKGREEN +"#####################################################\n"+ bcolors.ENDC)