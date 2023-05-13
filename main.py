import os
from dotenv import load_dotenv
from configuration import get_config
import logging
from service import Service

load_dotenv()
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

SERVICE_BASE_DIR = os.path.dirname(__file__)

environment = os.getenv("ENVIRONMENT")
logger.info(f"Setting up Inertial Sensor service for environment [{environment}]")
configuration = get_config(environment)

if __name__ == '__main__':
    service = Service(configuration)
    service.start_ipc_consumer_thread()  # Kafka IPC topic consumer thread
