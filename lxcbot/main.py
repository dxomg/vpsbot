import discord
import os
import sys
import psutil
import time
import re
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix="-", intents=intents)
client.remove_command('help')
version = "1.5"

reqchannel = client.get_channel(1013904571376095333)

logs = "[LOGS] "
logstofile = "false" #Should we save the logs?
adminrole = "Admin" #Admin Rolename
modrole = "Mod" #Mod Rolename
donatorrole = "Donator" #Donator Rolename
#Giveaway Rolename & Rewards (MiB)
giveaway3 = "1024"
giveaway2 = "512"
giveaway1 = "248"
userrole = "User" #User Rolename (If user dosent have role commands wont work)
suspendedrole = "Suspended" #Not Working
#this will only allow command execution on specific channels
cmdchid = 0000000000000000000 #Change!!!
idprefix = "bot" #ID PREFIX
deleteleave = "true" #Not Working
lxcips = "10." #Do not Change!!
onstartupnet = "50000 50000" #Default Global Network Limit (Kbps) 
modperk = "512"
donatorperk = "512"
#Limit of User Creations (bypassable by ADMIN creation)
vpslimit = 50


#User Creation Options
usercpu = "1" #Vcores
userram = "128" #MiB
userdisk = "5" #GiB
if logstofile == "true":
    sys.stdout = open('/root/lxcbot/logs.txt', 'w')

os.spawnlp(os.P_NOWAIT, "/root/lxcbot/webserver.py", "webserver.py")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="-help"))
    print("")
    os.system("lxc list -f csv")
    print("")
    print(logs + "Containers List Loaded")
    print("")
    print(logs + "Bot Loaded Successfully!")

#Function to check if channel is cmdchid
async def commandchannelid(ctx):
    return ctx.channel.id == cmdchid

@client.event
async def on_member_remove(member):
    if deleteleave == "true":
        os.system(f"lxc delete {member.id} --force")

########################################################## - Help Command \/

@client.command()
@commands.has_role(userrole)
@commands.check(commandchannelid)
async def help(ctx):

    logvarcmd = "help"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")
#Embed

    embed = discord.Embed(title="Help", description="Prefix (-)", color=discord.Color.blue())
    embed.add_field(name="createvps (ubuntu/debian/archlinux/alpine)", value=f"Allows you to create 1 vps")
    embed.add_field(name="startvps", value=f"Allows you to manage your vps")
    embed.add_field(name="stopvps", value=f"Allows you to manage your vps")
    embed.add_field(name="restartvps", value=f"Allows you to manage your vps")
    embed.add_field(name="deletevps", value=f"Allows you to delete your vps")
    embed.add_field(name="regenpass", value=f"Re-Generate vps password")
    embed.add_field(name="infovps", value=f"Allows you to see the current Status of your vps")
    embed.add_field(name="nodeinfo", value=f"Allows you to see the current usage of the node")
    embed.add_field(name="modperks", value=f"This command applies the Moderator perks")
    embed.add_field(name="donatorperks", value=f"This command applies the Donator perks")
    embed.add_field(name="help", value=f"This Command")
    embed.set_footer(text = f"Version: {version}")
    await ctx.reply(embed=embed)

########################################################## - Help Command CN version \/

@client.command()
@commands.has_role(userrole)
@commands.check(commandchannelid)
async def helpcn(ctx):

    logvarcmd = "helpcn"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")
#Embed

    embed = discord.Embed(title="Help", description="Prefix (-)", color=discord.Color.blue())
    embed.add_field(name="createvps (ubuntu/debian/archlinux/alpine)", value=f"允许你创建1个vps")
    embed.add_field(name="startvps", value=f"允许你启动你的vps")
    embed.add_field(name="stopvps", value=f"允许你停止你的vps")
    embed.add_field(name="restartvps", value=f"允许你重新启动你的vps")
    embed.add_field(name="deletevps", value=f"允许你删除你的vps")
    embed.add_field(name="infovps", value=f"允许你看到你的vps的当前状态。")
    embed.add_field(name="nodeinfo", value=f"允许你查看节点的当前使用情况")
    embed.add_field(name="helpcn", value=f"该命令")
    embed.set_footer(text = f"Version: {version}")
    await ctx.reply(embed=embed)

########################################################## - Help Command RU version \/

@client.command()
@commands.has_role(userrole)
@commands.check(commandchannelid)
async def helpru(ctx):

    logvarcmd = "helpru"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")
#Embed

    embed = discord.Embed(title="Help", description="Префикс (-)", color=discord.Color.blue())
    embed.add_field(name="createvps (ubuntu/debian/archlinux/alpine)", value=f"Позволяет вам создать 1 VPS")
    embed.add_field(name="startvps", value=f"Позволяет вам запустить ваш")
    embed.add_field(name="stopvps", value=f"Позволяет вам остановить ваш VPS")
    embed.add_field(name="restartvps", value=f"Позволяет вам перезагрузить ваш VPS")
    embed.add_field(name="deletevps", value=f"Позволяет вам удалить ваш VPS")
    embed.add_field(name="infovps", value=f"Позволяет вам посмотреть статус вашего VPS")
    embed.add_field(name="nodeinfo", value=f"Позволяет посмотреть вам использование ресурсов ноды")
    embed.add_field(name="helpru", value=f"Эта команда")
    embed.set_footer(text = f"Version: {version}")
    await ctx.reply(embed=embed)

########################################################## - Help Command ES version \/

@client.command()
@commands.has_role(userrole)
@commands.check(commandchannelid)
async def helpes(ctx):

    logvarcmd = "helpes"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")
