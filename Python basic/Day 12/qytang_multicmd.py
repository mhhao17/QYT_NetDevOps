import paramiko
import time


def configure_router(ip, username, password, cmd_list, enable='', wait_time=2, verbose=True):
    ssh = paramiko.SSHClient()  # 創建SSH Client
    ssh.load_system_host_keys()  # 載入系統SSH密鑰
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 添加新的SSH密鑰
    ssh.connect(ip, port=22, username=username, password=password, timeout=5, compress=True)
    chan = ssh.invoke_shell()  # 啟用交互式shell
    time.sleep(wait_time)   # 等待網路設備回應
    output = ''
    if enable and '>' in chan.recv(2048).decode():  # 如果提示符是>，說明沒有進入特權模式
        chan.send('enable'.encode())  # 進入特權模式
        chan.send(b'\n')  # Enter
        chan.send(enable.encode())  # 輸入特權模式密碼
        chan.send(b'\n')  # Enter
        time.sleep(wait_time)  # 等待網路設備回應
        chan.recv(2048).decode()  # 獲取路由器返回的訊息
    for command in cmd_list:
        chan.send(command.encode())   # 發送配置命令
        chan.send(b'\n')  # Enter
        time.sleep(wait_time)  # 等待時間
        output += chan.recv(2048).decode()  # 讀取回應
    if verbose:
        print(output)
    ssh.close()  # 關閉SSH session


if __name__ == '__main__':
    commands_to_send = ['terminal length 0', 'show version', 'config terminal', 'router ospf 1',
                        'network 192.168.0.0 255.255.255.0 area 0', 'end', 'write memory',
                        # 添加更多配置命令...
                        ]
    configure_router('192.168.10.101', 'admin', 'Cisc0123', commands_to_send, enable='Cisc0123')

