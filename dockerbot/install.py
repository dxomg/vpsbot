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
    while True:
        try:
            architecture = int(input("> "))

            if architecture in (1, 2):
                return architecture
            elif architecture == 3:
                print("You can search on google how to get it :)")
            elif architecture == 4:
                print("Ask the developer for help :)")
            else:
                print("Enter a correct value!")
        except ValueError:
            print("Enter a correct value!")

def install():
    architecture = getarch()
    if architecture == 1:
        print(f"{bcolors.WARNING}Installing requirements{bcolors.ENDC}")
        os.system("apt install screenfetch git wondershaper docker.io -y")
        print(f"{bcolors.WARNING}70% Done{bcolors.ENDC}")
        os.system("git clone https://github.com/dxomg/vpsbot")
        os.system("cd vpsbot/dockerbot")
        os.system("wget -O imagesamd64.tar.gz 'https://drive.google.com/uc?id=1iUUNLS4hhSk6vCXMwjR09jCOFAblK7as&export=download&confirm=t&uuid=6aa2ceab-5731-4e33-ab08-f054aedafe3e' && docker load < imagesamd64.tar")
        print(f"{bcolors.WARNING}100% Done{bcolors.ENDC}")
    if architecture  == 2:
        print(f"{bcolors.WARNING}Installing requirements{bcolors.ENDC}")
        os.system("apt install screenfetch git wondershaper docker.io -y")
        print(f"{bcolors.WARNING}70% Done{bcolors.ENDC}")
        os.system("git clone https://github.com/dxomg/vpsbot")
        os.system("cd vpsbot/dockerbot")
        os.system("wget -O imagesamd64.tar.gz 'https://drive.google.com/uc?id=1lGrbGAnDBbGpUH63X_zq2Bxy0EeOXNnY&export=download&confirm=t&uuid=90ee1fa3-806d-40c3-9cc1-d31adf586b17' && docker load < imagesarm64.tar")
        print(f"{bcolors.OKGREEN}100% Done{bcolors.ENDC}")
        print(f"""
        {bcolors.WARNING}Install has been completed!, now go edit the config.cfg file to your needs
        and start the bot with the {bcolors.BOLD}python3 main.py{bcolors.ENDC} command{bcolors.ENDC}
        """)
install()
