import sys
import json
import ipaddress

configurationFile = '/etc/NetConnect.json'


def parseConfigurationFile():
    
    d = []
    try:
        with open(configurationFile, 'r') as f:
            try:
                d = json.loads(f)
            except ValueError as e:
                print('Configuration file is corrupt')
                sys.exit()
    except IOError:
        print('Could not read file:', configurationFile)
        sys.exit()

    server = d['server']
    try:
        ip_object = ipaddress.ip_address(server)
        print('IP of the server seems to be valid')
    except ValueError:
        print('The IP format is incorrect')
        sys.exit()
    
    path = d['path']
    certificate = d['certificate']
    


if __name__=='__main__':

    server, certificate = parseConfigurationFile()



