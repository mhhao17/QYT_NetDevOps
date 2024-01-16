import socket
import sys
import struct
import hashlib
import pickle

# Bind address to UDP port
address = ('0.0.0.0', 6666)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)

print('UDP服務器就緒!等待客戶數據!')
while True:
    try:
        # 接收數據[注意: 此處限制了發送大小为512]
        recv_source_data = s.recvfrom(512)

        # 提取發送數據與socket訊息 (源地址, 源端口)
        rdata, addr = recv_source_data
        # 提取頭部訊息
        header = rdata[:16]

        unpack_header = struct.unpack('>HHLQ', header)
        version = unpack_header[0]
        pkt_type = unpack_header[1]
        seq_id = unpack_header[2]
        length = unpack_header[3]

        # 提取數據
        rdata = rdata[16:]
        # 提取MD5值
        data = rdata[:length]
        md5_recv = rdata[length:]
        md5_value = hashlib.md5(header + data).digest()

        # 如果本地计算的MD5值等于发送过来的MD5值
        if md5_recv == md5_value:
            print('=' * 80)
            print("{0:<30}:{1:<30}".format('數據源自於', str(addr)))
            print("{0:<30}:{1:<30}".format('數據序列號', seq_id))
            print("{0:<30}:{1:<30}".format('數據長度為', length))
            print("{0:<30}:{1:<30}".format('數據內容為', str(pickle.loads(data))))
        else:
            print('MD5校驗錯誤! ')
    except KeyboardInterrupt:
        sys.exit()
