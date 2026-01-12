#Downloads a file from the given URL to the specified output path.
import requests
import time
import logging

logging.basicConfig(level=logging.INFO)

def download_file(url, output_path, retries=3):
    attempt = 0

    while attempt < retries:
        try:
            logging.info(f"Attempt {attempt + 1}: Downloading file...")
            response = requests.get(url, timeout=20)
            response.raise_for_status()

            with open(output_path, "wb") as file:
                file.write(response.content)

            logging.info("File downloaded successfully")
            return output_path

        except Exception as e:
            logging.error(f"Download failed: {e}")
            attempt += 1
            time.sleep(2)

    raise Exception("File download failed after multiple retries")
