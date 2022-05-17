"""
Написать программу, которая проверяет наличие открытых портов по указанному адресу (IP или доменному имени).
Вывести на экран все открытые порты из указанного диапазона.
"""

import socket

host_name = input("Please enter host name or IP address: ")
port_initial = int(input("Please enter initial port: "))
port_last = int(input("Please enter last port: "))

target = socket.gethostbyname(host_name)

print("Scanning %s" % target)

for port in range(port_initial, port_last+1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)
    result = s.connect_ex((target, port))
    if result == 0:
        print("Port %s is open" % port)
    s.close()
