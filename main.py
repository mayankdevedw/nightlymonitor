# Nightly Monitoring Bot
import Queue

from monitor.deployment_thread import DeploymentThread
from objects.gtn_object import GTN


class NightlyMonitoringBot(object):

    def __init__(self, gtn_set, run_set_id, run_env='ycloud',
                 threshold_percentage=50, max_rerun=2, initial_wait=60, interval_wait=30):
        # Initialising the parameters
        self.gtn_set = gtn_set
        self.run_set_id = run_set_id
        self.run_env = run_env
        self.threshold_percentage = threshold_percentage
        self.max_rerun = max_rerun
        self.initial_wait = initial_wait
        self.interval_wait = interval_wait

        # Dictionary placeholder for <key: GTN> : <value: GTN_Object>
        self.gtn_object_dict = {}

        # Blocking Queue to create individual Threads to monitor them
        self.gtn_queue = Queue.Queue(maxsize=100)  # By Default Python Queues are Blocking Queue

        # Empty Queue to Keep Track of Trigger GTNs
        self.trigger_queue = Queue.Queue(maxsize=50)

        # Preparing the GTN Object and GTN Queue
        for cur_gtn in self.gtn_set:
            self.gtn_object_dict[cur_gtn] = GTN(cur_gtn, run_set_id)
            self.gtn_queue.put(cur_gtn)

        dep_thread_object = DeploymentThread(self.gtn_queue, self.trigger_queue, self.gtn_object_dict)
        # TODO: dep_thread_object.monitor_thread()


if __name__ == '__main__':
    # Takes List of GTN IDs and/or RunSetID
    GTN_SET = {1515537, 1515536, 1515535, 1515534, 1515533, 1515531, 1515529, 1515527, 1515520, 1515517,
               1515514, 1515502, 1515498, 1515495, 1515494, 1515492, 1515491, 1515490, 1515489, 1515488,
               1515487, 1515486, 1515485, 1515484, 1515483, 1515480, 1515479, 1515477, 1515476, 1515475,
               1515474, 1515473, 1515470, 1515469, 1515468, 1515467, 1515466, 1514973, 1514972, 1514970,
               1514965, 1514964, 1514963, 1514962, 1514961, 1514960, 1514959, 1514958, 1514957, 1514956,
               1514955, 1514954, 1514953, 1514951, 1514950, 1514949, 1514948, 1514947, 1514946, 1514943,
               1514942, 1514941, }
    # Link- https://quanta.infra.cloudera.com/#/jobHistory?endTime=1570791600000&startTime=1570773600000&users=cdp-10-reaper
    cur_run_set_id = "setID_001"

    nemo_bot = NightlyMonitoringBot(GTN_SET, cur_run_set_id)
