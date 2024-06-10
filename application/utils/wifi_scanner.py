from scapy.all import *
from scapy.layers.dot11 import Dot11Elt, Dot11, RadioTap


def sniff_beacon(interface):
    """Sniffs for beacon frames and displays network information."""
    print("Scanning WiFi networks...")
    # Filter for beacon frames (type 0, subtype 8)
    # promisc=True enables monitor mode (requires root)
    packets = sniff(iface=interface,
                    count=10,
                    filter="type 0 and subtype 8",
                    promisc=True)

    info_results = []

    for packet in packets:
        # Extract SSID (network name) from beacon frame
        ssid = packet[Dot11Elt].info
        # Extract BSSID (MAC address of access point)
        bssid = packet[Dot11].addr2
        # Extract channel
        channel = packet[RadioTap].channel
        # Extract signal strength (received signal strength indication - RSSI)
        rssi = packet.dBm_antsignal

        scan_result = {'ssid': ssid,
                       'bssid': bssid,
                       'channel': channel,
                       'rssi': rssi}

        info_results.append(scan_result)
