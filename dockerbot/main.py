import os,sys,discord,psutil,time
from configparser import ConfigParser
from typing import Literal
from discord import app_commands
from discord.ext import commands
config=ConfigParser()
config.read('config.cfg')
botprefix='/'
intents=discord.Intents.all()
client=commands.Bot(command_prefix=botprefix,intents=intents)
client.remove_command('help')
version='Beta 1.1'
logs='[Logs] '
devicename=config['Config']['devicename']
adminrole=config['Config']['adminrole']
userrole=config['Config']['userrole']
usercpu=config['Config']['usercpu']
usercores=config['Config']['usercores']
userram=config['Config']['userram']
userswap=config['Config']['userswap']
userdisk=config['Config']['userdisk']
onstartupnet=config['Config']['onstartupnet']
idprefix=config['Config']['idprefix']
vpslimit=int(config['Config']['vpslimit'])
cmdchid=config['Config']['cmdchid']
@client.event
async def on_ready():await client.change_presence(activity=discord.Game(name=f"{botprefix}help"));synced=await client.tree.sync();print(f"{len(synced)} Commands have been synced")
async def commandchannelid(ctx):return ctx.channel.id==cmdchid
@client.tree.command(name='help',description='Tells you all commands')
@commands.has_role(userrole)
@commands.check(commandchannelid)
async def help(interaction):logvarcmd='help';print(f"{logs}User {interaction.user.id} executed {logvarcmd}");embed=discord.Embed(title='Help',description=f"Prefix ({botprefix})",color=discord.Color.blue());embed.add_field(name='createvps (ubuntu/debian/alpine)',value=f"Allows you to create 1 vps");embed.add_field(name='startvps',value=f"Allows you to manage your vps");embed.add_field(name='stopvps',value=f"Allows you to manage your vps");embed.add_field(name='restartvps',value=f"Allows you to manage your vps");embed.add_field(name='deletevps',value=f"Allows you to delete your vps");embed.add_field(name='regenssh',value=f"Re-Generate the ssh session");embed.add_field(name='infovps',value=f"Allows you to see the current Status of your vps");embed.add_field(name='nodeinfo',value=f"Allows you to see the current usage of the node");embed.add_field(name='help',value=f"This Command");embed.set_footer(text=f"Version: {version}");await interaction.response.send_message(embed=embed)
@client.tree.command(name='helpcn',description='Tells you all commands')
@commands.has_role(userrole)
@commands.check(commandchannelid)
async def helpcn(interaction):logvarcmd='helpcn';print(f"{logs}User {interaction.user.id} executed {logvarcmd}");embed=discord.Embed(title='Help',description=f"Prefix ({botprefix})",color=discord.Color.blue());embed.add_field(name='createvps (ubuntu/debian/alpine)',value=f"允许你创建1个vps");embed.add_field(name='startvps',value=f"允许你启动你的vps");embed.add_field(name='stopvps',value=f"允许你停止你的vps");embed.add_field(name='restartvps',value=f"允许你重新启动你的vps");embed.add_field(name='deletevps',value=f"允许你删除你的vps");embed.add_field(name='infovps',value=f"允许你看到你的vps的当前状态。");embed.add_field(name='nodeinfo',value=f"允许你查看节点的当前使用情况");embed.add_field(name='helpcn',value=f"该命令");embed.set_footer(text=f"Version: {version}");await interaction.response.send_message(embed=embed)
@client.tree.command(name='helpru',description='Tells you all commands')
@commands.has_role(userrole)
@commands.check(commandchannelid)
async def helpru(interaction):logvarcmd='helpru';print(f"{logs}User {interaction.user.id} executed {logvarcmd}");embed=discord.Embed(title='Help',description=f"Префикс ({botprefix})",color=discord.Color.blue());embed.add_field(name='createvps (ubuntu/debian/archlinux/alpine)',value=f"Позволяет вам создать 1 VPS");embed.add_field(name='startvps',value=f"Позволяет вам запустить ваш");embed.add_field(name='stopvps',value=f"Позволяет вам остановить ваш VPS");embed.add_field(name='restartvps',value=f"Позволяет вам перезагрузить ваш VPS");embed.add_field(name='deletevps',value=f"Позволяет вам удалить ваш VPS");embed.add_field(name='infovps',value=f"Позволяет вам посмотреть статус вашего VPS");embed.add_field(name='nodeinfo',value=f"Позволяет посмотреть вам использование ресурсов ноды");embed.add_field(name='helpru',value=f"Эта команда");embed.set_footer(text=f"Version: {version}");await interaction.response.send_message(embed=embed)
@client.tree.command(name='helpes',description='Tells you all commands')
@commands.has_role(userrole)
@commands.check(commandchannelid)
async def helpes(interaction):logvarcmd='helpes';print(f"{logs}User {interaction.user.id} executed {logvarcmd}");embed=discord.Embed(title='Help',description=f"Prefijo ({botprefix})",color=discord.Color.blue());embed.add_field(name='createvps (ubuntu/debian/archlinux/alpine)',value=f"Te permite crear 1 VPS");embed.add_field(name='startvps',value=f"Te permite iniciar tu VPS");embed.add_field(name='stopvps',value=f"Te permite parar tu VPS");embed.add_field(name='restartvps',value=f"Te permite reiniciar tu VPS");embed.add_field(name='deletevps',value=f"Te permite eliminar tu VPS");embed.add_field(name='infovps',value=f"Te permite el estado actual de tu VPS");embed.add_field(name='nodeinfo',value=f"Te permite ver el uso actual del nodo");embed.add_field(name='helpes',value=f"Este comando");embed.set_footer(text=f"Version: {version}");await interaction.response.send_message(embed=embed)
@client.tree.command(name='helpfr',description='Tells you all commands')
@commands.has_role(userrole)
@commands.check(commandchannelid)
async def helpfr(interaction):logvarcmd='helpfr';print(f"{logs}User {interaction.user.id} executed {logvarcmd}");embed=discord.Embed(title='Help',description=f"Préfixe ({botprefix})",color=discord.Color.blue());embed.add_field(name='createvps (ubuntu/debian/archlinux/alpine)',value=f"Vous permet de créer 1 VPS");embed.add_field(name='startvps',value=f"Vous permet de démarrer votre VPS");embed.add_field(name='stopvps',value=f"Vous permet d'arrêter votre VPS");embed.add_field(name='restartvps',value=f"Permet de redémarrer votre VPS");embed.add_field(name='deletevps',value=f"Vous permet de supprimer votre VPS");embed.add_field(name='infovps',value=f"Permet de voir le statut actuel de votre VPS");embed.add_field(name='nodeinfo',value=f"Permet de voir l'état actuel du nœud");embed.add_field(name='helpfr',value=f"Cette commande");embed.set_footer(text=f"Version: {version}");await interaction.response.send_message(embed=embed)
@client.tree.command(name='createvps',description='Tells you all commands')
@commands.has_role(userrole)
@commands.check(commandchannelid)
async def createvps(interaction,image):
	logvarcmd='createvps';desc=f"""```yaml
ID: {idprefix}{interaction.user.id}
OS: {image}
----------------------
Cpu: {usercpu} Vcore(s)%
Core(s): {usercores}
Ram: {userram} MiB
Swap: {userswap} MiB
Disk: {userdisk} GiB
Net: {onstartupnet} Kibps
----------------------```""";vpsnum1=os.popen(f"docker ps -a -q | wc -l");vpsnumout1=vpsnum1.readlines()
	for vpsnumout in vpsnumout1:vpsnumout=vpsnumout.strip('\n')
	embed=discord.Embed(title='Creation Successfull!',description=desc,color=discord.Color.green());user=await client.fetch_user(interaction.user.id);alpine='alpine_custom';ubuntu='ubuntu22_custom';debian='debian11_custom'
	if image=='alpine'and int(vpsnumout)<=vpslimit:
		print(f"{logs}User {interaction.user.id} executed {logvarcmd}");await interaction.response.send_message('Creating...');os.system(f'docker run -it -d --cpus="{usercpu}" --cpuset-cpus="{usercores}" --memory="{userram}m" --memory-swap="{userswap}m" -w="/root" --name="{idprefix}{interaction.user.id}" --hostname="{idprefix}{interaction.user.id}" {alpine}');os.system(f'docker exec {idprefix}{interaction.user.id} sh -c "tmate -S /tmp/tmate.sock new-session -d"');os.system(f'docker exec {idprefix}{interaction.user.id} sh -c "tmate -S /tmp/tmate.sock wait tmate-ready"');sshsend1=os.popen(f'docker exec {idprefix}{interaction.user.id} sh -c "sh /root/tmate.sh"');sshsendout1=sshsend1.readlines()
		for sshsend in sshsendout1:sshsend=sshsend.strip('\n')
		await user.send(f"{sshsend}")
		try:
			checkveth1=os.popen(f"bash vethiddocker.sh | grep -i '{idprefix}{interaction.user.id}'");checkvethout1=checkveth1.readlines()
			for checkveth in checkvethout1:checkveth=checkveth.strip('\n');checkvethdone=checkveth.split(':',1)[-1];os.system(f"wondershaper {checkvethdone} {onstartupnet}");await interaction.response.send_message(embed=embed)
		except:await interaction.response.send_message(embed=embed)
	elif image=='ubuntu'and int(vpsnumout)<=vpslimit:
		print(f"{logs}User {interaction.user.id} executed {logvarcmd}");await interaction.response.send_message('Creating...');os.system(f'docker run -it -d --cpus="{usercpu}" --cpuset-cpus="{usercores}" --memory="{userram}m" --memory-swap="{userswap}m" -w="/root" --name="{idprefix}{interaction.user.id}" --hostname="{idprefix}{interaction.user.id}" {ubuntu}');os.system(f'docker exec {idprefix}{interaction.user.id} sh -c "tmate -S /tmp/tmate.sock new-session -d"');os.system(f'docker exec {idprefix}{interaction.user.id} sh -c "tmate -S /tmp/tmate.sock wait tmate-ready"');sshsend1=os.popen(f'docker exec {idprefix}{interaction.user.id} sh -c "bash /root/tmate.sh"');sshsendout1=sshsend1.readlines()
		for sshsend in sshsendout1:sshsend=sshsend.strip('\n')
		await user.send(f"{sshsend}")
		try:
			checkveth1=os.popen(f"bash vethiddocker.sh | grep -i '{idprefix}{interaction.user.id}'");checkvethout1=checkveth1.readlines()
			for checkveth in checkvethout1:checkveth=checkveth.strip('\n');checkvethdone=checkveth.split(':',1)[-1];os.system(f"wondershaper {checkvethdone} {onstartupnet}");await interaction.response.send_message(embed=embed)
		except:await interaction.response.send_message(embed=embed)
	elif image=='debian'and int(vpsnumout)<=vpslimit:
		print(f"{logs}User {interaction.user.id} executed {logvarcmd}");await interaction.response.send_message('Creating...');os.system(f'docker run -it -d --cpus="{usercpu}" --cpuset-cpus="{usercores}" --memory="{userram}m" --memory-swap="{userswap}m" -w="/root" --name="{idprefix}{interaction.user.id}" --hostname="{idprefix}{interaction.user.id}" {debian}');os.system(f'docker exec {idprefix}{interaction.user.id} sh -c "tmate -S /tmp/tmate.sock new-session -d"');os.system(f'docker exec {idprefix}{interaction.user.id} sh -c "tmate -S /tmp/tmate.sock wait tmate-ready"');sshsend1=os.popen(f'docker exec {idprefix}{interaction.user.id} sh -c "bash /root/tmate.sh"');sshsendout1=sshsend1.readlines()
		for sshsend in sshsendout1:sshsend=sshsend.strip('\n')
		await user.send(f"{sshsend}")
		try:
			checkveth1=os.popen(f"bash vethiddocker.sh | grep -i '{idprefix}{interaction.user.id}'");checkvethout1=checkveth1.readlines()
			for checkveth in checkvethout1:checkveth=checkveth.strip('\n');checkvethdone=checkveth.split(':',1)[-1];os.system(f"wondershaper {checkvethdone} {onstartupnet}");await interaction.response.send_message(embed=embed)
		except:await interaction.response.send_message(embed=embed)
