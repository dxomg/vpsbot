import os
import sys
import discord
import psutil
import time
from configparser import ConfigParser
from typing import Literal
from discord import app_commands
from discord.ext import commands

config = ConfigParser()
config.read('config.cfg')

botprefix = "/" # Don't change
intents = discord.Intents.all()
client = commands.Bot(command_prefix=botprefix, intents=intents)
client.remove_command('help')
version = "Beta 1.1"

#Log Options
logs = "[Logs] "
devicename = config['Config']['devicename']

#Gerarchy (Admin's & User's Roles)
adminrole = config['Config']['adminrole']
userrole = config['Config']['userrole']

#Creation Options
usercpu = config['Config']['usercpu'] # Multiplied by the cores set \/
usercores = config['Config']['usercores'] # Wich Core(s) should we use for the user containers?
userram = config['Config']['userram'] #Megabytes
userswap = config['Config']['userswap'] #Megabytes
userdisk = config['Config']['userdisk'] #Gigabytes, Unavailable in Rasperry pi (--storage-opt size={userdisk}G) was deleted
onstartupnet = config['Config']['onstartupnet'] # Kibps DOWN/UP
idprefix = config['Config']['idprefix'] #ID Prefix on container Names & Hostnames
vpslimit = int(config['Config']['vpslimit']) # Limit of availability on vpses

#Channel Options
cmdchid = config['Config']['cmdchid'] # Channel id where bot will allow messages from


##### - Start Of Code - #####
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f"{botprefix}help"))
    synced = await client.tree.sync()
    print(f"{len(synced)} Commands have been synced")

#Function to check if channel is cmdchid
async def commandchannelid(ctx):
    return ctx.channel.id == cmdchid

########################################################## - Help Command \/

@client.tree.command(name="help", description="Tells you all commands")
@commands.has_role(userrole)
@commands.check(commandchannelid)
async def help(interaction: discord.Interaction):

    logvarcmd = "help"
    print(f"{logs}User {interaction.user.id} executed {logvarcmd}")
#Embed

    embed = discord.Embed(title="Help", description=f"Prefix ({botprefix})", color=discord.Color.blue())
    embed.add_field(name="createvps (ubuntu/debian/alpine)", value=f"Allows you to create 1 vps")
    embed.add_field(name="startvps", value=f"Allows you to manage your vps")
    embed.add_field(name="stopvps", value=f"Allows you to manage your vps")
    embed.add_field(name="restartvps", value=f"Allows you to manage your vps")
    embed.add_field(name="deletevps", value=f"Allows you to delete your vps")
    embed.add_field(name="regenssh", value=f"Re-Generate the ssh session")
    embed.add_field(name="infovps", value=f"Allows you to see the current Status of your vps")
    embed.add_field(name="nodeinfo", value=f"Allows you to see the current usage of the node")
    embed.add_field(name="help", value=f"This Command")
    embed.set_footer(text = f"Version: {version}")
    await interaction.response.send_message(embed=embed)

########################################################## - Help Command CN version \/

@client.tree.command(name="helpcn", description="Tells you all commands")
@commands.has_role(userrole)
@commands.check(commandchannelid)
async def helpcn(interaction: discord.Interaction):

    logvarcmd = "helpcn"
    print(f"{logs}User {interaction.user.id} executed {logvarcmd}")
#Embed

    embed = discord.Embed(title="Help", description=f"Prefix ({botprefix})", color=discord.Color.blue())
    embed.add_field(name="createvps (ubuntu/debian/alpine)", value=f"允许你创建1个vps")
    embed.add_field(name="startvps", value=f"允许你启动你的vps")
    embed.add_field(name="stopvps", value=f"允许你停止你的vps")
    embed.add_field(name="restartvps", value=f"允许你重新启动你的vps")
    embed.add_field(name="deletevps", value=f"允许你删除你的vps")
    embed.add_field(name="infovps", value=f"允许你看到你的vps的当前状态。")
    embed.add_field(name="nodeinfo", value=f"允许你查看节点的当前使用情况")
    embed.add_field(name="helpcn", value=f"该命令")
    embed.set_footer(text = f"Version: {version}")
    await interaction.response.send_message(embed=embed)

########################################################## - Help Command RU version \/

@client.tree.command(name="helpru", description="Tells you all commands")
@commands.has_role(userrole)
@commands.check(commandchannelid)
async def helpru(interaction: discord.Interaction):

    logvarcmd = "helpru"
    print(f"{logs}User {interaction.user.id} executed {logvarcmd}")
#Embed

    embed = discord.Embed(title="Help", description=f"Префикс ({botprefix})", color=discord.Color.blue())
    embed.add_field(name="createvps (ubuntu/debian/archlinux/alpine)", value=f"Позволяет вам создать 1 VPS")
    embed.add_field(name="startvps", value=f"Позволяет вам запустить ваш")
    embed.add_field(name="stopvps", value=f"Позволяет вам остановить ваш VPS")
    embed.add_field(name="restartvps", value=f"Позволяет вам перезагрузить ваш VPS")
    embed.add_field(name="deletevps", value=f"Позволяет вам удалить ваш VPS")
    embed.add_field(name="infovps", value=f"Позволяет вам посмотреть статус вашего VPS")
    embed.add_field(name="nodeinfo", value=f"Позволяет посмотреть вам использование ресурсов ноды")
    embed.add_field(name="helpru", value=f"Эта команда")
    embed.set_footer(text = f"Version: {version}")
    await interaction.response.send_message(embed=embed)

