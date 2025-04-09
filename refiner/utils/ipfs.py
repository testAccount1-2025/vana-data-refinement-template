
import json
import logging
import os
import requests
from refiner.config import settings

IPFS_API_ENDPOINT = "https://vany.ipfs.ykyr.net"

def upload_json_to_ipfs(data):
    """
    Uploads JSON data to IPFS using the specified IPFS gateway.
    :param data: JSON data to upload (dictionary or list)
    :return: IPFS hash
    """
    try:
        # Create a temporary file for the JSON data
        temp_file_path = os.path.join(settings.OUTPUT_DIR, "temp_json.json")
        with open(temp_file_path, 'w') as f:
            json.dump(data, f)
        
        # Upload the file and get the hash
        ipfs_hash = upload_file_to_ipfs(temp_file_path)
        
        # Clean up the temporary file
        os.remove(temp_file_path)
        
        logging.info(f"Successfully uploaded JSON to IPFS with hash: {ipfs_hash}")
        return ipfs_hash

    except Exception as e:
        logging.error(f"An error occurred while uploading JSON to IPFS: {e}")
        raise e

def upload_file_to_ipfs(file_path=None):
    """
    Uploads a file to IPFS using the specified IPFS gateway.
    :param file_path: Path to the file to upload (defaults to encrypted database)
    :return: IPFS hash
    """
    if file_path is None:
        # Default to the encrypted database file
        file_path = os.path.join(settings.OUTPUT_DIR, "db.libsql.pgp")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        with open(file_path, 'rb') as file:
            files = {
                'file': file
            }
            response = requests.post(
                f"{IPFS_API_ENDPOINT}/api/v0/add",
                files=files
            )
        
        response.raise_for_status()
        result = response.json()
        ipfs_hash = result['Hash']
        logging.info(f"Successfully uploaded file to IPFS with hash: {ipfs_hash}")
        return ipfs_hash

    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred while uploading file to IPFS: {e}")
        raise e

# Test with: python -m refiner.utils.ipfs
if __name__ == "__main__":
    ipfs_hash = upload_file_to_ipfs()
    print(f"File uploaded to IPFS with hash: {ipfs_hash}")
    print(f"Access at: {IPFS_API_ENDPOINT}/ipfs/{ipfs_hash}")
    
    test_data = {"test": "data"}
    ipfs_hash = upload_json_to_ipfs(test_data)
    print(f"JSON uploaded to IPFS with hash: {ipfs_hash}")
    print(f"Access at: {IPFS_API_ENDPOINT}/ipfs/{ipfs_hash}")