#Embed

    embed = discord.Embed(title="Help", description="Prefijo (-)", color=discord.Color.blue())
    embed.add_field(name="createvps (ubuntu/debian/archlinux/alpine)", value=f"Te permite crear 1 VPS")
    embed.add_field(name="startvps", value=f"Te permite iniciar tu VPS")
    embed.add_field(name="stopvps", value=f"Te permite parar tu VPS")
    embed.add_field(name="restartvps", value=f"Te permite reiniciar tu VPS")
    embed.add_field(name="deletevps", value=f"Te permite eliminar tu VPS")
    embed.add_field(name="infovps", value=f"Te permite el estado actual de tu VPS")
    embed.add_field(name="nodeinfo", value=f"Te permite ver el uso actual del nodo")
    embed.add_field(name="helpes", value=f"Este comando")
    embed.set_footer(text = f"Version: {version}")
    await ctx.reply(embed=embed)

########################################################## - Help Command FR version \/

@client.command()
@commands.has_role(userrole)
@commands.check(commandchannelid)
async def helpfr(ctx):

    logvarcmd = "helpfr"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")
#Embed

    embed = discord.Embed(title="Help", description="Préfixe (-)", color=discord.Color.blue())
    embed.add_field(name="createvps (ubuntu/debian/archlinux/alpine)", value=f"Vous permet de créer 1 VPS")
    embed.add_field(name="startvps", value=f"Vous permet de démarrer votre VPS")
    embed.add_field(name="stopvps", value=f"Vous permet d'arrêter votre VPS")
    embed.add_field(name="restartvps", value=f"Permet de redémarrer votre VPS")
    embed.add_field(name="deletevps", value=f"Vous permet de supprimer votre VPS")
    embed.add_field(name="infovps", value=f"Permet de voir le statut actuel de votre VPS")
    embed.add_field(name="nodeinfo", value=f"Permet de voir l'état actuel du nœud")
    embed.add_field(name="helpfr", value=f"Cette commande")
    embed.set_footer(text = f"Version: {version}")
    await ctx.reply(embed=embed)

########################################################## - Make a Port Request \/
@client.command()
@commands.check(commandchannelid)
async def portreq(ctx, msgrequest):

    logvarcmd = "portreq"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")
#Embed
    embed = discord.Embed(title="Request Sent!", description=f"Message: {msgrequest}", color=discord.Color.blue())
    reqembed = discord.Embed(title="Message Recieved!", description=f"Message: {msgrequest}", color=discord.Color.blue())
    await ctx.send(embed=embed)
    await reqchannel.send(embed=reqembed)
########################################################## - Create a Vps Command & Images \/
@client.command()
@commands.has_role(userrole)
@commands.check(commandchannelid)
async def createvps(ctx, image):

    logvarcmd = "createvps"

#Embed Template

    desc = f"""```yaml
ID: {idprefix}{ctx.author.id}
OS: {image}
----------------------
Cpu: {usercpu} Vcores
Ram: {userram} MiB
Disk: {userdisk} GiB
Net: {onstartupnet} Kibps
----------------------```"""

    embed = discord.Embed(title="Creation Successfull!", description=desc, color=discord.Color.green())
# Get Count of Current vpses
    vpscurrent1 = os.popen("lxc list -f csv | grep CONTAINER -c")
    vpscurrentout1 = vpscurrent1.readlines()
    for vpscurrent in vpscurrentout1:
        vpscurrent = vpscurrent.strip("\n")
#Images

    alpine = "alpine/3.16"
    archlinux = "archlinux"
    ubuntu = "ubuntu/jammy"
    debian = "debian/11"
