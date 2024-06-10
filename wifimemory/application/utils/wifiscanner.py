from scapy.all import *


def sniff_beacon(iface):
    """Sniffs for beacon frames and displays network information."""
    print("Scanning WiFi networks...")
    # Filter for beacon frames (type 0, subtype 8)
    # promisc=True enables monitor mode (requires root)
    packets = sniff(iface=iface, count=10, filter="type 0 and subtype 8", promisc=True)

    for packet in packets:
        # Extract SSID (network name) from beacon frame
        ssid = packet[Dot11Elt].info
        # Extract BSSID (MAC address of access point)
        bssid = packet[Dot11].addr2
        # Extract channel
        channel = packet[Radio].channel
        # Extract signal strength (received signal strength indication - RSSI)
        rssi = packet.dBm_antsignal

        print(f"SSID: {ssid}")
        print(f"BSSID: {bssid}")
        print(f"Channel: {channel}")
        print(f"Signal Strength (RSSI): {rssi} dBm")
        print("-" * 30)


# Get user input for network interface
iface = input("Enter your wireless interface (e.g., wlan0): ")

# Start sniffing for beacons
sniff_beacon(iface)

print("Scan completed!")
