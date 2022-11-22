# vpsbot
Allows you to create &amp; admin LinuxContainers (LXC) Using Discord 

# Requirements:
- Python3 (apt pkg)
- wondersharper (apt pkg)
- screenfetch (apt pkg)
- git (apt pkg)
- docker.io (apt pkg)
- discord (python lib)
- psutil (python lib)

# Server Requirements:
- Any 1 Gb KVM Server will work (Testing Env)
- Any 8 Gb KVM Server will also work (Production Env)

# Tested Devices:
- Raspberry Pi 4 (4 GB Model)
- Old 2Gb Dell Laptop
- 4Gb 1Vcore KVM Server

# Installation!
First make sure to modify *config.cfg* to your needs then do
- **apt install screenfetch git wondersharper docker.io -y**
- **pip install -r requirements.txt**
- **git clone https://github.com/dxomg/vpsbot**
- **cd dockerbot**
- **wget https://download1483.mediafire.com/nh8cisqdihkg/4hdf9gcigevw5ws/imagesamd64.tar && docker load < imagesamd64.tar** for amd64 Processors
- **wget https://download1648.mediafire.com/e3g1zr4izvqg/ge4k03pdsb9n585/imagesarm64.tar &&  docker load < imagesarm64.tar** for arm64 Processors
- **python3 main.py**