#Reply user fetching {using discord API!}
    user = await client.fetch_user(ctx.author.id)

    if image == "alpine" and int(vpscurrent) <= vpslimit:
        print(f"{logs}User {ctx.author.id} executed {logvarcmd}")
        await ctx.reply("Creating...")
        os.system(f"lxc launch images:{alpine} {idprefix}{ctx.author.id} -c limits.cpu={usercpu} -c limits.memory={userram}MiB && lxc config device override {idprefix}{ctx.author.id} root size={userdisk}GB")
    #Check for veth from id
        checkveth1 = os.popen(f"lxc config show {idprefix}{ctx.author.id} | grep -i 'veth'")
        checkvethout1 = checkveth1.readlines()
        for checkveth in checkvethout1:
            checkveth = checkveth.strip('\n')
            checkvethdone = checkveth.split(':', 1)[-1]
        os.system(f"wondershaper {checkvethdone} {onstartupnet}")
    #Set password to container
        passgen1 = os.popen(f"bash /root/lxcbot/passgen.sh")
        passgenout1 = passgen1.readlines()
        for passgen in passgenout1:
            passgen = passgen.strip('\n')

        os.system("rm .ssh/known_hosts") # Remove known_hosts file to prevent Bad Host Key error from paramiko in web panel
        os.system(f"lxc exec {idprefix}{ctx.author.id} -- apk add openssh-server")
        os.system(f"lxc exec {idprefix}{ctx.author.id} -- apk add openssh-server")
        os.system(f"lxc exec {idprefix}{ctx.author.id} -- wget -O /etc/ssh/sshd_config https://raw.githubusercontent.com/dxomg/sshd_config/main/sshd_config")
        os.system(f"lxc exec {idprefix}{ctx.author.id} -- service sshd restart")
        os.system(f"lxc exec {idprefix}{ctx.author.id} -- sh -c 'echo 'root:{passgen}' | chpasswd'")
        await user.send(f"""```yaml
User: root
Password: {passgen}

- to get ip do -infovps```
Panel: http://panel.vpsbot.ml:8888/""")
        await ctx.reply(embed=embed)

    elif image == "archlinux" and int(vpscurrent) <= vpslimit:
        print(f"{logs}User {ctx.author.id} executed {logvarcmd}")
        await ctx.reply("Creating...")
        os.system(f"lxc launch images:{archlinux} {idprefix}{ctx.author.id} -c limits.cpu={usercpu} -c limits.memory={userram}MiB && lxc config device override {idprefix}{ctx.author.id} root size={userdisk}GB && lxc config device override {idprefix}{ctx.author.id} root size={userdisk}GB") #Double execution else it dosent work, dunno why
    #Check for veth from id
        checkveth1 = os.popen(f"lxc config show {idprefix}{ctx.author.id} | grep -i 'veth'")
        checkvethout1 = checkveth1.readlines()
        for checkveth in checkvethout1:
            checkveth = checkveth.strip('\n')
            checkvethdone = checkveth.split(':', 1)[-1]
        os.system(f"wondershaper {checkvethdone} {onstartupnet}")
    #Set password to container
        passgen1 = os.popen(f"bash /root/lxcbot/passgen.sh")
        passgenout1 = passgen1.readlines()
        for passgen in passgenout1:
            passgen = passgen.strip('\n')

        os.system("rm .ssh/known_hosts") # Remove known_hosts file to prevent Bad Host Key error from paramiko in web panel
        os.system(f"lxc exec {idprefix}{ctx.author.id} -- sh -c 'echo -e Y | pacman -S openssh wget'")
        os.system(f"lxc exec {idprefix}{ctx.author.id} -- wget -O /etc/ssh/sshd_config https://raw.githubusercontent.com/dxomg/sshd_config/main/sshd_config")
        os.system(f"lxc exec {idprefix}{ctx.author.id} -- systemctl restart sshd")
        os.system(f"lxc exec {idprefix}{ctx.author.id} -- sh -c 'echo 'root:{passgen}' | chpasswd'")
        await user.send(f"""```yaml
User: root
Password: {passgen}

- to get ip do -infovps```
Panel: http://panel.vpsbot.ml:8888/""")
        await ctx.reply(embed=embed)

    elif image == "debian" and int(vpscurrent) <= vpslimit:
        print(f"{logs}User {ctx.author.id} executed {logvarcmd}")
        await ctx.reply("Creating...")
        os.system(f"lxc launch images:{debian} {idprefix}{ctx.author.id} -c limits.cpu={usercpu} -c limits.memory={userram}MiB && lxc config device override {idprefix}{ctx.author.id} root size={userdisk}GB")
    #Check for veth from id
        checkveth1 = os.popen(f"lxc config show {idprefix}{ctx.author.id} | grep -i 'veth'")
        checkvethout1 = checkveth1.readlines()
        for checkveth in checkvethout1:
            checkveth = checkveth.strip('\n')
            checkvethdone = checkveth.split(':', 1)[-1]
        os.system(f"wondershaper {checkvethdone} {onstartupnet}")
    #Set password to container
        passgen1 = os.popen(f"bash /root/lxcbot/passgen.sh")
        passgenout1 = passgen1.readlines()
        for passgen in passgenout1:
            passgen = passgen.strip('\n')

        os.system("rm .ssh/known_hosts") # Remove known_hosts file to prevent Bad Host Key error from paramiko in web panel
        os.system(f"lxc exec {idprefix}{ctx.author.id} -- apt install -qq openssh-server wget -y")
        os.system(f"lxc exec {idprefix}{ctx.author.id} -- wget -O /etc/ssh/sshd_config https://raw.githubusercontent.com/dxomg/sshd_config/main/sshd_config")
        os.system(f"lxc exec {idprefix}{ctx.author.id} -- systemctl restart sshd")
        os.system(f"lxc exec {idprefix}{ctx.author.id} -- sh -c 'echo 'root:{passgen}' | chpasswd'")
        await user.send(f"""```yaml
User: root
Password: {passgen}

- to get ip do -infovps```
Panel: http://panel.vpsbot.ml:8888/""")
        await ctx.reply(embed=embed)

    elif image == "ubuntu" and int(vpscurrent) <= vpslimit:
        print(f"{logs}User {ctx.author.id} executed {logvarcmd}")
        await ctx.reply("Creating...")
        os.system(f"lxc launch images:{ubuntu} {idprefix}{ctx.author.id} -c limits.cpu={usercpu} -c limits.memory={userram}MiB && lxc config device override {idprefix}{ctx.author.id} root size={userdisk}GB")
    #Check for veth from id
        checkveth1 = os.popen(f"lxc config show {idprefix}{ctx.author.id} | grep -i 'veth'")
        checkvethout1 = checkveth1.readlines()
        for checkveth in checkvethout1:
            checkveth = checkveth.strip('\n')
            checkvethdone = checkveth.split(':', 1)[-1]
        os.system(f"wondershaper {checkvethdone} {onstartupnet}")
    #Set password to container
        passgen1 = os.popen(f"bash /root/lxcbot/passgen.sh")
        passgenout1 = passgen1.readlines()
        for passgen in passgenout1:
            passgen = passgen.strip('\n')


        os.system("rm .ssh/known_hosts") # Remove known_hosts file to prevent Bad Host Key error from paramiko in web panel
        os.system(f"lxc exec {idprefix}{ctx.author.id} -- apt install -qq openssh-server wget -y")
        os.system(f"lxc exec {idprefix}{ctx.author.id} -- wget -O /etc/ssh/sshd_config https://raw.githubusercontent.com/dxomg/sshd_config/main/sshd_config")
        os.system(f"lxc exec {idprefix}{ctx.author.id} -- systemctl restart sshd")
        os.system(f"lxc exec {idprefix}{ctx.author.id} -- sh -c 'echo 'root:{passgen}' | chpasswd'")
        await user.send(f"""```yaml
User: root
Password: {passgen}

- to get ip do -infovps```
Panel: http://panel.vpsbot.ml:8888/""")
        await ctx.reply(embed=embed)
    else:
        await ctx.reply(f"Incorrect Image Name or Vps Limit Reached ({vpslimit})")

############################# ADMIN version - \/

@client.command()
@commands.has_role(adminrole)
async def admincreatevps(ctx, id, image, cpu, ram, disk, up, down):

    logvarcmd = "admincreatevps"

#Options {don't change for admin}
    usercpu = cpu
    userram = ram
    userdisk = disk

    desc = f"""```yaml
ID: {id}
OS: {image}
----------------------
Cpu: {cpu} Vcores
Ram: {ram} MiB
Disk: {disk} GiB
Net: {up} {down} Kibps
----------------------```"""

