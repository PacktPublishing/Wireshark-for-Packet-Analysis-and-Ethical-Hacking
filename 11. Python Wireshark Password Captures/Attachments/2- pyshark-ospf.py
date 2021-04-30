#=====================================================                 
#OSPF:
#=====================================================                 

import pyshark

capture = pyshark.LiveCapture ('eth0')
for packet in capture:
    if 'OSPF' in packet:
        print('OSPF password: ' + packet.ospf.auth_simple)