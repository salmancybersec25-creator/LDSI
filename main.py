# LDSI - Local Device Security Inventory
# Version 1.0 - Basic Device Inventory
# Author: Your Name Here

import sys
import socket
import platform
import psutil
import json
from datetime import datetime

# --- Banner ---
print("=====================================")
print("  Local Device Security Inventory")
print("  Version 1.0 - Basic Inventory")
print("=====================================")

# --- Python version ---
python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
print(f"Python version: {python_version}")

# --- Hostname ---
hostname = platform.node()
print(f"Hostname:       {hostname}")

# --- Operating system ---
os_name = platform.system()
os_release = platform.release()
os_version = platform.version()

print(f"Operating system: {os_name}")
print(f"OS release:     {os_release}")
print(f"OS version:     {os_version}")

# --- Collect network adapter data ---
network_records = []
interfaces = psutil.net_if_addrs()

for adapter_name, addr_list in interfaces.items():
    for addr in addr_list:
        if addr.family == socket.AF_INET:
            network_records.append({
                "adapter": adapter_name,
                "ipv4":    addr.address,
                "netmask": addr.netmask,
            })

# --- Print for the human reading the terminal ---
print("Network adapters (IPv4):")
for rec in network_records:
    print(f"  {rec['adapter']}: {rec['ipv4']} ({rec['netmask']})")

# --- Timestamp ---
now = datetime.now()
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Report generated: {formatted_time}")

# --- Build the report structure ---
report = {
    "report_metadata": {
        "tool":         "LDSI",
        "tool_version": "1.0",
        "generated_at": formatted_time,
    },
    "system": {
        "hostname":       hostname,
        "os_name":        os_name,
        "os_release":     os_release,
        "os_version":     os_version,
        "python_version": python_version,
    },
    "network": network_records,
}

# --- Write the JSON report ---
filename = f"report_{now.strftime('%Y%m%d_%H%M%S')}.json"
with open(filename, "w", encoding="utf-8") as f:
    json.dump(report, f, indent=2)

print(f"Report saved to: {filename}")