########################################################## - Help Command ES version \/

@client.tree.command(name="helpes", description="Tells you all commands")
@commands.has_role(userrole)
@commands.check(commandchannelid)
async def helpes(interaction: discord.Interaction):

    logvarcmd = "helpes"
    print(f"{logs}User {interaction.user.id} executed {logvarcmd}")
#Embed

    embed = discord.Embed(title="Help", description=f"Prefijo ({botprefix})", color=discord.Color.blue())
    embed.add_field(name="createvps (ubuntu/debian/archlinux/alpine)", value=f"Te permite crear 1 VPS")
    embed.add_field(name="startvps", value=f"Te permite iniciar tu VPS")
    embed.add_field(name="stopvps", value=f"Te permite parar tu VPS")
    embed.add_field(name="restartvps", value=f"Te permite reiniciar tu VPS")
    embed.add_field(name="deletevps", value=f"Te permite eliminar tu VPS")
    embed.add_field(name="infovps", value=f"Te permite el estado actual de tu VPS")
    embed.add_field(name="nodeinfo", value=f"Te permite ver el uso actual del nodo")
    embed.add_field(name="helpes", value=f"Este comando")
    embed.set_footer(text = f"Version: {version}")
    await interaction.response.send_message(embed=embed)

########################################################## - Help Command FR version \/

@client.tree.command(name="helpfr", description="Tells you all commands")
@commands.has_role(userrole)
@commands.check(commandchannelid)
async def helpfr(interaction: discord.Interaction):

    logvarcmd = "helpfr"
    print(f"{logs}User {interaction.user.id} executed {logvarcmd}")
#Embed

    embed = discord.Embed(title="Help", description=f"Préfixe ({botprefix})", color=discord.Color.blue())
    embed.add_field(name="createvps (ubuntu/debian/archlinux/alpine)", value=f"Vous permet de créer 1 VPS")
    embed.add_field(name="startvps", value=f"Vous permet de démarrer votre VPS")
    embed.add_field(name="stopvps", value=f"Vous permet d'arrêter votre VPS")
    embed.add_field(name="restartvps", value=f"Permet de redémarrer votre VPS")
    embed.add_field(name="deletevps", value=f"Vous permet de supprimer votre VPS")
    embed.add_field(name="infovps", value=f"Permet de voir le statut actuel de votre VPS")
    embed.add_field(name="nodeinfo", value=f"Permet de voir l'état actuel du nœud")
    embed.add_field(name="helpfr", value=f"Cette commande")
    embed.set_footer(text = f"Version: {version}")
    await interaction.response.send_message(embed=embed)

@client.tree.command(name="createvps", description="Tells you all commands")
@commands.has_role(userrole)
@commands.check(commandchannelid)
async def createvps(interaction: discord.Interaction, image: Literal["debian", "ubuntu", "alpine"]):

    logvarcmd = "createvps"

# Template
    desc = f"""```yaml
ID: {idprefix}{interaction.user.id}
OS: {image}
----------------------
Cpu: {usercpu} Vcore(s)%
Core(s): {usercores}
Ram: {userram} MiB
Swap: {userswap} MiB
Disk: {userdisk} GiB
Net: {onstartupnet} Kibps
----------------------```"""


# Get Count of Current Vpses
    vpsnum1 = os.popen(f'docker ps -a -q | wc -l') # Use | grep -i {idprefix} -c to only get containers created by the bot
    vpsnumout1 = vpsnum1.readlines()
    for vpsnumout in vpsnumout1:
        vpsnumout = vpsnumout.strip("\n")

    embed = discord.Embed(title="Creation Successfull!", description=desc, color=discord.Color.green())

#Reply user fetching {using discord API!}
    user = await client.fetch_user(interaction.user.id)

#Images
    alpine = "alpine_custom"
#    archlinux = "amd64/archlinux:base-20221030.0.98412"
    ubuntu = "ubuntu22_custom"
    debian = "debian11_custom"

# LOTS OF IFS
    if image == "alpine" and int(vpsnumout) <= vpslimit:
        print(f"{logs}User {interaction.user.id} executed {logvarcmd}")
        await interaction.response.send_message("Creating...")
        os.system(f'docker run -it -d --cpus="{usercpu}" --cpuset-cpus="{usercores}" --memory="{userram}m" --memory-swap="{userswap}m" -w="/root" --name="{idprefix}{interaction.user.id}" --hostname="{idprefix}{interaction.user.id}" {alpine}')


        os.system(f'docker exec {idprefix}{interaction.user.id} sh -c "tmate -S /tmp/tmate.sock new-session -d"')
        os.system(f'docker exec {idprefix}{interaction.user.id} sh -c "tmate -S /tmp/tmate.sock wait tmate-ready"')

        sshsend1 = os.popen(f'docker exec {idprefix}{interaction.user.id} sh -c "sh /root/tmate.sh"')
        sshsendout1 = sshsend1.readlines()
        for sshsend in sshsendout1:
            sshsend = sshsend.strip('\n')

        await user.send(f"{sshsend}")