@client.tree.command(name='admincreatevps',description='Allows admins to create vpses')
@commands.has_role(adminrole)
async def admicreatevps(interaction,id,image,cpu,cores,ram,swap,net):
	logvarcmd='admincreatevps';desc=f"""```yaml
ID: {id}
OS: {image}
----------------------
Cpu: {cpu} Vcore(%)
Core(s): {cores}
Ram: {ram} MiB
Swap: {swap} MiB
Disk: - GiB
Net: {net} Kibps
----------------------```""";embed=discord.Embed(title='Creation Successfull!',description=desc,color=discord.Color.green());alpine='alpine:3.16.2';ubuntu='ubuntu22_custom';debian='debian:11'
	if image=='alpine':
		print(f"{logs}User {interaction.user.id} executed {logvarcmd}");await interaction.response.send_message('Creating...');os.system(f'docker run -it -d --cpus="{cpu}" --cpuset-cpus="{cores}" --memory="{ram}m" --memory-swap="{swap}m" -w="/root" --name="{id}" --hostname="{id}" {alpine}');passgen1=os.popen(f"bash passgen.sh");passgenout1=passgen1.readlines()
		for passgen in passgenout1:passgen=passgen.strip('\n')
		os.system(f'docker exec {id} sh -c "echo "root:{passgen}" | chpasswd"')
		try:
			checkveth1=os.popen(f"bash vethiddocker.sh | grep -i '{id}'");checkvethout1=checkveth1.readlines()
			for checkveth in checkvethout1:checkveth=checkveth.strip('\n');checkvethdone=checkveth.split(':',1)[-1];os.system(f"wondershaper {checkvethdone} {onstartupnet}");await interaction.response.send_message(embed=embed)
		except:await interaction.response.send_message(embed=embed)
	elif image=='ubuntu':
		print(f"{logs}User {interaction.user.id} executed {logvarcmd}");await interaction.response.send_message('Creating...');os.system(f'docker run -it -d --cpus="{cpu}" --cpuset-cpus="{cores}" --memory="{ram}m" --memory-swap="{swap}m" -w="/root" --name="{id}" --hostname="{id}" {ubuntu}');passgen1=os.popen(f"bash passgen.sh");passgenout1=passgen1.readlines()
		for passgen in passgenout1:passgen=passgen.strip('\n')
		os.system(f'docker exec {id} sh -c "echo "root:{passgen}" | chpasswd"')
		try:
			checkveth1=os.popen(f"bash vethiddocker.sh | grep -i '{id}'");checkvethout1=checkveth1.readlines()
			for checkveth in checkvethout1:checkveth=checkveth.strip('\n');checkvethdone=checkveth.split(':',1)[-1];os.system(f"wondershaper {checkvethdone} {onstartupnet}");await interaction.response.send_message(embed=embed)
		except:await interaction.response.send_message(embed=embed)
	elif image=='debian':
		print(f"{logs}User {interaction.user.id} executed {logvarcmd}");await interaction.response.send_message('Creating...');os.system(f'docker run -it -d --cpus="{cpu}" --cpuset-cpus="{cores}" --memory="{ram}m" --memory-swap="{swap}m" -w="/root" --name="{id}" --hostname="{id}" {debian}');passgen1=os.popen(f"bash passgen.sh");passgenout1=passgen1.readlines()
		for passgen in passgenout1:passgen=passgen.strip('\n')
		os.system(f'docker exec {id} sh -c "echo "root:{passgen}" | chpasswd"')
		try:
			checkveth1=os.popen(f"bash vethiddocker.sh | grep -i '{id}'");checkvethout1=checkveth1.readlines()
			for checkveth in checkvethout1:checkveth=checkveth.strip('\n');checkvethdone=checkveth.split(':',1)[-1];os.system(f"wondershaper {checkvethdone} {onstartupnet}");await interaction.response.send_message(embed=embed)
		except:await interaction.response.send_message(embed=embed)
