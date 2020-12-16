mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cisco = []
for i in mac:
    newmac = str(i)
    newmac =newmac.replace(':','.')
    mac_cisco.append(newmac)
print(mac_cisco)
