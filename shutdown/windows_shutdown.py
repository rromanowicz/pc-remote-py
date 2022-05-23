import logging
import os
import threading
from datetime import datetime, timedelta


class WindowsShutdown:
    __fmt = "%(asctime)s: %(message)s"
    logging.basicConfig(format=__fmt, level=logging.INFO, datefmt="%H:%M:%S")

    __type = ""
    __time_started: datetime.time
    __minutes: int
    __thread: threading.Timer = None

    def __run_cmd(self, schedule_type):
        stream = os.popen("C:\\nircmd.exe {}".format(schedule_type))
        return stream.read()

    def __exec_thread(self, minutes: int):
        self.__time_started = datetime.now().time()
        self.__minutes = minutes
        self.__thread = threading.Timer(float(minutes * 60), self.__run_cmd, [self.__type])
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
        self.__type = 'initshutdown'
        self.__exec_thread(minutes)

    def schedule_sleep(self, minutes: int):
        logging.info("Sleep scheduled in {} minutes.".format(minutes))
        self.__type = 'standby'
        self.__exec_thread(minutes)

    def schedule_hibernate(self, minutes: int):
        logging.info("Hibernate scheduled in {} minutes.".format(minutes))
        self.__type = 'hibernate'
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
