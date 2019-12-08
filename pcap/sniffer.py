import dpkt
import socket
from scapy.sendrecv import sniff
from scapy.utils import wrpcap
import scapy.all as scapy
from scapy.utils import PcapReader
while True:
    dpkt = sniff(count=1)
    dpkt.setfilter = 'TCP'
    wrpcap("test.pcap", dpkt)
    packets = scapy.rdpcap('test.pcap')
    for head in packets:
        if 'TCP' in head:
            s = repr(head)
            print(s)
            # print("数据报的源地址为："+head['IP'].src)
            # print("数据报的目的地址为："+head['IP'].dst)
            #