# Set Network Limit
        try:
            checkveth1 = os.popen(f"bash vethiddocker.sh | grep -i '{idprefix}{interaction.user.id}'")
            checkvethout1 = checkveth1.readlines()
            for checkveth in checkvethout1:
                checkveth = checkveth.strip('\n')
                checkvethdone = checkveth.split(':', 1)[-1]
                os.system(f"wondershaper {checkvethdone} {onstartupnet}")

                await interaction.response.send_message(embed=embed)
        except:
            await interaction.response.send_message(embed=embed)
######
#    elif image == "archlinux":
#       print(f"{logs}User {interaction.user.id} executed {logvarcmd}")
#       await interaction.response.send_message("Creating...")
#       os.system(f'docker run -it -d --cpus="{usercpu}" --memory="{userram}m" --memory-swap="{userswap}m" -w="/root" --name="{idprefix}{interaction.user.id}" --hostname="{idprefix}{interaction.user.id}" {archlinux}')
#
#Set password to container
#        passgen1 = os.popen(f"bash passgen.sh")
#        passgenout1 = passgen1.readlines()
#        for passgen in passgenout1:
#            passgen = passgen.strip('\n')
#        
#        os.system(f'docker exec {idprefix}{interaction.user.id} sh -c "echo "root:{passgen}" | chpasswd"')
#
# Set Network Limit
#         checkveth1 = os.popen(f"bash vethiddocker.sh | grep -i '{idprefix}{interaction.user.id}'")
#        checkvethout1 = checkveth1.readlines()
#        for checkveth in checkvethout1:
#            checkveth = checkveth.strip('\n')
#            checkvethdone = checkveth.split(':', 1)[-1]
#
#        os.system(f"wondershaper {checkvethdone} {onstartupnet}")
#        await interaction.response.send_message(embed=embed)
######
    elif image == "ubuntu" and int(vpsnumout) <= vpslimit:
        print(f"{logs}User {interaction.user.id} executed {logvarcmd}")
        await interaction.response.send_message("Creating...")
        os.system(f'docker run -it -d --cpus="{usercpu}" --cpuset-cpus="{usercores}" --memory="{userram}m" --memory-swap="{userswap}m" -w="/root" --name="{idprefix}{interaction.user.id}" --hostname="{idprefix}{interaction.user.id}" {ubuntu}')


        os.system(f'docker exec {idprefix}{interaction.user.id} sh -c "tmate -S /tmp/tmate.sock new-session -d"')
        os.system(f'docker exec {idprefix}{interaction.user.id} sh -c "tmate -S /tmp/tmate.sock wait tmate-ready"')

        sshsend1 = os.popen(f'docker exec {idprefix}{interaction.user.id} sh -c "bash /root/tmate.sh"')
        sshsendout1 = sshsend1.readlines()
        for sshsend in sshsendout1:
            sshsend = sshsend.strip('\n')

        await user.send(f"{sshsend}")
# Set Network Limit
        try:
            checkveth1 = os.popen(f"bash vethiddocker.sh | grep -i '{idprefix}{interaction.user.id}'")
            checkvethout1 = checkveth1.readlines()
            for checkveth in checkvethout1:
                checkveth = checkveth.strip('\n')
                checkvethdone = checkveth.split(':', 1)[-1]
                os.system(f"wondershaper {checkvethdone} {onstartupnet}")

                await interaction.response.send_message(embed=embed)
        except:
            await interaction.response.send_message(embed=embed)
######
    elif image == "debian" and int(vpsnumout) <= vpslimit:
        print(f"{logs}User {interaction.user.id} executed {logvarcmd}")
        await interaction.response.send_message("Creating...")
        os.system(f'docker run -it -d --cpus="{usercpu}" --cpuset-cpus="{usercores}" --memory="{userram}m" --memory-swap="{userswap}m" -w="/root" --name="{idprefix}{interaction.user.id}" --hostname="{idprefix}{interaction.user.id}" {debian}')


        os.system(f'docker exec {idprefix}{interaction.user.id} sh -c "tmate -S /tmp/tmate.sock new-session -d"')
        os.system(f'docker exec {idprefix}{interaction.user.id} sh -c "tmate -S /tmp/tmate.sock wait tmate-ready"')

        sshsend1 = os.popen(f'docker exec {idprefix}{interaction.user.id} sh -c "bash /root/tmate.sh"')
        sshsendout1 = sshsend1.readlines()
        for sshsend in sshsendout1:
            sshsend = sshsend.strip('\n')

        await user.send(f"{sshsend}")
# Set Network Limit
        try:
            checkveth1 = os.popen(f"bash vethiddocker.sh | grep -i '{idprefix}{interaction.user.id}'")
            checkvethout1 = checkveth1.readlines()
            for checkveth in checkvethout1:
                checkveth = checkveth.strip('\n')
                checkvethdone = checkveth.split(':', 1)[-1]
                os.system(f"wondershaper {checkvethdone} {onstartupnet}")

                await interaction.response.send_message(embed=embed)
        except:
            await interaction.response.send_message(embed=embed)

