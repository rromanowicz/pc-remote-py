import logging
from tools import tools
import threading
from datetime import datetime, timedelta


class Shutdown:
    def __init__(self, os: str):
        self.__os = os.lower()
        self.__cmd = tools.commands[self.__os]['shutdown']['cmd']

    __fmt = "%(asctime)s: %(message)s"
    logging.basicConfig(format=__fmt, level=logging.INFO, datefmt="%H:%M:%S")

    __type = ""
    __time_started: datetime.time
    __minutes: int
    __thread: threading.Timer = None

    def __exec_thread(self, minutes: int):
        self.__time_started = datetime.now().time()
        self.__minutes = minutes
        self.__thread = threading.Timer(float(minutes * 60), tools.run_term_command, [self.__cmd.format(self.__type)])
        self.__thread.start()

    def __cancel_thread(self):
        if self.is_scheduled():
            self.__thread.cancel()
            self.__thread.join()
            logging.info("Schedule canceled.")
            return 'Shutdown canceled.'
        logging.info("Nothing to cancel.")
        return 'Nothing scheduled.'

    def schedule_shutdown(self, minutes: int):
        logging.info("Shutdown scheduled in {} minutes.".format(minutes))
        self.__type = tools.shutdown_types[self.__os]['shutdown']
        self.__exec_thread(minutes)

    def schedule_sleep(self, minutes: int):
        logging.info("Sleep scheduled in {} minutes.".format(minutes))
        self.__type = tools.shutdown_types[self.__os]['sleep']
        self.__exec_thread(minutes)

    def schedule_hibernate(self, minutes: int):
        logging.info("Hibernate scheduled in {} minutes.".format(minutes))
        self.__type = tools.shutdown_types[self.__os]['hibernate']
        self.__exec_thread(minutes)

    def schedule_cancel(self):
        return self.__cancel_thread()

    def is_scheduled(self):
        return self.__thread is not None and self.__thread.is_alive()

    def get_status(self):
        if self.is_scheduled():
            return "{} at {}".format(self.__type.capitalize(),
                                     (datetime.strptime(str(self.__time_started), '%H:%M:%S.%f') +
                                      timedelta(minutes=self.__minutes)).time())
        else:
            return "Nothing scheduled."
