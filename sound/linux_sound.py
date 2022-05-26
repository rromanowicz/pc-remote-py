from tools import tools


class LinuxSound:
    __cmd = tools.commands['linux']['sound']['cmd']
    __sink = tools.commands['linux']['sound']['sink']

    def increase_volume(self, val: int):
        tools.run_term_command(
            self.__cmd.format(tools.run_term_command(self.__sink).replace('\n', ''), "+", str(val)))

    def decrease_volume(self, val: int):
        tools.run_term_command(
            self.__cmd.format(tools.run_term_command(self.__sink).replace('\n', ''), "-", str(val)))

    def set_volume(self, val: int):
        tools.run_term_command(
            self.__cmd.format(tools.run_term_command(self.__sink).replace('\n', ''), "", str(val)))

    def mute(self):
        self.set_volume(0)
