import os
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command

nr = InitNornir(config_file="nornir.yaml")

# Code so automated tests will run properly
nr.inventory.groups["cisco"].password = os.environ["NORNIR_PASSWORD"]

results = nr.run(task=netmiko_send_command, command_string="show ip int brief")
print()
for k, v in results.items():
    print("-" * 50)
    print(k)
    print(v[0].result)
    print("-" * 50)
print()
