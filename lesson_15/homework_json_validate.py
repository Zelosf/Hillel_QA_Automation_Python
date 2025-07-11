import json
import os
import logging


logging.basicConfig(
    filename='json__hlushko.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def validate_json_files(folder_path='dir_json'):
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            full_path = os.path.join(folder_path, filename)
            try:
                with open(full_path, encoding='utf-8') as f:
                    json.load(f)
            except Exception as e:
                logging.error(f"{filename}: {e}")


validate_json_files()