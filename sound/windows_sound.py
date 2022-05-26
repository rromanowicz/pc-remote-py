from tools import tools


class WindowsSound:
    __cmd = tools.commands['windows']['sound']['cmd']

    def increase_volume(self, val: int):
        tools.run_term_command(self.__cmd.format('changesysvolume', str(65535 // 100 * val)))

    def decrease_volume(self, val: int):
        tools.run_term_command(self.__cmd.format('changesysvolume -', str(65535 // 100 * val)))

    def set_volume(self, val: int):
        tools.run_term_command(self.__cmd.format('setsysvolume', str(65535 // 100 * val)))

    def mute(self):
        tools.run_term_command(self.__cmd.format('mutesysvolume', "2"))