#Embed Template

    embed = discord.Embed(title="Creation Successfull!", description=desc, color=discord.Color.green())

#Images

    alpine = "alpine/3.16"
    archlinux = "archlinux"
    ubuntu = "ubuntu/jammy"
    debian = "debian/11"

    if image == "alpine":
        print(f"{logs}User {ctx.author.id} executed {logvarcmd}")
        await ctx.reply("Creating...")
        os.system(f"lxc launch images:{alpine} {id} -c limits.cpu={usercpu} -c limits.memory={userram}MiB && lxc config device override {id} root size={userdisk}GB")
    #Check for veth from id
        checkveth1 = os.popen(f"lxc config show {id} | grep -i 'veth'")
        checkvethout1 = checkveth1.readlines()
        for checkveth in checkvethout1:
            checkveth = checkveth.strip('\n')
            checkvethdone = checkveth.split(':', 1)[-1]
        os.system(f"wondershaper {checkvethdone} {up} {down}")


        os.system("rm .ssh/known_hosts") # Remove known_hosts file to prevent Bad Host Key error from paramiko in web panel
        await ctx.reply(embed=embed)

    elif image == "archlinux":
        print(f"{logs}User {ctx.author.id} executed {logvarcmd}")
        await ctx.reply("Creating...")
        os.system(f"lxc launch images:{archlinux} {id} -c limits.cpu={usercpu} -c limits.memory={userram}MiB && lxc config device override {id} root size={userdisk}GB && lxc config device override {id} root size={userdisk}GB") #Double execution else it dosent work, dunno why
    #Check for veth from id
        checkveth1 = os.popen(f"lxc config show {id} | grep -i 'veth'")
        checkvethout1 = checkveth1.readlines()
        for checkveth in checkvethout1:
            checkveth = checkveth.strip('\n')
            checkvethdone = checkveth.split(':', 1)[-1]
        os.system(f"wondershaper {checkvethdone} {up} {down}")


        os.system("rm .ssh/known_hosts") # Remove known_hosts file to prevent Bad Host Key error from paramiko in web panel
        await ctx.reply(embed=embed)

    elif image == "debian":
        print(f"{logs}User {ctx.author.id} executed {logvarcmd}")
        await ctx.reply("Creating...")
        os.system(f"lxc launch images:{debian} {id} -c limits.cpu={usercpu} -c limits.memory={userram}MiB && lxc config device override {id} root size={userdisk}GB")
    #Check for veth from id
        checkveth1 = os.popen(f"lxc config show {id} | grep -i 'veth'")
        checkvethout1 = checkveth1.readlines()
        for checkveth in checkvethout1:
            checkveth = checkveth.strip('\n')
            checkvethdone = checkveth.split(':', 1)[-1]
        os.system(f"wondershaper {checkvethdone} {up} {down}")


        os.system("rm .ssh/known_hosts") # Remove known_hosts file to prevent Bad Host Key error from paramiko in web panel
        await ctx.reply(embed=embed)

    elif image == "ubuntu":
        print(f"{logs}User {ctx.author.id} executed {logvarcmd}")
        await ctx.reply("Creating...")
        os.system(f"lxc launch images:{ubuntu} {id} -c limits.cpu={usercpu} -c limits.memory={userram}MiB && lxc config device override {id} root size={userdisk}GB")
    #Check for veth from id
        checkveth1 = os.popen(f"lxc config show {id} | grep -i 'veth'")
        checkvethout1 = checkveth1.readlines()
        for checkveth in checkvethout1:
            checkveth = checkveth.strip('\n')
            checkvethdone = checkveth.split(':', 1)[-1]
        os.system(f"wondershaper {checkvethdone} {up} {down}")


        os.system("rm .ssh/known_hosts") # Remove known_hosts file to prevent Bad Host Key error from paramiko in web panel
        await ctx.reply(embed=embed)

    else:
        await ctx.reply("Incorrect Image Name")

########################################################## - Machine Info Command \/

@client.command()
@commands.has_role(userrole)
@commands.check(commandchannelid)
async def nodeinfo(ctx):

    logvarcmd = "nodeinfo"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")

#Useless vars
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    swap = psutil.swap_memory().percent
    total = (round(ram + swap))/2

    


    temp1 = os.popen("sensors | grep CPU:")
    tempout1 = temp1.readlines()
    for tempout in tempout1:
        tempout = tempout.strip("\n CPU: +")

    fan1 = os.popen("sensors | grep Processor")
    fanout1 = fan1.readlines()
    for fanout in fanout1:
        fanout = fanout.strip("\n Processor Fan:")

    def uptimeseconds():
        return time.time() - psutil.boot_time()
    uptime = (round(uptimeseconds() / 3600))

    vpsnum1 = os.popen("lxc list -f csv | grep CONTAINER -c")
    vpsnumout1 = vpsnum1.readlines()
    for vpsnumout in vpsnumout1:
        vpsnumout = vpsnumout.strip("\n")

    vpsactive1 = os.popen("lxc list -f csv | grep RUNNING -c")
    vpsactiveout1 = vpsactive1.readlines()
    for vpsactiveout in vpsactiveout1:
        vpsactiveout = vpsactiveout.strip("\n")

    vpsinactive1 = os.popen("lxc list -f csv | grep STOPPED -c")
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
    embed = discord.Embed(title="Node Info", description=desc, color=discord.Color.purple())
    embed.add_field(name="**CPU**", value=f"{cpu}%")
    embed.add_field(name="**RAM**", value=f"{total}%")
    try:
        embed.add_field(name="**TEMP**", value=f"{tempout}")
    except:
        embed.add_field(name="**TEMP**", value=f"-")


    try:
        embed.add_field(name="**FAN**", value=f"{fanout}")
    except:
        embed.add_field(name="**FAN**", value=f"-")


    embed.add_field(name="**UPTIME**", value=f"{uptime} Hours")
    embed.add_field(name="**INSTANCES**", value=f"{vpsnumout}")
    embed.add_field(name="**ACTIVE**", value=f"{vpsactiveout}")
    embed.add_field(name="**INACTIVE**", value=f"{vpsinactiveout}")
    embed.add_field(name="**LIMIT**", value=f"{vpslimit}")
    await ctx.reply(embed=embed)


