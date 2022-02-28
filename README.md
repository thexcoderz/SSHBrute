<p align="center">
<img title="SSHBrute" src="https://raw.githubusercontent.com/thexcoderz/SSHBrute/main/img-2.png" alt="SSHBrute"/>
</p>

# SSHBrute

A fast and lightweight SSH (secured shell) brute force tool made using Python. Uses threading with custom time delay to increase the speed to its peak. Maximum speed 100 attempts in 12 seconds.
***

## Installation
First of all clone or download the SSHBrute Project in your system. For Linux users just type the following command in the shell.
```bash
$ git clone https://github.com/thexcoderz/SSHBrute.git
```
You will need python3 installed in your system to use this tool. If you are using Linux then run the setup.sh script. It will automatically install and setup all the requirements.
```bash
$ bash setup.sh
```
For another operating systems just refer to official Python Download site for installation. After installing python, Move to the SSHBrute's project directory and type the following command to install the required python modules.
```bash
$ pip3 install -r requirements.txt
```
Now We are ready to use the tool !
***
## Usage
For performing the attack you will need a wordlist containing the passwords. The tool comes with a default wordlist containing 500 common password. You can use your own wordlist also.

To start attack on a ssh service :
```
$ python3 sshbrute.py --hostname <Server> --port <Port> --user <User>
# OR
$ python3 sshbrute.py -ip <Server> -p <Port> -u <User>
```
You can specify your own wordlist with --passlist OR -pl argument. Example:
```
$ python3 sshbrute.py --hostname <Server> --port <Port> --user <User> --passlist <Path_To_WordList>
# OR
$ python3 sshbrute.py -ip <Server> -p <Port> -u <User> -pl <Path_To_WordList>
```
### Time Delay
The default delay between attempts is 0.5s. You can change the time delay between the attempts via the --delay OR -d argument. Warning - Don't set the delay to 0. Example:
```
$ python3 sshbrute.py --hostname <Server> --port <Port> --user <User> --delay 0.3
# OR
$ python3 sshbrute.py -ip <Server> -p <Port> -u <User> -d 0.3
```
***
## Help
You can see all the available options with the following command:
```
$ python3 sshbrute.py -h

usage: ss.py [-h] [--hostname HOSTNAME] [--port PORT] [--user USER] [--passlist PASSLIST] [--delay DELAY]
             [--background]

Start a SSH bruteforce attack !

options:
  -h, --help            show this help message and exit
  --hostname HOSTNAME, -ip HOSTNAME
                        Remote Ip of server. Default: localhost
  --port PORT, -p PORT  Port on which ssh is running. Default: 22
  --user USER, -u USER  User of ther remote machine. Default: root
  --passlist PASSLIST, -pl PASSLIST
                        Path to the password list file. Default: pass.txt
  --delay DELAY, -d DELAY
                        Delay between attempts. Default: 0.5
  --background          Only show successful attempts. Default: False
```
## For Developers
This tool can be improved. I would love to see an improved version of this tool.
You can use this tool for any purpose free of cost.
***
## Images
<p align="center">
<img title="SSHBrute" src="https://raw.githubusercontent.com/thexcoderz/SSHBrute/main/img-1.png" alt="SSHBrute"/>
</p>
<p align="center">
<img title="SSHBrute" src="https://raw.githubusercontent.com/thexcoderz/SSHBrute/main/img-3.png" alt="SSHBrute"/>
</p>
