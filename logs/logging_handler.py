
# Error Logs
import logging
from os.path import join

logging.basicConfig(
    level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
        logging.FileHandler(join('logs', 'app_errors.log')),
        logging.StreamHandler()
    ]
)
