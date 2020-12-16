command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
c1 = {1,3,10,20,30,100}
c2 = {1,3,100,200,300}
print('switchport trunk allowed vlan')
print(c1.intersection(c2))
