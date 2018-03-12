#Minor changes in formating in requirements.txt 

import subprocess

all_installed = True
f = open('requirements.txt','r')
message = f.read()
message = message.split('\n')
failed = []
for i in message:
	print(i)
	command = 'pip install ' + i
	if(subprocess.call(command,shell=True) == 1):
		all_installed = False
		failed.append(i)

#Clears all dependencies installation instructions		
subprocess.call('clear',shell=True)

if all_installed:
	print("All dependencies installed successfully")
else:
	for i in failed:
		print(i + " failed")
		