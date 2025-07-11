import xml.etree.ElementTree as ET
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def search_incoming_by_group_number(group_number, xml_path='dir_xml/groups.xml'):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    for group in root.findall('group'):
        number = group.find('number')
        if number is not None and number.text == str(group_number):
            incoming = group.find('timingExbytes/incoming')
            if incoming is not None:
                logging.info(f"Для group/number={group_number}: incoming = {incoming.text}")
                return incoming.text
            else:
                logging.info(f"Для group/number={group_number}: 'incoming' не знайдено")
                return None

    logging.info(f"group/number={group_number} не знайдено")
    return None


search_incoming_by_group_number(4)