########################################################## - Start Vps Command \/

@client.command()
@commands.has_role(userrole)
@commands.check(commandchannelid)
async def startvps(ctx):

    logvarcmd = "startvps"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")

#Embed
    embed = discord.Embed(title="Start Successfull!", description="Start Vps", color=discord.Color.green())


#Command

    os.system(f"lxc start {idprefix}{ctx.author.id}")

#Check for veth from id
    checkveth1 = os.popen(f"lxc config show {idprefix}{ctx.author.id} | grep -i 'veth'")
    checkvethout1 = checkveth1.readlines()
    for checkveth in checkvethout1:
        checkveth = checkveth.strip('\n')
    checkvethdone = checkveth.split(':', 1)[-1]

    os.system(f"wondershaper {checkvethdone} {onstartupnet}")

    await ctx.reply(embed=embed)

############################# ADMIN version - \/

@client.command()
@commands.has_role(adminrole)
async def adminstartvps(ctx, id):

    logvarcmd = "adminstartvps"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")

#Embed
    embed = discord.Embed(title="Start Successfull!", description="Start Vps", color=discord.Color.green())


#Command
    os.system(f"lxc start {id}")
    #Check for veth from id
    checkveth1 = os.popen(f"lxc config show {idprefix}{ctx.author.id} | grep -i 'veth'")
    checkvethout1 = checkveth1.readlines()
    for checkveth in checkvethout1:
        checkveth = checkveth.strip('\n')
    checkvethdone = checkveth.split(':', 1)[-1]
    os.system(f"wondershaper {checkvethdone} {onstartupnet}")

    await ctx.reply(embed=embed)

########################################################## - Stop Vps Command \/
@client.command()
@commands.has_role(userrole)
@commands.check(commandchannelid)
async def stopvps(ctx):

    logvarcmd = "stopvps"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")
#Embed
    embed = discord.Embed(title="Stop Successfull!", description="Stop Vps", color=discord.Color.green())


#Command
    os.system(f"lxc stop {idprefix}{ctx.author.id}")

    await ctx.reply(embed=embed)

############################# ADMIN version - \/

@client.command()
@commands.has_role(adminrole)
async def adminstopvps(ctx, id):

    logvarcmd = "adminstopvps"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")

#Embed
    embed = discord.Embed(title="Stop Successfull!", description="Stop Vps", color=discord.Color.green())


#Command
    os.system(f"lxc stop {id}")

    await ctx.reply(embed=embed)

########################################################## - Restart Vps Command \/
@client.command()
@commands.has_role(userrole)
@commands.check(commandchannelid)
async def restartvps(ctx):

    logvarcmd = "restartvps"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")

#Embed
    embed = discord.Embed(title="Restart Successfull!", description="Restart Vps", color=discord.Color.green())


#Command
    os.system(f"lxc stop {idprefix}{ctx.author.id}")
    os.system(f"lxc start {idprefix}{ctx.author.id}")

    await ctx.reply(embed=embed)

############################# ADMIN version - \/

@client.command()
@commands.has_role(adminrole)
async def adminrestartvps(ctx, id):

    logvarcmd = "adminrestartvps"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")

#Embed
    embed = discord.Embed(title="Restart Successfull!", description="Restart Vps", color=discord.Color.green())


#Command
    os.system(f"lxc stop {id}")
    os.system(f"lxc start {id}")

    await ctx.reply(embed=embed)

########################################################## - Delete Vps Command \/
@client.command()
@commands.has_role(userrole)
@commands.check(commandchannelid)
async def deletevps(ctx):

    logvarcmd = "deletevps"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")

#Embed
    embed = discord.Embed(title="Delete Successfull!", description="Delete Vps", color=discord.Color.green())


#Command
    os.system(f"lxc delete {idprefix}{ctx.author.id} --force")

    await ctx.reply(embed=embed)

############################# ADMIN version - \/

@client.command()
@commands.has_role(adminrole)
async def admindeletevps(ctx, id):

    logvarcmd = "admindeletevps"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")

#Embed
    embed = discord.Embed(title="Delete Successfull!", description="Delete Vps", color=discord.Color.green())


#Command
    os.system(f"lxc delete {id} --force")

    await ctx.reply(embed=embed)

########################################################## - Information Vps Command \/
@client.command()
@commands.has_role(userrole)
@commands.check(commandchannelid)
async def infovps(ctx):

    logvarcmd = "infovps"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")