### -ADMIN CREATE VPS- ###

@client.tree.command(name="admincreatevps", description="Allows admins to create vpses")
@commands.has_role(adminrole)
async def admicreatevps(interaction: discord.Interaction, id: str, image: Literal["debian", "ubuntu", "alpine"], cpu: str, cores: str, ram: str, swap: str, net: str):

    logvarcmd = "admincreatevps"

# Template
    desc = f"""```yaml
ID: {id}
OS: {image}
----------------------
Cpu: {cpu} Vcore(%)
Core(s): {cores}
Ram: {ram} MiB
Swap: {swap} MiB
Disk: - GiB
Net: {net} Kibps
----------------------```"""

    embed = discord.Embed(title="Creation Successfull!", description=desc, color=discord.Color.green())

#Images
    alpine = "alpine:3.16.2"
#    archlinux = "amd64/archlinux:base-20221030.0.98412"
    ubuntu = "ubuntu22_custom"
    debian = "debian:11"

# LOTS OF IFS
    if image == "alpine":
        print(f"{logs}User {interaction.user.id} executed {logvarcmd}")
        await interaction.response.send_message("Creating...")
        os.system(f'docker run -it -d --cpus="{cpu}" --cpuset-cpus="{cores}" --memory="{ram}m" --memory-swap="{swap}m" -w="/root" --name="{id}" --hostname="{id}" {alpine}')
        
#Set password to container
        passgen1 = os.popen(f"bash passgen.sh")
        passgenout1 = passgen1.readlines()
        for passgen in passgenout1:
            passgen = passgen.strip('\n')
        
        os.system(f'docker exec {id} sh -c "echo "root:{passgen}" | chpasswd"')
# Set Network Limit
        try:
            checkveth1 = os.popen(f"bash vethiddocker.sh | grep -i '{id}'")
            checkvethout1 = checkveth1.readlines()
            for checkveth in checkvethout1:
                checkveth = checkveth.strip('\n')
                checkvethdone = checkveth.split(':', 1)[-1]
                os.system(f"wondershaper {checkvethdone} {onstartupnet}")

                await interaction.response.send_message(embed=embed)
        except:
            await interaction.response.send_message(embed=embed)
######
#    elif image == "archlinux":
#       print(f"{logs}User {interaction.user.id} executed {logvarcmd}")
#       await interaction.response.send_message("Creating...")
#       os.system(f'docker run -it -d --cpus="{usercpu}" --memory="{userram}m" --memory-swap="{userswap}m" -w="/root" --name="{idprefix}{interaction.user.id}" --hostname="{idprefix}{interaction.user.id}" {archlinux}')
#
#Set password to container
#        passgen1 = os.popen(f"bash passgen.sh")
#        passgenout1 = passgen1.readlines()
#        for passgen in passgenout1:
#            passgen = passgen.strip('\n')
#        
#        os.system(f'docker exec {idprefix}{interaction.user.id} sh -c "echo "root:{passgen}" | chpasswd"')
#
# Set Network Limit
#         checkveth1 = os.popen(f"bash vethiddocker.sh | grep -i '{idprefix}{interaction.user.id}'")
#        checkvethout1 = checkveth1.readlines()
#        for checkveth in checkvethout1:
#            checkveth = checkveth.strip('\n')
#            checkvethdone = checkveth.split(':', 1)[-1]
#
#        os.system(f"wondershaper {checkvethdone} {onstartupnet}")
#        await interaction.response.send_message(embed=embed)
######
    elif image == "ubuntu":
        print(f"{logs}User {interaction.user.id} executed {logvarcmd}")
        await interaction.response.send_message("Creating...")
        os.system(f'docker run -it -d --cpus="{cpu}" --cpuset-cpus="{cores}" --memory="{ram}m" --memory-swap="{swap}m" -w="/root" --name="{id}" --hostname="{id}" {ubuntu}')

#Set password to container
        passgen1 = os.popen(f"bash passgen.sh")
        passgenout1 = passgen1.readlines()
        for passgen in passgenout1:
            passgen = passgen.strip('\n')
        
        os.system(f'docker exec {id} sh -c "echo "root:{passgen}" | chpasswd"')

# Set Network Limit
        try:
            checkveth1 = os.popen(f"bash vethiddocker.sh | grep -i '{id}'")
            checkvethout1 = checkveth1.readlines()
            for checkveth in checkvethout1:
                checkveth = checkveth.strip('\n')
                checkvethdone = checkveth.split(':', 1)[-1]
                os.system(f"wondershaper {checkvethdone} {onstartupnet}")

                await interaction.response.send_message(embed=embed)
        except:
            await interaction.response.send_message(embed=embed)
######
    elif image == "debian":
        print(f"{logs}User {interaction.user.id} executed {logvarcmd}")
        await interaction.response.send_message("Creating...")
        os.system(f'docker run -it -d --cpus="{cpu}" --cpuset-cpus="{cores}" --memory="{ram}m" --memory-swap="{swap}m" -w="/root" --name="{id}" --hostname="{id}" {debian}')

#Set password to container
        passgen1 = os.popen(f"bash passgen.sh")
        passgenout1 = passgen1.readlines()
        for passgen in passgenout1:
            passgen = passgen.strip('\n')
        
        os.system(f'docker exec {id} sh -c "echo "root:{passgen}" | chpasswd"')

