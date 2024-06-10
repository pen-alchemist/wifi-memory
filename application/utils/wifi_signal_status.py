from scapy.all import sniff
from scapy.layers.dot11 import Dot11


def monitor_signals(iface):
    """Sniffs for beacon frames and displays real-time signal levels."""
    print("Monitoring WiFi signal levels...")
    sniff(iface=iface, prn=lambda packet: process_packet(packet), filter="type 0 and subtype 8", store=False)


def process_packet(packet):
    """Processes beacon frames and updates signal strength."""
    if packet.haslayer(Dot11):
        bssid = packet[Dot11].addr2
        # Extract signal strength (received signal strength indication - RSSI)
        rssi = packet.dBm_antsignal
        print(f"BSSID: {bssid} - Signal Strength (RSSI): {rssi} dBm")
