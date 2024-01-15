from kamene.all import Ether, ARP, sendp
import time

def send_gratuitous_arp(interface, src_ip, src_mac, interval=1):
    # 構建ethernet frame
    ether_frame = Ether(dst="ff:ff:ff:ff:ff:ff", src=src_mac)

    # 構建 ARP 數據包，op=2 表示 ARP 響應
    arp_packet = ARP(op=2, hwsrc=src_mac, psrc=src_ip, hwdst="00:0c:29:80:ea:64", pdst=src_ip)

    # 合並ethernet frame 和 ARP 數據包
    packet = ether_frame / arp_packet

    # 發送數據包
    sendp(packet, iface=interface, verbose=False)

    while True:
        sendp(packet, iface=interface, verbose=False)
        time.sleep(interval)

interface = "ens224"  # 替換為你的網路接口
source_ip = "10.10.1.1"  # 替換為你的 IP 地址
source_mac = "00:0c:29:80:ea:64"  # 替換為你的 MAC 地址
send_interval = 2  # 發送數據包的時間間隔(秒)

send_gratuitous_arp(interface, source_ip, source_mac, interval=send_interval)

