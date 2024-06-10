from django.shortcuts import render

from wifimemory.application.utils.ip_address import get_ip_address
from wifimemory.application.utils.wifi_scanner import sniff_beacon
from wifimemory.application.utils.wifi_signal_status import monitor_signals


def ip_address(request):
    """View for displaying IP address."""
    # Logic to get IP address
    ip = get_ip_address()
    if ip:
        print(f"Your IP address on eth0 is: {ip}")
    else:
        print("Failed to get IP address.")

    # Replace with your IP retrieval function
    context = {'ip_address': ip}
    return render(request, 'homewifi/ip_address.html', context)


def wifi_scanner(request):
    """View for displaying WiFi scanner results."""
    # Logic to scan for WiFi networks
    scan_results = sniff_beacon()
    context = {'scan_results': scan_results}
    return render(request, 'homewifi/wifi_scanner.html', context)


def wifi_signal(request):
    """View for displaying real-time WiFi signal status."""
    # Logic to get real-time signal strength
    # This might involve a separate thread or background process
    signal_data = monitor_signals()
    context = {'signal_data': signal_data}
    return render(request, 'homewifi/wifi_signal.html', context)
