ip = '192.168.3.4'
subnet = '255.255.255.0'
ip = ip.split('.')
subnet = subnet.split('.')
print(ip)
print(subnet)
ipBin = []
subnetBin = []
ipBin = [bin(x)[2:].zfill(8) for x in map(int, ip)]
subnetBin = [bin(x)[2:].zfill(8) for x in map(int, subnet)]

print(ipBin)
print(subnetBin)


def get_min(ip1, subnet1):
    ip_first = []
    temp_ip = []
    temp1 = []
    temp2 = []
    for i in range(4):
        temp1.append(ip1[i])
        temp2.append(subnet1[i])
        for j in range(8):
            if temp1[0][j] == temp2[0][j] and temp1[0][j] != '0':
                temp_ip.append('1')
            else:
                temp_ip.append('0')
        a = ''.join(temp_ip)
        ip_first.append(a)
        temp_ip = []
        temp1 = []
        temp2 = []
    return ip_first


firstIp = get_min(ipBin, subnetBin)
firstIp = [int(x, 2) for x in firstIp]
print(firstIp)
