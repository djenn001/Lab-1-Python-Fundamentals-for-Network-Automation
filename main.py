
import logging
from src.network_device import NetworkDevice
from src.parser_utils import parse_json, parse_yaml, parse_xml, parse_csv


logging.basicConfig(
    filename="logs/lab.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    logging.info("LAB1_START")
    devices = parse_json("data/devices.json")
    interfaces = parse_yaml("data/interfaces.yaml")
    vlans = parse_xml("data/vlans.xml")
    inventory = parse_csv("data/inventory.csv")
    

    for interface in interfaces["interfaces"]:
        msg = f"Interface {interface['name']} is {interface['status']}"
        print(msg)
        logging.info(f"INTERFACE_MSG: {msg}")

    for device in inventory:
        msg = f"Device {device['hostname']} is a {device['location']} {device['role']}"
        print(msg)
        logging.info(f"DEVICE_MSG: {msg}")

    for vlan in vlans:
        msg = f"VLAN {vlan['id']} is the {vlan['name']}"
        print(msg)
        logging.info(f"VLAN_MSG: {msg}")

    for device_data in devices:
        device = NetworkDevice(
            device_data["hostname"],
            device_data["ip"],
            device_data["type"]
        )
        device.summarize()

    logging.info("LAB1_END")
    

if __name__ == "__main__":
    main()


