from scapy.all import sniff

def packet_callback(packet):
    print("\nPacket Captured:")
    print(packet.summary())

print("=== Simple Packet Sniffer ===")
print("Capturing network packets...")
print("Press Ctrl + C to stop.\n")

sniff(prn=packet_callback, store=False)
