import paramiko


def qytang_ssh(ip, username, password,  cmd='ls', port=22):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    return stdout.read().decode()


if __name__ == '__main__':
    # print(qytang_ssh('192.168.10.138', 'root', 'Netdevops'))
    print(qytang_ssh('192.168.10.101', 'admin', 'Cisc0123', cmd='sh ip int bri'))