# Set Network Limit
        try:
            checkveth1 = os.popen(f"bash vethiddocker.sh | grep -i '{id}'")
            checkvethout1 = checkveth1.readlines()
            for checkveth in checkvethout1:
                checkveth = checkveth.strip('\n')
                checkvethdone = checkveth.split(':', 1)[-1]
                os.system(f"wondershaper {checkvethdone} {onstartupnet}")

                await interaction.response.send_message(embed=embed)
        except:
            await interaction.response.send_message(embed=embed)

############## -REGEN SSH SESSION VPS- ##############
@client.tree.command(name="regenssh", description="Regenerates ssh if it dosent work")
@commands.has_role(userrole)
async def regenssh(interaction: discord.Interaction):
    
    logvarcmd = "regenssh"
    print(f"{logs}User {interaction.user.id} executed {logvarcmd}")

#Reply user fetching {using discord API!}
    user = await client.fetch_user(interaction.user.id)

#Embed
    embed = discord.Embed(title="SSH Regenerated Successfully!", description="Regen SSH", color=discord.Color.green())

    os.system(f'docker exec {idprefix}{interaction.user.id} sh -c "tmate -S /tmp/tmate.sock new-session -d"')
    os.system(f'docker exec {idprefix}{interaction.user.id} sh -c "tmate -S /tmp/tmate.sock wait tmate-ready"')

    sshsend1 = os.popen(f'docker exec {idprefix}{interaction.user.id} sh -c "sh /root/tmate.sh"')
    sshsendout1 = sshsend1.readlines()
    for sshsend in sshsendout1:
        sshsend = sshsend.strip('\n')

    await user.send(f"{sshsend}")
    await interaction.response.send_message(embed=embed)

### -ADMIN REGEN SSH- ###

@client.tree.command(name="adminregenssh", description="Allows admins to regenerate vpses ssh")
@commands.has_role(adminrole)
async def adminregenssh(interaction: discord.Interaction, id: str):
    
    logvarcmd = "adminregenssh"
    print(f"{logs}User {interaction.user.id} executed {logvarcmd}")

#Reply user fetching {using discord API!}
    user = await client.fetch_user(interaction.user.id)

#Embed
    embed = discord.Embed(title="SSH Regenerated Successfully!", description="Regen SSH", color=discord.Color.green())

    os.system(f'docker exec {id} sh -c "tmate -S /tmp/tmate.sock new-session -d"')
    os.system(f'docker exec {id} sh -c "tmate -S /tmp/tmate.sock wait tmate-ready"')

    sshsend1 = os.popen(f'docker exec {id} sh -c "sh /root/tmate.sh"')
    sshsendout1 = sshsend1.readlines()
    for sshsend in sshsendout1:
        sshsend = sshsend.strip('\n')

    await user.send(f"{sshsend}")
    await interaction.response.send_message(embed=embed)

############## -DELETE VPS- ############## 
@client.tree.command(name="deletevps", description="Allows you to delete your vps")
@commands.has_role(userrole)
async def deletevps(interaction: discord.Interaction):

    logvarcmd = "deletevps"
    print(f"{logs}User {interaction.user.id} executed {logvarcmd}")

#Embed
    embed = discord.Embed(title="Delete Successfull!", description="Delete Vps", color=discord.Color.green())  

#Command
    os.system(f"docker rm {idprefix}{interaction.user.id} -f")
    await interaction.response.send_message(embed=embed)

### -ADMIN DELETE VPS- ###

@client.tree.command(name="admindeletevps", description="Allows admins to delete vpses")
@commands.has_role(adminrole)
async def admindeletevps(interaction: discord.Interaction, id: str):

    logvarcmd = "admindeletevps"
    print(f"{logs}User {interaction.user.id} executed {logvarcmd}")

#Embed
    embed = discord.Embed(title="Delete Successfull!", description="Delete Vps", color=discord.Color.green())  

#Command
    os.system(f"docker rm {id} -f")
    await interaction.response.send_message(embed=embed)

############## -START VPS- ############## 

@client.tree.command(name="startvps", description="Allows you to start your vps")
@commands.has_role(userrole)
async def startvps(interaction: discord.Interaction):

    logvarcmd = "startvps"
    print(f"{logs}User {interaction.user.id} executed {logvarcmd}")

#Embed
    embed = discord.Embed(title="Start Successfull!", description="Start Vps", color=discord.Color.green())

#Command
    os.system(f"docker start {idprefix}{interaction.user.id}")
    
    checkveth1 = os.popen(f"bash vethiddocker.sh | grep -i '{idprefix}{interaction.user.id}'")
    checkvethout1 = checkveth1.readlines()
    for checkveth in checkvethout1:
        checkveth = checkveth.strip('\n')
        checkvethdone = checkveth.split(':', 1)[-1]

    os.system(f"wondershaper {checkvethdone} {onstartupnet}")

    await interaction.response.send_message(embed=embed)

### -ADMIN START VPS- ###

@client.tree.command(name="adminstartvps", description="Allows admins to start vpses")
@commands.has_role(adminrole)
async def adminstartvps(interaction: discord.Interaction, id: str):

    logvarcmd = "adminstartvps"
    print(f"{logs}User {interaction.user.id} executed {logvarcmd}")

