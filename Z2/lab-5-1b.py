while True:
    try:
        a = input('Enter ip address in format 10.0.1.1,range[0-255]:')
        ip = int(a.split('.')[0])
    except ValueError:
            print('Incorrect IPv4 address')
    else:
        if ip < 0 or ip > 255:
            print(('Inccorect IPv4 address').format(a))
        elif ip > 0 and ip <=127:
            print(('ip address {} class A,this unicast').format(a))
            break
        elif ip > 127 and ip <= 191:
            print(('ip address {} class B,this unicast').format(a))
            break
        elif ip > 191 and ip <= 223:
            print(('ip address {} class C,this unicast').format(a))
            break
        elif ip > 223 and ip <= 239:
            print(('ip address{} class D,this multicast').format(a))
            break
        elif a == '255.255.255.255':
            print(('local broadcast').format(a))
            break
        elif a == '0.0.0.0':
            print(('unassigned').format(a))
            break
        else:
            print ('unused')

