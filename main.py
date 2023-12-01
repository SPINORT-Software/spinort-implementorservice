import os
from dotenv import load_dotenv
from configuration import get_config
import logging
from service import Service
from configparser import ConfigParser

load_dotenv()
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

confluent_properties_file = open("kafka_client_properties.ini")
confluent_config_parser = ConfigParser()
confluent_config_parser.read_file(confluent_properties_file)
confluent_config = {**dict(confluent_config_parser['default']), **dict(confluent_config_parser['consumer'])}

SERVICE_BASE_DIR = os.path.dirname(__file__)

environment = os.getenv("ENVIRONMENT")
logger.info(f"Setting up Inertial Sensor service for environment [{environment}]")
configuration = get_config(environment)

if __name__ == '__main__':
    service = Service(configuration, confluent_config)
    service.start_ipc_consumer_thread()  # Kafka IPC topic consumer thread