#Embed
    embed = discord.Embed(title="Start Successfull!", description="Start Vps", color=discord.Color.green())

#Command
    os.system(f"docker start {id}")

    checkveth1 = os.popen(f"bash vethiddocker.sh | grep -i '{id}'")
    checkvethout1 = checkveth1.readlines()
    for checkveth in checkvethout1:
        checkveth = checkveth.strip('\n')
        checkvethdone = checkveth.split(':', 1)[-1]

    os.system(f"wondershaper {checkvethdone} {onstartupnet}")

    await interaction.response.send_message(embed=embed)

############## -STOP VPS- ##############

@client.tree.command(name="stop", description="Allows you to stop your vps")
@commands.has_role(userrole)
async def stopvps(interaction: discord.Interaction):

    logvarcmd = "stopvps"
    print(f"{logs}User {interaction.user.id} executed {logvarcmd}")

#Embed
    embed = discord.Embed(title="Stop Successfull!", description="Stop Vps", color=discord.Color.green())

#Command
    os.system(f"docker kill {idprefix}{interaction.user.id}")
    await interaction.response.send_message(embed=embed)

### -ADMIN STOP VPS- ###

@client.tree.command(name="adminstopvps", description="Allows admins to stop vpses")
@commands.has_role(adminrole)
async def adminstopvps(interaction: discord.Interaction, id: str):

    logvarcmd = "adminstopvps"
    print(f"{logs}User {interaction.user.id} executed {logvarcmd}")

#Embed
    embed = discord.Embed(title="Stop Successfull!", description="Stop Vps", color=discord.Color.green())

#Command
    os.system(f"docker kill {id}")
    await interaction.response.send_message(embed=embed)

############## -RESTART VPS- ##############

@client.tree.command(name="restartvps", description="Allows you to restart your vps")
@commands.has_role(userrole)
async def restartvps(interaction: discord.Interaction):

    logvarcmd = "restartvps"
    print(f"{logs}User {interaction.user.id} executed {logvarcmd}")

#Embed
    embed = discord.Embed(title="Restart Successfull!", description="Restart Vps", color=discord.Color.green())

#Command
    os.system(f"docker kill {idprefix}{interaction.user.id}")
    os.system(f"docker start {idprefix}{interaction.user.id}")

    checkveth1 = os.popen(f"bash vethiddocker.sh | grep -i '{idprefix}{interaction.user.id}'")
    checkvethout1 = checkveth1.readlines()
    for checkveth in checkvethout1:
        checkveth = checkveth.strip('\n')
        checkvethdone = checkveth.split(':', 1)[-1]

    os.system(f"wondershaper {checkvethdone} {onstartupnet}")
    await interaction.response.send_message(embed=embed)

### -ADMIN RESTART VPS- ###

@client.tree.command(name="adminrestartvps", description="Allows admins to restart vpses")
@commands.has_role(adminrole)
async def adminrestartvps(interaction: discord.Interaction, id: str):

    logvarcmd = "adminrestartvps"
    print(f"{logs}User {interaction.user.id} executed {logvarcmd}")

#Embed
    embed = discord.Embed(title="Restart Successfull!", description="Restart Vps", color=discord.Color.green())

#Command
    os.system(f"docker kill {id}")
    os.system(f"docker start {id}")

    checkveth1 = os.popen(f"bash vethiddocker.sh | grep -i '{id}'")
    checkvethout1 = checkveth1.readlines()
    for checkveth in checkvethout1:
        checkveth = checkveth.strip('\n')
        checkvethdone = checkveth.split(':', 1)[-1]

        os.system(f"wondershaper {checkvethdone} {onstartupnet}")
    await interaction.response.send_message(embed=embed)

############## -INFO VPS- ##############

@client.tree.command(name="infovps", description="Allows you to see your vps info")
@commands.has_role(userrole)
async def infovps(interaction: discord.Interaction):


    logvarcmd = "infovps"
    print(f"{logs}User {interaction.user.id} executed {logvarcmd}")

### -Get Current- ###
    await interaction.response.defer() # Fix for NotFoundError: Not Found 404: (10062) 'Unknown interaction'
    try:
        cpu1 = os.popen('docker stats --all --format "{{.CPUPerc}}" --no-stream 'f'{idprefix}{interaction.user.id}')
        cpuout1 = cpu1.readlines()
        for cpu in cpuout1:
            cpu = cpu.strip('\n')
    except:
        cpu = "Unknown"

    try:    
        ram1 = os.popen('docker stats --all --format "{{.MemUsage}}" --no-stream 'f'{idprefix}{interaction.user.id}')
        ramout1 = ram1.readlines()
        for ram in ramout1:
            ram = ram.strip('\n')
    except:
        ram = "Unknown"

    try:
        net1 = os.popen('docker stats --all --format "{{.MemUsage}}" --no-stream 'f'{idprefix}{interaction.user.id}')
        netout1 = net1.readlines()
        for net in netout1:
            net = net.strip('\n')
    except:
        net = "Unknown"

    try:
        checkveth1 = os.popen(f"bash vethiddocker.sh | grep -i '{idprefix}{interaction.user.id}'")
        checkvethout1 = checkveth1.readlines()
        for checkveth in checkvethout1:
            checkveth = checkveth.strip('\n')
            checkvethdone = checkveth.split(':', 1)[-1]
    except:
        checkvethdone = "Unknown"

    try:
        ip1 = os.popen('docker inspect -f "{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}" 'f'{idprefix}{interaction.user.id}')
        ipout1 = ip1.readlines()
        for ip in ipout1:
            ip = ip.strip('\n')
    except:
        ip = "Unknown"

