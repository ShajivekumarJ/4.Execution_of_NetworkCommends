import os

print("NETWORK COMMAND EXECUTION")

print("\n1. IP Configuration")
os.system("ipconfig")

print("\n2. Ping Test")
os.system("ping google.com")

print("\n3. Trace Route")
os.system("tracert google.com")

print("\n4. Netstat")
os.system("netstat")

print("\n5. ARP Table")
os.system("arp -a")

print("\n6. DNS Lookup")
os.system("nslookup google.com")