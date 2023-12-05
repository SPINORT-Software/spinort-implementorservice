import json
import os
from dotenv import load_dotenv
import logging
from localStoragePy import localStoragePy

from consumer import Consumer
from commands import Commands
from kafka_alert import KafkaAlertApi
from producer import Producer
from configuration import AlertConfiguration

load_dotenv()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

SERVICE_BASE_DIR = os.path.dirname(__file__)


class Service:
    def __init__(self, configuration: AlertConfiguration, confluent_config):
        self.local_storage = localStoragePy(configuration.get_local_storage_workspace_name(),
                                            configuration.get_local_storage_workspace_backend())
        self.producer = Producer(confluent_config, configuration.get_ipc_engine_alerts_topic())
        self.kafka_alert = KafkaAlertApi(configuration, self.local_storage, self.send_message_to_engine)
        self.configuration = configuration
        self.confluent_config = confluent_config

    def start_ipc_consumer_thread(self):
        consumer = Consumer(
            self.confluent_config,
            self.configuration.get_kafka_ipc_topic(),
            self.kafka_alert.accept_record
        )
        consumer.start()

    def send_message_to_engine(self, **kwargs):
        message = {
            'command': Commands.create_new_treatment_cycle.name,
            'session': kwargs.get('session_id')
        }
        self.producer.produce(json.dumps(message))