@client.tree.command(name='regenssh',description='Regenerates ssh if it dosent work')
@commands.has_role(userrole)
async def regenssh(interaction):
	logvarcmd='regenssh';print(f"{logs}User {interaction.user.id} executed {logvarcmd}");user=await client.fetch_user(interaction.user.id);embed=discord.Embed(title='SSH Regenerated Successfully!',description='Regen SSH',color=discord.Color.green());os.system(f'docker exec {idprefix}{interaction.user.id} sh -c "tmate -S /tmp/tmate.sock new-session -d"');os.system(f'docker exec {idprefix}{interaction.user.id} sh -c "tmate -S /tmp/tmate.sock wait tmate-ready"');sshsend1=os.popen(f'docker exec {idprefix}{interaction.user.id} sh -c "sh /root/tmate.sh"');sshsendout1=sshsend1.readlines()
	for sshsend in sshsendout1:sshsend=sshsend.strip('\n')
	await user.send(f"{sshsend}");await interaction.response.send_message(embed=embed)
@client.tree.command(name='adminregenssh',description='Allows admins to regenerate vpses ssh')
@commands.has_role(adminrole)
async def adminregenssh(interaction,id):
	logvarcmd='adminregenssh';print(f"{logs}User {interaction.user.id} executed {logvarcmd}");user=await client.fetch_user(interaction.user.id);embed=discord.Embed(title='SSH Regenerated Successfully!',description='Regen SSH',color=discord.Color.green());os.system(f'docker exec {id} sh -c "tmate -S /tmp/tmate.sock new-session -d"');os.system(f'docker exec {id} sh -c "tmate -S /tmp/tmate.sock wait tmate-ready"');sshsend1=os.popen(f'docker exec {id} sh -c "sh /root/tmate.sh"');sshsendout1=sshsend1.readlines()
	for sshsend in sshsendout1:sshsend=sshsend.strip('\n')
	await user.send(f"{sshsend}");await interaction.response.send_message(embed=embed)