#Command
    infocpu1 = os.popen(f"lxc config show {idprefix}{ctx.author.id} | grep limits.cpu ")
    infocpuout1 = infocpu1.readlines()
    for infocpu in infocpuout1:
        infocpu = infocpu.strip('\n limits.cpu: "')

    infomem1 = os.popen(f"lxc config show {idprefix}{ctx.author.id} | grep limits.memory ")
    infomemout1 = infomem1.readlines()
    for infomem in infomemout1:
        infomem = infomem.strip('\n limits.memory:')

    infodisk1 = os.popen(f"lxc config show {idprefix}{ctx.author.id} | grep size ")
    infodiskout1 = infodisk1.readlines()
    for infodisk in infodiskout1:
        infodisk = infodisk.strip('\n size: GB ')

    inforunning1 = os.popen(f"lxc info --resources {idprefix}{ctx.author.id} | grep Status")
    inforunningout1 = inforunning1.readlines()
    for inforunning in inforunningout1:
        inforunning = inforunning.strip('\n')

    #infoccpu1 = os.popen(f"lxc info --resources {idprefix}{ctx.author.id} | grep -i 'CPU usage (in seconds):'")
    #infoccpuout1 = infoccpu1.readlines()
    #for infoccpu in infoccpuout1:
    #    infoccpu = infoccpu.strip('\n CPU usage (in seconds):')

    #infoccpun = round(int(infoccpu)/(60*1))

    infocreated1 = os.popen(f"lxc info --resources {idprefix}{ctx.author.id} | grep -i 'Created:'")
    infocreatedout1 = infocreated1.readlines()
    for infocreated in infocreatedout1:
        infocreated = infocreated.strip('\n Created: UT')

    if inforunning == "Status: STOPPED": # Stupid fix for UnboundLocalError
        infolocalip = "Offline"
        infocmem = "Offline"
        checkvethdone = "Offline"
        checknetlimitdone = "Offline"

    else:
        infolocalip1 = os.popen(f"lxc info --resources {idprefix}{ctx.author.id} | grep -i '{lxcips}'")
        infolocalipout1 = infolocalip1.readlines()
        for infolocalip in infolocalipout1:
            infolocalip = infolocalip.strip('\n inet: (global)')
        infolocalip = infolocalip.split('/', 1)[0]

        infocmem1 = os.popen(f"lxc info --resources {idprefix}{ctx.author.id} | grep -i 'Memory (current):'")
        infocmemout1 = infocmem1.readlines()
        for infocmem in infocmemout1:
            infocmem = infocmem.strip('\n Memory (current):')

    #Check for veth from id
        checkveth1 = os.popen(f"lxc config show {idprefix}{ctx.author.id} | grep -i 'veth'")
        checkvethout1 = checkveth1.readlines()
        for checkveth in checkvethout1:
            checkveth = checkveth.strip('\n')
        checkvethdone = checkveth.split(':', 1)[-1]

    #Check Network limits
        try:   
            checknetlimit1 = os.popen(f"wondershaper {checkvethdone} | grep -i 'prio 1'")
            checknetlimitout1 = checknetlimit1.readlines()
            for checknetlimit in checknetlimitout1:
                checknetlimit = checknetlimit.strip('\n rate')
            checknetlimitdone = checknetlimit.split('rate', 1)[-1]
            checknetlimitdone = checknetlimitdone.split('prio', 1)[0]
        except:
            checknetlimitdone = "Unmetered"

#Description text
    desc = f"""```yaml
ID: {idprefix}{ctx.author.id}
{inforunning}
IP: {infolocalip}
Veth: {checkvethdone}
Cpu: Not Working
Ram: {infocmem}
```"""

#Embed
    embed = discord.Embed(title="Your VpsInfo", description=desc, color=discord.Color.blue())
    embed.add_field(name="Cpu: ", value=f"{infocpu} Vcores")
    embed.add_field(name="Ram: ", value=f"{infomem}")
    embed.add_field(name="Disk: ", value=f"{infodisk} GB")
    embed.add_field(name="Net↿⇂: ", value=f"{checknetlimitdone}")
    embed.set_footer(text = f"Created: {infocreated} UTC")
    await ctx.reply(embed=embed)

############################# ADMIN version - \/

@client.command()
@commands.has_role(adminrole)
async def admininfovps(ctx, id):

    logvarcmd = "infovps"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")

#Command
    infocpu1 = os.popen(f"lxc config show {id} | grep limits.cpu ")
    infocpuout1 = infocpu1.readlines()
    for infocpu in infocpuout1:
        infocpu = infocpu.strip('\n limits.cpu: "')

    infomem1 = os.popen(f"lxc config show {id} | grep limits.memory ")
    infomemout1 = infomem1.readlines()
    for infomem in infomemout1:
        infomem = infomem.strip('\n limits.memory:')

    infodisk1 = os.popen(f"lxc config show {id} | grep size ")
    infodiskout1 = infodisk1.readlines()
    for infodisk in infodiskout1:
        infodisk = infodisk.strip('\n size: GB ')

    inforunning1 = os.popen(f"lxc info --resources {id} | grep Status")
    inforunningout1 = inforunning1.readlines()
    for inforunning in inforunningout1:
        inforunning = inforunning.strip('\n')

    #infoccpu1 = os.popen(f"lxc info --resources {id} | grep -i 'CPU usage (in seconds):'")
    #infoccpuout1 = infoccpu1.readlines()
    #for infoccpu in infoccpuout1:
    #    infoccpu = infoccpu.strip('\n CPU usage (in seconds):')

    #infoccpun = round(int(infoccpu)/(60*1))

    infocreated1 = os.popen(f"lxc info --resources {id} | grep -i 'Created:'")
    infocreatedout1 = infocreated1.readlines()
    for infocreated in infocreatedout1:
        infocreated = infocreated.strip('\n Created: UT')

    if inforunning == "Status: STOPPED": # Stupid fix for UnboundLocalError
        infolocalip = "Offline"
        infocmem = "Offline"
        checkvethdone = "Offline"
        checknetlimitdone = "Offline"
    else:
        infolocalip1 = os.popen(f"lxc info --resources {id} | grep -i '{lxcips}'")
        infolocalipout1 = infolocalip1.readlines()
        for infolocalip in infolocalipout1:
            infolocalip = infolocalip.strip('\n inet: (global)')
        infolocalip = infolocalip.split('/', 1)[0]
        
        infocmem1 = os.popen(f"lxc info --resources {id} | grep -i 'Memory (current):'")
        infocmemout1 = infocmem1.readlines()
        for infocmem in infocmemout1:
            infocmem = infocmem.strip('\n Memory (current):')
            
    #Check for veth from id
        checkveth1 = os.popen(f"lxc config show {id} | grep -i 'host_name'")
        checkvethout1 = checkveth1.readlines()
        for checkveth in checkvethout1:
            checkveth = checkveth.strip('\n')
        checkvethdone = checkveth.split(':', 1)[-1]

    #Check Network limits
        try:   
            checknetlimit1 = os.popen(f"wondershaper {checkvethdone} | grep -i 'prio 1'")
            checknetlimitout1 = checknetlimit1.readlines()
            for checknetlimit in checknetlimitout1:
                checknetlimit = checknetlimit.strip('\n rate')
            checknetlimitdone = checknetlimit.split('rate', 1)[-1]
            checknetlimitdone = checknetlimitdone.split('prio', 1)[0]
        except:
            checknetlimitdone = "Unmetered"
