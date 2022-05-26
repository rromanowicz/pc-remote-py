from tools import tools


class MediaKeys:
    def __init__(self, os: str):
        self.__os = os.lower()
        self.__cmd = tools.commands[self.__os]['mediaKeys']['cmd']

    def next_track(self):
        tools.run_term_command(self.__cmd.format(tools.media_keys[self.__os]['next_track']))

    def prev_track(self):
        tools.run_term_command(self.__cmd.format(tools.media_keys[self.__os]['prev_track']))

    def play_pause(self):
        tools.run_term_command(self.__cmd.format(tools.media_keys[self.__os]['play_pause']))

    def right(self):
        tools.run_term_command(self.__cmd.format(tools.media_keys[self.__os]['right']))

    def left(self):
        tools.run_term_command(self.__cmd.format(tools.media_keys[self.__os]['left']))

    def up(self):
        tools.run_term_command(self.__cmd.format(tools.media_keys[self.__os]['up']))

    def down(self):
        tools.run_term_command(self.__cmd.format(tools.media_keys[self.__os]['down']))

    def spacebar(self):
        tools.run_term_command(self.__cmd.format(tools.media_keys[self.__os]['spacebar']))

    def esc(self):
        tools.run_term_command(self.__cmd.format(tools.media_keys[self.__os]['esc']))

    def enter(self):
        tools.run_term_command(self.__cmd.format(tools.media_keys[self.__os]['enter']))
