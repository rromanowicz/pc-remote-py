from tools import tools


class MediaKeys:
    __cmd = tools.commands['windows']['mediaKeys']['cmd']

    def next_track(self):
        tools.run_term_command(self.__cmd.format("0xB0"))

    def prev_track(self):
        tools.run_term_command(self.__cmd.format("0xB1"))

    def play_pause(self):
        tools.run_term_command(self.__cmd.format("0xB3"))

    def right(self):
        tools.run_term_command(self.__cmd.format("0x27"))

    def left(self):
        tools.run_term_command(self.__cmd.format("0x25"))

    def up(self):
        tools.run_term_command(self.__cmd.format("0x26"))

    def down(self):
        tools.run_term_command(self.__cmd.format("0x28"))

    def spacebar(self):
        tools.run_term_command(self.__cmd.format("0x20"))

    def esc(self):
        tools.run_term_command(self.__cmd.format("0x1B"))

    def enter(self):
        tools.run_term_command(self.__cmd.format("0xB0"))
