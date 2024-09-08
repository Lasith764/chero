
#import scapy
#chero lasith ruwantha 
import scapy.all as scapy
import re 
print('''\033[0:32
███░░░░██
████░░░██
██░██░░██
██░░██░██
██░░░████

███████
██
█████
██
███████

████████
░░░██
░░░██
░░░██
░░░██''')

ip_add_reange_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*s")

while True:
  ip_add_reange_enter = input("\nenter ip adres and reang: ")
  if ip_add_reange_pattern.search(ip_add_reange_enter)
    print(f"{ip_add_reange_enter} is valid ip adres reang")
    break

arp_result = scapy.arping(ip_add_reange_enter)