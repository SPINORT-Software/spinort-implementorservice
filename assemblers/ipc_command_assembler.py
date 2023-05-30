from .kafka_assembler import KafkaAssembler
from commands import Commands
from gpio_apply import GpioApply

import os, sys
import logging
import json

logger = logging.getLogger(__name__)


class IpcCommandAssembler(KafkaAssembler):
    def __init__(self, configuration, local_storage):
        self._configuration = configuration

        self._session_id_key = configuration.get_environ_name_session_id()
        self._session_type_key = configuration.get_environ_name_session_type()
        self._step_id_key = configuration.get_environ_name_calibration_step_id()
        self._data_send_allow_key = configuration.get_environ_name_data_send_allow()
        self._local_storage = local_storage
        self._gpio_app = GpioApply()

    def assemble(self, kafka_consumer_record):
        """
        Set the Environment Variables received in the Command from the Smartback Backend engine.
        In the calibration start Command:
        :param kafka_consumer_record:
        :return:
        """
        original = kafka_consumer_record.value.decode("utf-8")
        original_event = json.loads(original)

        try:
            if "command" not in original_event:
                logger.info(
                    f"Not enough data available in the command message to assemble. Dropping the message {original_event}")
                return False

            command = original_event.get("command")
            logger.info(f"Received command [{command}] from ipc topic.")

            if command == Commands.implement_treatment_result.name:
                """
                Receive stimulation data from SPINORT Engine.                
                """
                session_id_value = original_event.get("session")
                stimulation_energy = int(original_event.get("energy"))
                stimulation_side = original_event.get("side")

                logger.info("Stimulation data is received from the engine.")
                logger.info(original_event)
                self._gpio_app.apply_pwm(stimulation_energy)
            else:
                logger.info(f"An unrecognized command is provided. Command = [{command}]")

        except Exception as e:
            logger.info(f"There was an error processing the command: {str(e)}")
            logger.info(f"The original event is {original_event}")
