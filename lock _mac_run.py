import os
import sys
import time
import uuid

def get_mac_address():
    node = uuid.getnode()
    mac = uuid.UUID(int=node).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])


def check_license(licensed_mac_address):
    cur_mac_address = get_mac_address()
    if licensed_mac_address == cur_mac_address:
        return True
    else:
        print('cur_mac_address:{} is not the same of licensed_mac_address{}'.format(
            cur_mac_address, licensed_mac_address))

def check_license_00e04c680325():
    licensed_mac_address = '00:e0:4c:68:03:25'
    if check_license(licensed_mac_address):
        print('check license success!')
        return True
    else:
        print('check license failed!')
        return False
 
 if __name__ == '__main__':
    
    check_license_00e04c680325()