### -Get Limits- ###

    try:
        cpulimit1 = os.popen(f'docker container inspect {idprefix}{interaction.user.id}|grep -i "NanoCpu"')
        cpulimitout1 = cpulimit1.readlines()
        for cpulimit in cpulimitout1:
            cpulimit = cpulimit.strip('\n , "NanoCpus":')

            cpulimit = int(cpulimit)/1000000000 # Get Cores instead of Nano Cores
    except:
        cpulimit = "Unknown"

    try:    
        ramlimit1 = os.popen(f'docker container inspect {idprefix}{interaction.user.id}|grep -i Memory | head -n 1')
        ramlimitout1 = ramlimit1.readlines()
        for ramlimit in ramlimitout1:
            ramlimit = ramlimit.strip('\n , "Memory":')

            ramlimit = round(int(ramlimit)/1024/1024)
    except:
        ramlimit = "Unknown"

    try:    
        swaplimit1 = os.popen(f'docker container inspect {idprefix}{interaction.user.id}|grep -i MemorySwap | head -n 1')
        swaplimitout1 = swaplimit1.readlines()
        for swaplimit in swaplimitout1:
            swaplimit = swaplimit.strip('\n , "MemorySwap":')

            swaplimit = round(int(swaplimit)/1024/1024)
    except:
        swaplimit = "Unknown"

    disklimit = "Unmetered"
    netlimit = onstartupnet

#Desc
    desc = f"""```yaml
ID: {idprefix}{interaction.user.id}
IP: {ip}
Cpu: {cpu}| Core({usercores})
Ram: {ram}
```"""

    embed = discord.Embed(title="Your VpsInfo", description=desc, color=discord.Color.blue())
    embed.add_field(name="Cpu: ", value=f"{cpulimit} Vcore(%)")
    embed.add_field(name="Ram: ", value=f"{ramlimit} MiB")
    embed.add_field(name="Swap: ", value=f"{swaplimit} MiB")
    embed.add_field(name="Disk: ", value=f"{disklimit}")
    embed.add_field(name="Net⇂↿: ", value=f"{netlimit}")
    await interaction.followup.send(embed=embed)

### -ADMIN INFO VPS- ###

@client.tree.command(name="admininfovps", description="Allows admins to see other vpses info")
@commands.has_role(userrole)
async def admininfovps(interaction: discord.Interaction, id: str):


    logvarcmd = "admininfovps"
    print(f"{logs}User {interaction.user.id} executed {logvarcmd}")

### -Get Current- ###
    await interaction.response.defer() # Fix for NotFoundError: Not Found 404: (10062) 'Unknown interaction'
    try:
        cpu1 = os.popen('docker stats --all --format "{{.CPUPerc}}" --no-stream 'f'{id}')
        cpuout1 = cpu1.readlines()
        for cpu in cpuout1:
            cpu = cpu.strip('\n')
    except:
        cpu = "Unknown"

    try:    
        ram1 = os.popen('docker stats --all --format "{{.MemUsage}}" --no-stream 'f'{id}')
        ramout1 = ram1.readlines()
        for ram in ramout1:
            ram = ram.strip('\n')
    except:
        ram = "Unknown"

    try:
        net1 = os.popen('docker stats --all --format "{{.MemUsage}}" --no-stream 'f'{id}')
        netout1 = net1.readlines()
        for net in netout1:
            net = net.strip('\n')
    except:
        net = "Unknown"

    try:
        checkveth1 = os.popen(f"bash vethiddocker.sh | grep -i '{id}'")
        checkvethout1 = checkveth1.readlines()
        for checkveth in checkvethout1:
            checkveth = checkveth.strip('\n')
            checkvethdone = checkveth.split(':', 1)[-1]
    except:
        checkvethdone = "Unknown"

    try:
        ip1 = os.popen('docker inspect -f "{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}" 'f'{id}')
        ipout1 = ip1.readlines()
        for ip in ipout1:
            ip = ip.strip('\n')
    except:
        ip = "Unknown"

