
# Error Logs
import logging

logging.basicConfig(
    level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
        logging.FileHandler('logs/app_errors.log'),
        logging.StreamHandler()
    ]
)
