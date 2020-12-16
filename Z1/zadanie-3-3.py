string1 = ' switchport trunk allowed vlan 1,3,10,20,30,100  '
commands = string1.strip().split()
print(commands)
var = ['switchport', 'trunk', 'allowed', 'vlan', '1,3,10,20,30,100']
vlans = commands[-1].split(',')
print(vlans)
vara = ['1', '3', '10', '20', '30', '100']
