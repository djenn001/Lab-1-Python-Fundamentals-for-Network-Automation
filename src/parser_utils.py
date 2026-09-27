import csv
import json
import logging
import xml.etree.ElementTree as ET
import yaml

def parse_json(filepath):
    try:
        with open(filepath, "r") as file:
            data = json.load(file)

        logging.info("PARSE_JSON_SUCCESS")
        return data
    except FileNotFoundError:
        logging.error("PARSE_JSON_ERROR")
        return []
    
    except json.JSONDecodeError:
        logging.error("PARSE_JSON_ERROR")
        return [] 
    
def parse_yaml(filepath):
    try:
        with open(filepath, "r") as file:
            data = yaml.safe_load(file)
        logging.info("PARSE_YAML_SUCCESS")
        return data 
        
    except FileNotFoundError:
        logging.error("PARSE_YAML_ERROR")
        return []
        
    except yaml.YAMLError:
        logging.error("PARSE_YAML_ERROR")
        return[]
    
def parse_xml(filepath):
    try: 
        tree = ET.parse(filepath)
        root = tree.getroot()
        vlans = root.findall("vlan")
        results = []

        for vlan in vlans:
            vlan_id = vlan.find("id").text
            vlan_name = vlan.find("name").text
            results.append({"id": vlan_id, "name": vlan_name})
        
        logging.info("PARSE_XML_SUCCESS")
        return results
    except FileNotFoundError:
        logging.error("PARSE_XML_ERROR")
        return []
    
    except ET.ParseError:
        logging.error("PARSE_XML_ERROR")
        return []
    


def parse_csv(filepath):
    try:
        with open(filepath, "r") as file:
            reader = csv.DictReader(file)
            data = list(reader)
        logging.info("PARSE_CSV_SUCCESS")
        return data
    
    except FileNotFoundError:
        logging.error("PARSE_CSV_ERROR")
        return []
    
    except csv.Error:
        logging.error("PARSE_CSV_ERROR")
        return []
    



                         