#Description text
    desc = f"""```yaml
ID: {id}
{inforunning}
IP: {infolocalip}
Veth: {checkvethdone}
Cpu: Not Working
Ram: {infocmem}
```"""

#Embed
    embed = discord.Embed(title="Your VpsInfo", description=desc, color=discord.Color.blue())
    embed.add_field(name="Cpu: ", value=f"{infocpu} Vcores")
    embed.add_field(name="Ram: ", value=f"{infomem}")
    embed.add_field(name="Disk: ", value=f"{infodisk} GB")
    embed.add_field(name="Net↿⇂: ", value=f"{checknetlimitdone}")
    embed.set_footer(text = f"Created: {infocreated} UTC")
    await ctx.reply(embed=embed)

########################################################## - Execute Commands In Vps \/ - Deprecated use WebSSH panel

# @client.command()
# async def exec(ctx, *, command: str):

#     logvarcmd = "exec"
#     print(f"{logs}User {ctx.author.id} executed {logvarcmd}")

#Command
    # execcmd1 = os.popen(f"lxc exec {idprefix}{ctx.author.id} -- sh -c '{command}'") # Fix for Vuln Here :))) - to do: fix "" in echo
    # execcmdout1 = re.sub(r'\\.',lambda x:{'\\n':'\n','\\t':'\t','\\b':'\b','\\v':'\v'}.get(x[0],x[0]),f'{execcmd1.readlines()}') # Fix for Weird lines
    # for execcmd in execcmdout1:
    #     execcmd = execcmd.strip('\n')

    # if int(len(f"{execcmd}")) >= 6000:
    #     await ctx.reply("Cannot send, output exceeds 6000 lines")
    # else:
    # #Embed
    #     embed = discord.Embed(title="Executed!", description=f"```{execcmdout1}```", color=discord.Color.blue())
    #     await ctx.reply(embed=embed)

############################# ADMIN version - \/

@client.command()
@commands.has_role(adminrole)
async def adminexec(ctx, id, *, command: str):

    logvarcmd = "adminexec"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")
#Command

    execcmd1 = os.popen(f"lxc exec {id} -- sh -c '{command}'") # Fix for Vuln Here :))) - to do: fix "" in echo
    execcmdout1 = re.sub(r'\\.',lambda x:{'\\n':'\n','\\t':'\t','\\b':'\b','\\v':'\v'}.get(x[0],x[0]),f'{execcmd1.readlines()}') # Fix for Weird lines
    for execcmd in execcmdout1:
        execcmd = execcmd.strip('\n')

#Embed
    embed = discord.Embed(title="Executed!", description=f"```{execcmdout1}```", color=discord.Color.blue())
    await ctx.reply(embed=embed)

########################################################## - Re-Gen password  \/
@client.command()
@commands.check(commandchannelid)
async def regenpass(ctx):

    logvarcmd = "regenpass"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")
#Embed
    embed = discord.Embed(title="Re-Generated", description="Re-Generate VPS password", color=discord.Color.green())

#Fetch users using discord API
    user = await client.fetch_user(ctx.author.id)
#Pass Gen using Bash Script
    passgen1 = os.popen(f"bash /root/lxcbot/passgen.sh")
    passgenout1 = passgen1.readlines()
    for passgen in passgenout1:
        passgen = passgen.strip('\n')
    os.system(f"lxc exec {idprefix}{ctx.author.id} -- sh -c 'echo 'root:{passgen}' | chpasswd'")

    await user.send(f"""```yaml
User: root
Password: {passgen}

- to get ip do -infovps```
Panel: http://panel.vpsbot.ml:8888/""")
    await ctx.reply(embed=embed)

########################################################## - Re-Gen password  \/ - ADMIN
@client.command()
@commands.has_role(adminrole)
async def adminregenpass(ctx, id):

    logvarcmd = "adminregenpass"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")

#Embed
    embed = discord.Embed(title="Re-Generated", description="Re-Generate VPS password", color=discord.Color.green())

#Fetch users using discord API
    user = await client.fetch_user(ctx.author.id)
#Pass Gen using Bash Script
    passgen1 = os.popen(f"bash /root/lxcbot/passgen.sh")
    passgenout1 = passgen1.readlines()
    for passgen in passgenout1:
        passgen = passgen.strip('\n')
    os.system(f"lxc exec {id} -- sh -c 'echo 'root:{passgen}' | chpasswd'")

    await user.send(f"""```yaml
User: root
Password: {passgen}

- to get ip do -infovps```
Panel: http://panel.vpsbot.ml:8888/""")
    await ctx.reply(embed=embed)

########################################################## - Set Cpu to a Container - ADMIN

@client.command()
@commands.has_role(adminrole)
async def setcpu(ctx, id, vcores):

    logvarcmd = "setcpu"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")

#Command
    os.system(f"lxc config set {id} limits.cpu={vcores}")

#Embed
    embed = discord.Embed(title="Changed Successfully!", description="Change Cpu", color=discord.Color.green())
    await ctx.reply(embed=embed)

########################################################## - Set Memory to a Container - ADMIN

@client.command()
@commands.has_role(adminrole)
async def setmem(ctx, id, mib):

    logvarcmd = "setmem"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")

#Command
    os.system(f"lxc config set {id} limits.memory={mib}MiB")

#Embed
    embed = discord.Embed(title="Changed Successfully!", description="Change Memory", color=discord.Color.green())

########################################################## - Set Disk to a Container - ADMIN

@client.command()
@commands.has_role(adminrole)
async def setdisk(ctx, id, disk):

    logvarcmd = "setdisk"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")
