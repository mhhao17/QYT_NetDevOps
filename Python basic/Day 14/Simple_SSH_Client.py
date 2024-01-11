from qytang_ssh import qytang_ssh
from argparse import ArgumentParser
usage = "python Simple_SSH_Client.py -i ipaddr -u username -p password -c command"

parser = ArgumentParser(usage=usage)

parser.add_argument('-i', '--ipaddr', type=str, default='', help='SSH Server')
parser.add_argument('-u', '--username', type=str, default='root', help='SSH Username')
parser.add_argument('-p', '--password', type=str, default='Netdevops', help='SSH Password')
parser.add_argument('-c', '--command', type=str, default='ls', help='Shell Command')

args = parser.parse_args()

print(qytang_ssh(args.ipaddr, args.username, args.password, cmd=args.command))



