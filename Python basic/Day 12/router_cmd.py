import paramiko
import time


def router_cmd(ip, username, password):
    ssh_client = paramiko.SSHClient()  # 創建SSH Client
    ssh_client.load_system_host_keys()  # 加載系统SSH密鑰
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 添加新的SSH密鑰
    ssh_client.connect(hostname=ip, username=username, password=password, timeout=5, compress=True)  # SSH连接
    command = ssh_client.invoke_shell()  # 啟用交互式shell
    time.sleep(1)  # 等待網路設備回應
    command.recv(2048).decode()  # 獲取路由器返回的訊息
    command.send('config ter\n'.encode())  # 發送配置命令
    command.send(b'\n')
    time.sleep(2)
    command.send('router ospf 1\n'.encode())
    command.send(b'\n')
    time.sleep(2)
    output = command.recv(65536).decode()
    print(output)
    ssh_client.close()


if __name__ == '__main__':
    router_cmd('192.168.10.101', 'admin', 'Cisc0123')


