reader = open('1.csv','r')
file = reader.read().splitlines()
reader.close()

#print(file)

for rows in file:
  rows=rows.split(',')
#  print(rows)

  if len(rows[0]) != 0 and len(rows[1]) != 0 and len(rows[2]) != 0:

    HOST_IPADDR= rows[0]
#    print(HOST_IPADDR)

    INTERFACE = rows[1]
#    print(INTERFACE)

    VLAN_VOICE = rows[2]
#    print(VLAN_VOICE)

    print('host is:' + HOST_IPADDR)
    print('configure Terminal')
    print('interface ' + INTERFACE)
    print('switchport voice vlan ' + VLAN_VOICE)

    ANSWER = raw_input("Continue? yes or no: ")
#    ANSWER = str(ANSWER)
    print(ANSWER)
    if ANSWER != 'yes' and ANSWER != 'YES':
      print('skipping')
      continue

    else:
      print('thank you')
    print(' ')
    print('next')
    print(' ')
