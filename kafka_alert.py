import logging

from kafka.consumer.fetcher import ConsumerRecord
from exceptions.filter_out import FilterOutException

from assemblers.ipc_command_assembler import IpcCommandAssembler

logger = logging.getLogger(__name__)


class KafkaAlertApi:
    def __init__(self, configuration, local_storage, timer_callback):
        self._ipc_command_assembler = IpcCommandAssembler(configuration, local_storage, timer_callback)

    def accept_record(self, kafka_consumer_record: ConsumerRecord):
        try:
            logger.info(f"Processing ConsumerRecord from offset: [{kafka_consumer_record.offset}]")
            self._ipc_command_assembler.assemble(kafka_consumer_record)
        except FilterOutException:
            logger.exception(f"The kafka event is filtered out.")
        except Exception as exception:
            logger.exception(f"The kafka event could not be assembled {exception}")
