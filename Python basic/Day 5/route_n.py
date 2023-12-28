import os
import re

route_n_result = os.popen('route -n').read()
ipv4_gw_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
matches = ipv4_gw_pattern.findall(route_n_result)
ipv4_gw = matches[1]

print(f'網關為:{ipv4_gw}')
