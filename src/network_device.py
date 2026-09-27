#python3 
import logging 

class NetworkDevice:
 
    def __init__(self, hostname, ip, type):
        self.hostname = hostname
        self.ip = ip
        self.type = type
    def summarize(self):
        msg = f"[DEVICE_SUMMARY]: {self.hostname} ({self.type}) - {self.ip}"
        print(msg)
        logging.info(msg)
        return msg