#Command
    os.system(f"lxc config device remove {id} root")
    os.system(f"lxc config device override {id} root size={disk}GB")

#Embed
    embed = discord.Embed(title="Changed Successfully!", description="Change Disk", color=discord.Color.green())
    await ctx.reply(embed=embed)

########################################################## - Set Network {Kbps} to a Container - ADMIN

@client.command()
@commands.has_role(adminrole)
async def setnet(ctx, id, up, down):

    logvarcmd = "setnet"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")

    #Check for veth from id
    checkveth1 = os.popen(f"lxc config show {id} | grep -i 'host_name'")
    checkvethout1 = checkveth1.readlines()
    for checkveth in checkvethout1:
        checkveth = checkveth.strip('\n')
    checkvethdone = checkveth.split(':', 1)[-1]
    os.system(f"wondershaper {checkvethdone} {up} {down}")

#Embed
    embed = discord.Embed(title="Changed Successfully!", description="Change Network [Kbps]", color=discord.Color.green())
    await ctx.reply(embed=embed)

########################################################## - List of vpses - ADMIN

@client.command()
@commands.has_role(adminrole)
async def listvps(ctx):

    logvarcmd = "listvps"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")

    list1 = os.popen(f"lxc list -f csv | grep bot")
    listout1 = re.sub(r'\\.',lambda x:{'\\n':'\n','\\t':'\t','\\b':'\b','\\v':'\v'}.get(x[0],x[0]),f'{list1.readlines()}')

#Embed
    embed = discord.Embed(title="Vps List", description=f"```{listout1}```", color=discord.Color.green())
    await ctx.reply(embed=embed)

########################################################## - List of RUNNING vpses - ADMIN

@client.command()
@commands.has_role(adminrole)
async def listrunning(ctx):

    logvarcmd = "listrunning"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")

    listrunning1 = os.popen(f"lxc list -f csv | grep 'RUNNING' | grep bot")
    listrunningout1 = re.sub(r'\\.',lambda x:{'\\n':'\n','\\t':'\t','\\b':'\b','\\v':'\v'}.get(x[0],x[0]),f'{listrunning1.readlines()}')

#Embed
    embed = discord.Embed(title="Vps List Running", description=f"```{listrunningout1}```", color=discord.Color.green())
    await ctx.reply(embed=embed)

########################################################## - List of STOPPED vpses - ADMIN

@client.command()
@commands.has_role(adminrole)
async def liststopped(ctx):

    logvarcmd = "liststopped"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")

    liststopped1 = os.popen(f"lxc list -f csv | grep 'STOPPED' | grep bot")
    liststoppedout1 = re.sub(r'\\.',lambda x:{'\\n':'\n','\\t':'\t','\\b':'\b','\\v':'\v'}.get(x[0],x[0]),f'{liststopped1.readlines()}')

#Embed
    embed = discord.Embed(title="Vps List Stopped", description=f"```{liststoppedout1}```", color=discord.Color.green())
    await ctx.reply(embed=embed)

########################################################## - Perks for Mods - MODS

@client.command()
@commands.has_role(modrole)
@commands.check(commandchannelid)
async def modperks(ctx):

    logvarcmd = "modperks"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")

    os.system(f"lxc config set {idprefix}{ctx.author.id} limits.memory={modperk}MiB")
#Embed
    embed = discord.Embed(title="Perks Applied!", description=f"Applies Mod Perks {modperk}MiB", color=discord.Color.green())
    await ctx.reply(embed=embed)

########################################################## - Perks for Donators - Donators

@client.command()
@commands.has_role(modrole)
@commands.check(commandchannelid)
async def donatorperks(ctx):

    logvarcmd = "donatorperks"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")

    os.system(f"lxc config set {idprefix}{ctx.author.id} limits.memory={donatorperk}MiB")
#Embed
    embed = discord.Embed(title="Perks Applied!", description=f"Applies Donator Perks {modperk}MiB", color=discord.Color.green())
    await ctx.reply(embed=embed)

########################################################## - Giveaway Commands to claim - Giveaway

@client.command()
@commands.check(commandchannelid)
@commands.has_role(giveaway1)
async def claim248(ctx):

    logvarcmd = "claim248"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")

    os.system(f"lxc config set {idprefix}{ctx.author.id} limits.memory={giveaway1}MiB")
#Embed
    embed = discord.Embed(title="Perks Applied!", description=f"Applies Giveaway Perks {giveaway1}MiB", color=discord.Color.green())
    await ctx.reply(embed=embed)

@client.command()
@commands.check(commandchannelid)
@commands.has_role(giveaway2)
async def claim512(ctx):

    logvarcmd = "claim512"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")

    os.system(f"lxc config set {idprefix}{ctx.author.id} limits.memory={giveaway2}MiB")
#Embed
    embed = discord.Embed(title="Perks Applied!", description=f"Applies Giveaway Perks {giveaway2}MiB", color=discord.Color.green())
    await ctx.reply(embed=embed)

@client.command()
@commands.check(commandchannelid)
@commands.has_role(giveaway3)
async def claim1024(ctx):

    logvarcmd = "claim1024"
    print(f"{logs}User {ctx.author.id} executed {logvarcmd}")

    os.system(f"lxc config set {idprefix}{ctx.author.id} limits.memory={giveaway3}MiB")
#Embed
    embed = discord.Embed(title="Perks Applied!", description=f"Applies Giveaway Perks {giveaway3}MiB", color=discord.Color.green())
    await ctx.reply(embed=embed)

########################################################## - Show Current Logs - ADMIN

@client.command()
@commands.has_role(adminrole)
async def log(ctx):

#Embed
    f = open("logs.txt", "r")
    embed = discord.Embed(title="Logs", description=f"```{f.read()}```", color=discord.Color.blue())

    await ctx.send(embed=embed) 
    f.close()

client.run("YOUR TOKEN")

if logstofile == "true":
    sys.stdout.close()
