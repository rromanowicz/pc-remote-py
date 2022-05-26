from tools import tools


class MediaKeys:
    __cmd = tools.commands['linux']['mediaKeys']['cmd']

    def next_track(self):
        tools.run_term_command(self.__cmd.format("XF86AudioNext"))

    def prev_track(self):
        tools.run_term_command(self.__cmd.format("XF86AudioPrev"))

    def play_pause(self):
        tools.run_term_command(self.__cmd.format("XF86AudioPlay"))

    def right(self):
        tools.run_term_command(self.__cmd.format("Right"))

    def left(self):
        tools.run_term_command(self.__cmd.format("Left"))

    def up(self):
        tools.run_term_command(self.__cmd.format("Up"))

    def down(self):
        tools.run_term_command(self.__cmd.format("Down"))

    def spacebar(self):
        tools.run_term_command(self.__cmd.format("space"))

    def esc(self):
        tools.run_term_command(self.__cmd.format("Escape"))

    def enter(self):
        tools.run_term_command(self.__cmd.format("KP_Enter"))