@client.tree.command(name='deletevps',description='Allows you to delete your vps')
@commands.has_role(userrole)
async def deletevps(interaction):logvarcmd='deletevps';print(f"{logs}User {interaction.user.id} executed {logvarcmd}");embed=discord.Embed(title='Delete Successfull!',description='Delete Vps',color=discord.Color.green());os.system(f"docker rm {idprefix}{interaction.user.id} -f");await interaction.response.send_message(embed=embed)
@client.tree.command(name='admindeletevps',description='Allows admins to delete vpses')
@commands.has_role(adminrole)
async def admindeletevps(interaction,id):logvarcmd='admindeletevps';print(f"{logs}User {interaction.user.id} executed {logvarcmd}");embed=discord.Embed(title='Delete Successfull!',description='Delete Vps',color=discord.Color.green());os.system(f"docker rm {id} -f");await interaction.response.send_message(embed=embed)
@client.tree.command(name='startvps',description='Allows you to start your vps')
@commands.has_role(userrole)
async def startvps(interaction):
	logvarcmd='startvps';print(f"{logs}User {interaction.user.id} executed {logvarcmd}");embed=discord.Embed(title='Start Successfull!',description='Start Vps',color=discord.Color.green());os.system(f"docker start {idprefix}{interaction.user.id}");checkveth1=os.popen(f"bash vethiddocker.sh | grep -i '{idprefix}{interaction.user.id}'");checkvethout1=checkveth1.readlines()
	for checkveth in checkvethout1:checkveth=checkveth.strip('\n');checkvethdone=checkveth.split(':',1)[-1]
	os.system(f"wondershaper {checkvethdone} {onstartupnet}");await interaction.response.send_message(embed=embed)
