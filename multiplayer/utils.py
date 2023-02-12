import os
import re


def get_ip_list():
    try:
        global os
        devices = []
        for device in os.popen('arp -a'): devices.append(device)
        result = [device for device in devices if not '(incomplete)' in device and not 'ff:ff:ff:ff:ff:ff' in device and '192.168.' in device]
        result = [re.findall(r'\(.*?\)', el)[0][1:-1] for el in result]
        return(result)
    except:
        return ('Не получилось определить ip адреса в вашей сети, введите вручную')





