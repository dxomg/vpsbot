import os
import sys

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

if os.geteuid() != 0:
    exit(f"{bcolors.FAIL}You need to have root privileges to run this script.\nPlease try again, this time using root user. Exiting.{bcolors.ENDC}")

print(f"""
{bcolors.OKCYAN}Hello!, Welcome to the vpsbot installer :){bcolors.ENDC}

{bcolors.BOLD}{bcolors.UNDERLINE}What is your device architecture?{bcolors.ENDC}

1 > amd64
2 > arm64
3 > Dont Know!
4 > Not here!

Choose carefully!
""")

def getarch():
    try:
        architecture = int(input("> "))

        if architecture == 1:
            return architecture
        elif architecture == 2:
            return architecture
        elif architecture == 3:
            print("You can search on google how to get it :)")
        elif architecture == 4:
            print("Ask the developer for help :)")
        else:
            print("Enter a correct value!")
    except:
        print("Enter a correct value!")
getarch()

def install():
    if getarch() == 1:
        print(f"{bcolors.WARNING}Installing requirements{bcolors.ENDC}")
        os.system("apt install screenfetch git wondershaper docker.io -y")
        print(f"{bcolors.WARNING}70% Done{bcolors.ENDC}")
        os.system("git clone https://github.com/dxomg/vpsbot")
        os.system("cd vpsbot/dockerbot")
        os.system("wget https://download1483.mediafire.com/nh8cisqdihkg/4hdf9gcigevw5ws/imagesamd64.tar && docker load < imagesamd64.tar")
        print(f"{bcolors.WARNING}100% Done{bcolors.ENDC}")
    if getarch() == 2:
        print(f"{bcolors.WARNING}Installing requirements{bcolors.ENDC}")
        os.system("apt install screenfetch git wondershaper docker.io -y")
        print(f"{bcolors.WARNING}70% Done{bcolors.ENDC}")
        os.system("git clone https://github.com/dxomg/vpsbot")
        os.system("cd vpsbot/dockerbot")
        os.system("wget https://download1648.mediafire.com/e3g1zr4izvqg/ge4k03pdsb9n585/imagesarm64.tar && docker load < imagesarm64.tar")
        print(f"{bcolors.WARNING}100% Done{bcolors.ENDC}")
install()