@client.tree.command(name='adminstartvps',description='Allows admins to start vpses')
@commands.has_role(adminrole)
async def adminstartvps(interaction,id):
	logvarcmd='adminstartvps';print(f"{logs}User {interaction.user.id} executed {logvarcmd}");embed=discord.Embed(title='Start Successfull!',description='Start Vps',color=discord.Color.green());os.system(f"docker start {id}");checkveth1=os.popen(f"bash vethiddocker.sh | grep -i '{id}'");checkvethout1=checkveth1.readlines()
	for checkveth in checkvethout1:checkveth=checkveth.strip('\n');checkvethdone=checkveth.split(':',1)[-1]
	os.system(f"wondershaper {checkvethdone} {onstartupnet}");await interaction.response.send_message(embed=embed)
@client.tree.command(name='stop',description='Allows you to stop your vps')
@commands.has_role(userrole)
async def stopvps(interaction):logvarcmd='stopvps';print(f"{logs}User {interaction.user.id} executed {logvarcmd}");embed=discord.Embed(title='Stop Successfull!',description='Stop Vps',color=discord.Color.green());os.system(f"docker kill {idprefix}{interaction.user.id}");await interaction.response.send_message(embed=embed)
@client.tree.command(name='adminstopvps',description='Allows admins to stop vpses')
@commands.has_role(adminrole)
async def adminstopvps(interaction,id):logvarcmd='adminstopvps';print(f"{logs}User {interaction.user.id} executed {logvarcmd}");embed=discord.Embed(title='Stop Successfull!',description='Stop Vps',color=discord.Color.green());os.system(f"docker kill {id}");await interaction.response.send_message(embed=embed)
@client.tree.command(name='restartvps',description='Allows you to restart your vps')
@commands.has_role(userrole)
async def restartvps(interaction):
	logvarcmd='restartvps';print(f"{logs}User {interaction.user.id} executed {logvarcmd}");embed=discord.Embed(title='Restart Successfull!',description='Restart Vps',color=discord.Color.green());os.system(f"docker kill {idprefix}{interaction.user.id}");os.system(f"docker start {idprefix}{interaction.user.id}");checkveth1=os.popen(f"bash vethiddocker.sh | grep -i '{idprefix}{interaction.user.id}'");checkvethout1=checkveth1.readlines()
	for checkveth in checkvethout1:checkveth=checkveth.strip('\n');checkvethdone=checkveth.split(':',1)[-1]
	os.system(f"wondershaper {checkvethdone} {onstartupnet}");await interaction.response.send_message(embed=embed)