### -Get Limits- ###

    try:
        cpulimit1 = os.popen(f'docker container inspect {id}|grep -i "NanoCpu"')
        cpulimitout1 = cpulimit1.readlines()
        for cpulimit in cpulimitout1:
            cpulimit = cpulimit.strip('\n , "NanoCpus":')

            cpulimit = int(cpulimit)/1000000000 # Get Cores instead of Nano Cores
    except:
        cpulimit = "Unknown"

    try:    
        ramlimit1 = os.popen(f'docker container inspect {id}|grep -i Memory | head -n 1')
        ramlimitout1 = ramlimit1.readlines()
        for ramlimit in ramlimitout1:
            ramlimit = ramlimit.strip('\n , "Memory":')

            ramlimit = round(int(ramlimit)/1024/1024)
    except:
        ramlimit = "Unknown"

    try:    
        swaplimit1 = os.popen(f'docker container inspect {id}|grep -i MemorySwap | head -n 1')
        swaplimitout1 = swaplimit1.readlines()
        for swaplimit in swaplimitout1:
            swaplimit = swaplimit.strip('\n , "MemorySwap":')

            swaplimit = round(int(swaplimit)/1024/1024)
    except:
        swaplimit = "Unknown"

    disklimit = "Unmetered"
    netlimit = onstartupnet

#Desc
    desc = f"""```yaml
ID: {id}
IP: {ip}
Cpu: {cpu}| Core({usercores})
Ram: {ram}
```"""

    embed = discord.Embed(title="Your VpsInfo", description=desc, color=discord.Color.blue())
    embed.add_field(name="Cpu: ", value=f"{cpulimit} Vcore(%)")
    embed.add_field(name="Ram: ", value=f"{ramlimit} MiB")
    embed.add_field(name="Swap: ", value=f"{swaplimit} MiB")
    embed.add_field(name="Disk: ", value=f"{disklimit}")
    embed.add_field(name="Net⇂↿: ", value=f"{netlimit}")
    await interaction.followup.send(embed=embed)

############## -NODE INFO- ##############
@client.tree.command(name="nodeinfo", description="Allows you to see node usage")
@commands.has_role(userrole)
#@commands.check(commandchannelid)
async def nodeinfo(interaction: discord.Interaction):

    logvarcmd = "nodeinfo"
    print(f"{logs}User {interaction.user.id} executed {logvarcmd}")

#Useless vars
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    swap = psutil.swap_memory().percent
    total = (round(ram + swap))/2

    try:
        temp1 = os.popen("vcgencmd measure_temp") # Change for your device!
        tempout1 = temp1.readlines()
        for tempout in tempout1:
            tempout = tempout.strip("\n temp= ' C")

    except:
        tempout = "-"
    
    try:
        fan1 = os.popen("sensors | grep Processor")
        fanout1 = fan1.readlines()
        for fanout in fanout1:
            fanout = fanout.strip("\n Processor Fan:")
    except:
        fanout = "-"

    def uptimeseconds():
        return time.time() - psutil.boot_time()
    uptime = (round(uptimeseconds() / 3600))

    vpsnum1 = os.popen(f'docker ps -a -q | wc -l') # Use | grep -i {idprefix} -c to only get containers created by the bot
    vpsnumout1 = vpsnum1.readlines()
    for vpsnumout in vpsnumout1:
        vpsnumout = vpsnumout.strip("\n")

    vpsactive1 = os.popen(f'docker ps -q | wc -l') # Use | grep -i {idprefix} -c to only get containers created by the bot
    vpsactiveout1 = vpsactive1.readlines()
    for vpsactiveout in vpsactiveout1:
        vpsactiveout = vpsactiveout.strip("\n")

    vpsinactive1 = os.popen(f'docker ps -a -q -f "status=exited" | wc -l') # Use | grep -i {idprefix} -c to only get containers created by the bot
    vpsinactiveout1 = vpsinactive1.readlines()
    for vpsinactiveout in vpsinactiveout1:
        vpsinactiveout = vpsinactiveout.strip("\n")

    getos1 = os.popen("screenfetch -nN | grep -i 'OS'")
    getosout1 = getos1.readlines()
    for getosout in getosout1:
        getosout = getosout.strip("\n")

    getcpu1 = os.popen("screenfetch -nN | grep -i 'CPU'")
    getcpuout1 = getcpu1.readlines()
    for getcpuout in getcpuout1:
        getcpuout = getcpuout.strip("\n")

    getram1 = os.popen("screenfetch -nN | grep -i 'RAM'")
    getramout1 = getram1.readlines()
    for getramout in getramout1:
        getramout = getramout.strip("\n")

    getuptime1 = os.popen("screenfetch -nN | grep -i 'Uptime'")
    getuptimeout1 = getuptime1.readlines()
    for getuptimeout in getuptimeout1:
        getuptimeout = getuptimeout.strip("\n")
    
    desc = f"""```yaml
{getosout}
{getcpuout}
{getramout}
{getuptimeout}
```"""
#Embed
    embed = discord.Embed(title=f"Node Info - {devicename}", description=desc, color=discord.Color.purple())
    embed.add_field(name="**CPU**", value=f"{cpu}%")
    embed.add_field(name="**RAM**", value=f"{total}%")
    embed.add_field(name="**TEMP**", value=f"-")
    embed.add_field(name="**FAN**", value=f"-")
    embed.add_field(name="**UPTIME**", value=f"{uptime} Hours")
    embed.add_field(name="**INSTANCES**", value=f"{vpsnumout}")
    embed.add_field(name="**ACTIVE**", value=f"{vpsactiveout}")
    embed.add_field(name="**INACTIVE**", value=f"{vpsinactiveout}")
    embed.add_field(name="**LIMIT**", value=f"{vpslimit}")
    await interaction.response.send_message(embed=embed)

client.run(config['Config']['token'])
