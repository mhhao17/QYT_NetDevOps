import socket
import struct
import hashlib
import pickle


def udp_send_data(ip, port, data_list):
    address = (ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    version = 1
    pkt_type = 1
    seq_id = 1
    for x in data_list:
        # ---header設計---
        # 2字節 version 1
        # 2字節 type, 1為請求，2為響應 (由於是UDP單向流量!所有此次試驗只有請求)
        # 4字節 ID
        # 8字節 length

        # |  2  |   2  |    4   |    8    |
        # | ver | type |   ID   |   len   |

        # ---變長數據部份---
        # 使用pickle轉換數據

        # 把Python數據或者對象Pickle成為二進制數據
        send_data = pickle.dumps(x)
        # 按照頭部設計構建頭部
        header = struct.pack('>HHLQ', version, pkt_type, seq_id, len(send_data))
        # ---HASH校驗---
        # 16 字節 MD5值
        md5_checksum = hashlib.md5(header + send_data).digest()

        # 拼接頭部+發送數據+MD5值，然後發送到目的服務器
        s.sendto(header + send_data + md5_checksum, address)
        seq_id += 1
    s.close()

if __name__ == '__main__':
    from datetime import datetime
    user_data = ['乾頤堂', [1, 'qytang', 3], {'qytang': 1, 'test': 3}, {'datetime': datetime.now()}]
    udp_send_data('10.10.1.200', 6666, user_data)