@client.tree.command(name='adminrestartvps',description='Allows admins to restart vpses')
@commands.has_role(adminrole)
async def adminrestartvps(interaction,id):
	logvarcmd='adminrestartvps';print(f"{logs}User {interaction.user.id} executed {logvarcmd}");embed=discord.Embed(title='Restart Successfull!',description='Restart Vps',color=discord.Color.green());os.system(f"docker kill {id}");os.system(f"docker start {id}");checkveth1=os.popen(f"bash vethiddocker.sh | grep -i '{id}'");checkvethout1=checkveth1.readlines()
	for checkveth in checkvethout1:checkveth=checkveth.strip('\n');checkvethdone=checkveth.split(':',1)[-1];os.system(f"wondershaper {checkvethdone} {onstartupnet}")
	await interaction.response.send_message(embed=embed)
@client.tree.command(name='infovps',description='Allows you to see your vps info')
@commands.has_role(userrole)
async def infovps(interaction):
	logvarcmd='infovps';print(f"{logs}User {interaction.user.id} executed {logvarcmd}");await interaction.response.defer()
	try:
		cpu1=os.popen(f'docker stats --all --format "{{{{.CPUPerc}}}}" --no-stream {idprefix}{interaction.user.id}');cpuout1=cpu1.readlines()
		for cpu in cpuout1:cpu=cpu.strip('\n')
	except:cpu='Unknown'
	try:
		ram1=os.popen(f'docker stats --all --format "{{{{.MemUsage}}}}" --no-stream {idprefix}{interaction.user.id}');ramout1=ram1.readlines()
		for ram in ramout1:ram=ram.strip('\n')
	except:ram='Unknown'
	try:
		net1=os.popen(f'docker stats --all --format "{{{{.MemUsage}}}}" --no-stream {idprefix}{interaction.user.id}');netout1=net1.readlines()
		for net in netout1:net=net.strip('\n')
	except:net='Unknown'
	try:
		checkveth1=os.popen(f"bash vethiddocker.sh | grep -i '{idprefix}{interaction.user.id}'");checkvethout1=checkveth1.readlines()
		for checkveth in checkvethout1:checkveth=checkveth.strip('\n');checkvethdone=checkveth.split(':',1)[-1]
	except:checkvethdone='Unknown'
	try:
		ip1=os.popen(f'docker inspect -f "{{{{range .NetworkSettings.Networks}}}}{{{{.IPAddress}}}}{{{{end}}}}" {idprefix}{interaction.user.id}');ipout1=ip1.readlines()
		for ip in ipout1:ip=ip.strip('\n')
	except:ip='Unknown'
	try:
		cpulimit1=os.popen(f'docker container inspect {idprefix}{interaction.user.id}|grep -i "NanoCpu"');cpulimitout1=cpulimit1.readlines()
		for cpulimit in cpulimitout1:cpulimit=cpulimit.strip('\n , "NanoCpus":');cpulimit=int(cpulimit)/1000000000
	except:cpulimit='Unknown'
	try:
		ramlimit1=os.popen(f"docker container inspect {idprefix}{interaction.user.id}|grep -i Memory | head -n 1");ramlimitout1=ramlimit1.readlines()
		for ramlimit in ramlimitout1:ramlimit=ramlimit.strip('\n , "Memory":');ramlimit=round(int(ramlimit)/1024/1024)
	except:ramlimit='Unknown'
	try:
		swaplimit1=os.popen(f"docker container inspect {idprefix}{interaction.user.id}|grep -i MemorySwap | head -n 1");swaplimitout1=swaplimit1.readlines()
		for swaplimit in swaplimitout1:swaplimit=swaplimit.strip('\n , "MemorySwap":');swaplimit=round(int(swaplimit)/1024/1024)
	except:swaplimit='Unknown'
	disklimit='Unmetered';netlimit=onstartupnet;desc=f"""```yaml
ID: {idprefix}{interaction.user.id}
IP: {ip}
Cpu: {cpu}| Core({usercores})
Ram: {ram}
```""";embed=discord.Embed(title='Your VpsInfo',description=desc,color=discord.Color.blue());embed.add_field(name='Cpu: ',value=f"{cpulimit} Vcore(%)");embed.add_field(name='Ram: ',value=f"{ramlimit} MiB");embed.add_field(name='Swap: ',value=f"{swaplimit} MiB");embed.add_field(name='Disk: ',value=f"{disklimit}");embed.add_field(name='Net⇂↿: ',value=f"{netlimit}");await interaction.followup.send(embed=embed)
@client.tree.command(name='admininfovps',description='Allows admins to see other vpses info')
@commands.has_role(userrole)
async def admininfovps(interaction,id):
	logvarcmd='admininfovps';print(f"{logs}User {interaction.user.id} executed {logvarcmd}");await interaction.response.defer()
	try:
		cpu1=os.popen(f'docker stats --all --format "{{{{.CPUPerc}}}}" --no-stream {id}');cpuout1=cpu1.readlines()
		for cpu in cpuout1:cpu=cpu.strip('\n')
	except:cpu='Unknown'
	try:
		ram1=os.popen(f'docker stats --all --format "{{{{.MemUsage}}}}" --no-stream {id}');ramout1=ram1.readlines()
		for ram in ramout1:ram=ram.strip('\n')
	except:ram='Unknown'
	try:
		net1=os.popen(f'docker stats --all --format "{{{{.MemUsage}}}}" --no-stream {id}');netout1=net1.readlines()
		for net in netout1:net=net.strip('\n')
	except:net='Unknown'
	try:
		checkveth1=os.popen(f"bash vethiddocker.sh | grep -i '{id}'");checkvethout1=checkveth1.readlines()
		for checkveth in checkvethout1:checkveth=checkveth.strip('\n');checkvethdone=checkveth.split(':',1)[-1]
	except:checkvethdone='Unknown'
	try:
		ip1=os.popen(f'docker inspect -f "{{{{range .NetworkSettings.Networks}}}}{{{{.IPAddress}}}}{{{{end}}}}" {id}');ipout1=ip1.readlines()
		for ip in ipout1:ip=ip.strip('\n')
	except:ip='Unknown'
	try:
		cpulimit1=os.popen(f'docker container inspect {id}|grep -i "NanoCpu"');cpulimitout1=cpulimit1.readlines()
		for cpulimit in cpulimitout1:cpulimit=cpulimit.strip('\n , "NanoCpus":');cpulimit=int(cpulimit)/1000000000
	except:cpulimit='Unknown'
	try:
		ramlimit1=os.popen(f"docker container inspect {id}|grep -i Memory | head -n 1");ramlimitout1=ramlimit1.readlines()
		for ramlimit in ramlimitout1:ramlimit=ramlimit.strip('\n , "Memory":');ramlimit=round(int(ramlimit)/1024/1024)
	except:ramlimit='Unknown'
	try:
		swaplimit1=os.popen(f"docker container inspect {id}|grep -i MemorySwap | head -n 1");swaplimitout1=swaplimit1.readlines()
		for swaplimit in swaplimitout1:swaplimit=swaplimit.strip('\n , "MemorySwap":');swaplimit=round(int(swaplimit)/1024/1024)
	except:swaplimit='Unknown'
	disklimit='Unmetered';netlimit=onstartupnet;desc=f"""```yaml
ID: {id}
IP: {ip}
Cpu: {cpu}| Core({usercores})
Ram: {ram}
```""";embed=discord.Embed(title='Your VpsInfo',description=desc,color=discord.Color.blue());embed.add_field(name='Cpu: ',value=f"{cpulimit} Vcore(%)");embed.add_field(name='Ram: ',value=f"{ramlimit} MiB");embed.add_field(name='Swap: ',value=f"{swaplimit} MiB");embed.add_field(name='Disk: ',value=f"{disklimit}");embed.add_field(name='Net⇂↿: ',value=f"{netlimit}");await interaction.followup.send(embed=embed)
@client.tree.command(name='nodeinfo',description='Allows you to see node usage')
@commands.has_role(userrole)
async def nodeinfo(interaction):
	logvarcmd='nodeinfo';print(f"{logs}User {interaction.user.id} executed {logvarcmd}");cpu=psutil.cpu_percent();ram=psutil.virtual_memory().percent;swap=psutil.swap_memory().percent;total=round(ram+swap)/2
	try:
		temp1=os.popen('vcgencmd measure_temp');tempout1=temp1.readlines()
		for tempout in tempout1:tempout=tempout.strip("\n temp= ' C")
	except:tempout='-'
	try:
		fan1=os.popen('sensors | grep Processor');fanout1=fan1.readlines()
		for fanout in fanout1:fanout=fanout.strip('\n Processor Fan:')
	except:fanout='-'
	def uptimeseconds():return time.time()-psutil.boot_time()
	uptime=round(uptimeseconds()/3600);vpsnum1=os.popen(f"docker ps -a -q | wc -l");vpsnumout1=vpsnum1.readlines()
	for vpsnumout in vpsnumout1:vpsnumout=vpsnumout.strip('\n')
	vpsactive1=os.popen(f"docker ps -q | wc -l");vpsactiveout1=vpsactive1.readlines()
	for vpsactiveout in vpsactiveout1:vpsactiveout=vpsactiveout.strip('\n')
	vpsinactive1=os.popen(f'docker ps -a -q -f "status=exited" | wc -l');vpsinactiveout1=vpsinactive1.readlines()
	for vpsinactiveout in vpsinactiveout1:vpsinactiveout=vpsinactiveout.strip('\n')
	getos1=os.popen("screenfetch -nN | grep -i 'OS'");getosout1=getos1.readlines()
	for getosout in getosout1:getosout=getosout.strip('\n')
	getcpu1=os.popen("screenfetch -nN | grep -i 'CPU'");getcpuout1=getcpu1.readlines()
	for getcpuout in getcpuout1:getcpuout=getcpuout.strip('\n')
	getram1=os.popen("screenfetch -nN | grep -i 'RAM'");getramout1=getram1.readlines()
	for getramout in getramout1:getramout=getramout.strip('\n')
	getuptime1=os.popen("screenfetch -nN | grep -i 'Uptime'");getuptimeout1=getuptime1.readlines()
	for getuptimeout in getuptimeout1:getuptimeout=getuptimeout.strip('\n')
	desc=f"""```yaml
{getosout}
{getcpuout}
{getramout}
{getuptimeout}
```""";embed=discord.Embed(title=f"Node Info - {devicename}",description=desc,color=discord.Color.purple());embed.add_field(name='**CPU**',value=f"{cpu}%");embed.add_field(name='**RAM**',value=f"{total}%");embed.add_field(name='**TEMP**',value=f"-");embed.add_field(name='**FAN**',value=f"-");embed.add_field(name='**UPTIME**',value=f"{uptime} Hours");embed.add_field(name='**INSTANCES**',value=f"{vpsnumout}");embed.add_field(name='**ACTIVE**',value=f"{vpsactiveout}");embed.add_field(name='**INACTIVE**',value=f"{vpsinactiveout}");embed.add_field(name='**LIMIT**',value=f"{vpslimit}");await interaction.response.send_message(embed=embed)
client.run(config['Config']['token'])
