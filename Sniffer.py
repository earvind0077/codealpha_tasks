from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        print("\n--- New Packet Captured ---")
        print("Source IP:", ip_layer.src)
        print("Destination IP:", ip_layer.dst)
        print("Protocol:", ip_layer.proto)

        # Check Protocol Type
        if packet.haslayer(TCP):
            print("Protocol Type: TCP")
            print("Source Port:", packet[TCP].sport)
            print("Destination Port:", packet[TCP].dport)

        elif packet.haslayer(UDP):
            print("Protocol Type: UDP")
            print("Source Port:", packet[UDP].sport)
            print("Destination Port:", packet[UDP].dport)

        elif packet.haslayer(ICMP):
            print("Protocol Type: ICMP")

        # Print payload (if exists)
        if packet.haslayer(TCP):
            payload = bytes(packet[TCP].payload)
            print("Payload:", payload)

# Capture packets
print("Starting Packet Sniffer...")
sniff(prn=packet_callback, count=10)
