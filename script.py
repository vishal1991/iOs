import paramiko
import os
import platform
import shutil

ip = raw_input("Enter IP address:")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, username= 'root', password= 'alpine')
stdin, stdout, stderr = ssh.exec_command("ls /var/mobile/Containers/Bundle/Application")
x =  stdout.readlines()
for items in x:
	items.encode("utf-8")
	print items 

ssh.close()

path = raw_input("Copy UUID and paste here:")

localpath = os.getcwd()
remotepath = "/var/mobile/Containers/Bundle/Application/" + path

#p = subprocess.Popen('scp', localpath, remotepath)

#if platform.system() == 'Linux':

os.system("scp -r"+" "+ ip+":"+remotepath+" "+localpath)

delete = raw_input("Delete Directory [y/n]:")

delete = delete.lower()

if delete[0] == "y" :
	d = localpath + '/' + path
	shutil.rmtree(d)
	print "[+]OK"

'''
sftp = ssh.open_sftp()
sftp.get(str(remotepath), str(localpath))
sftp.close()
ssh.close()
print "[OK]"
'''
