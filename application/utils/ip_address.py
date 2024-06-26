import netifaces


def get_ip_address(interface="eth0"):
    """Gets the IP address of a specific network interface."""
    try:
        addrs = netifaces.ifaddresses(interface)
        return addrs[netifaces.AF_INET][0]['addr']
    except (ValueError, KeyError):
        print(f"Error retrieving IP address for interface {interface}")
        return None
