import paramiko
import re


def qytang_ssh(ip, username, password, port=22, cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x


def ssh_get_route(ip, username, password, port=22):
    route_n_result = qytang_ssh(ip, username, password, port, cmd='route -n')
    ipv4_gw_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    matches = ipv4_gw_pattern.findall(route_n_result)
    ipv4_gw = matches[1]
    return ipv4_gw


if __name__ == '__main__':
    print(qytang_ssh('192.168.10.138', 'root', 'Netdevops'))
    print(qytang_ssh('192.168.10.138', 'root', 'Netdevops', cmd='pwd'))
    print('網關為:')
    print(ssh_get_route('192.168.10.138', 'root', 'Netdevops'))
