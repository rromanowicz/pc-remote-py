import os


class WindowsSound:
    __path_to_file = "C:\\nircmd.exe"
    __cmd = "{} {} {}"

    def __run_cmd(self, action: str, val: int):
        stream = os.popen(self.__cmd.format(self.__path_to_file, action, str(val)))
        return stream.read()

    def increase_volume(self, val: int):
        self.__run_cmd('changesysvolume', 65535/100*val)

    def decrease_volume(self, val: int):
        self.__run_cmd('changesysvolume -', 65535/100*val)

    def set_volume(self, val: int):
        self.__run_cmd('setsysvolume', 65535/100*val)

    def mute(self):
        self.__run_cmd('mutesysvolume', 2)

