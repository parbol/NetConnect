import sys
import json
import ipaddress
import os
import time
import subprocess

configurationFile = './NetConnect.json'
workingDirectory = './'

def parseConfigurationFile():
    
    d = []
    try:
        with open(configurationFile, 'r') as f:
            try:
                d = json.load(f)
            except ValueError as e:
                print('Configuration file is corrupt')
                sys.exit()
    except IOError:
        print('Could not read file:', configurationFile)
        sys.exit()

    
    server = d['server']
    try:
        ip_object = ipaddress.ip_address(server)
    except ValueError:
        print('The IP format is incorrect')
        sys.exit()
    user = d['user']
    path = d['path']
    
    certificate = d['certificate']
    if not os.path.exists(certificate):
        print('Certificate could not be found')
        sys.exit()

    return server, user, certificate, path



if __name__=='__main__':

    server, user, certificate, path = parseConfigurationFile()
    
    print("scp", "-i", f"{certificate}", f"{user}@{server}:{path}", f"{workingDirectory}")
    process = subprocess.run(args=["scp", "-i", f"{certificate}", f"{user}@{server}:{path}", f"{workingDirectory}"], stdout=subprocess.PIPE, 
                                    stdin=subprocess.PIPE, encoding='utf8')

ssh -R [remote_addr:]remote_port:local_addr:local_port [user@]gateway_addr




