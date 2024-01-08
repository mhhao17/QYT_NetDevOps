import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *


def qytang_ping(ip):
    ping_pkt = IP(dst=ip)/ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return ip, True
#    else:
#        return ip, False


if __name__ == '__main__':
    print(qytang_ping('192.168.10.101'))
    #ping_pong = qytang_ping('192.168.10.101')
    #if ping_pong[1]:
    #    print(f'{ping_pong[0]} 通!')
    #else:
    #    print(f'{ping_pong[0]} 不通!')

    # ping_pong[0] //0 = ip
    # ping_pong[1] //1 = Ture/False
