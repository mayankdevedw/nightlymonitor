import enum
import logging
import time
from objects.shared_object import SharedObject
from objects.gtn_object import GTN
from quanta.quanta_request import get_gtn_current_state
logger = logging.getLogger(__name__)


class States(enum.Enum):
    executing = "EXECUTING"
    provisioning = "PROVISIONING"
    installing = "INSTALLING"
    install_success = "INSTALLATION_SUCCEEDED"
    started = "STARTED"
    provision_success = "PROVISIONING_SUCCEEDED"
    execution_failed = "INSTALLATION_FAILED"


class DeploymentThread(object):

    def __init__(self, gtn_queue, trigger_queue, object_dict):
        self._object_dict = object_dict
        self._gtn_queue = gtn_queue
        self._trigger_queue = (trigger_queue)

    def monitor_thread(self):
        while True and self._get_total_failed():
            gtn_id = self._gtn_queue.get()
            logger.info("Processing gtn_id %s", gtn_id)
            # Make Request for GTN_ID
            status = get_gtn_current_state(gtn_id)
            time.sleep(600)
            if status == States.execution_failed.value:
                self._gtn_queue.put(gtn_id)
                SharedObject.increment_fail_count()
                (self._object_dict["gtn_id"]).re_trigger = True
                logger.info("Current Failing Percentage is %s", str(self._get_total_failed()))
                self._trigger_queue.put(gtn_id)
            else:
                self._gtn_queue.put(gtn_id)

    def _get_total_failed(self):
        total_failed = 0
        for key, value in self._object_dict.values():
            gtn = GTN(self._object_dict[key])
            if gtn.re_trigger:
                total_failed += 1

        return total_failed/len(self._object_dict)*100


