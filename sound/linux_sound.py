import os


def run_cmd(cmd):
    stream = os.popen(cmd)
    return stream.read()


class LinuxSound:
    __cmd = "pactl -- set-sink-volume "
    __sink = "pactl list sinks | grep -B 1 RUNNING | grep -oP '(?<=#).*'"

    def increase_volume(self, val: int):
        run_cmd(self.__cmd + run_cmd(self.__sink).replace('\n', '') + " +" + str(val) + "%")

    def decrease_volume(self, val: int):
        run_cmd(self.__cmd + run_cmd(self.__sink).replace('\n', '') + " -" + str(val) + "%")

    def set_volume(self, val: int):
        run_cmd(self.__cmd + run_cmd(self.__sink).replace('\n', '') + " " + str(val) + "%")

    def mute(self):
        self.set_volume(0)
