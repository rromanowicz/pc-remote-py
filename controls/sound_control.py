from tools import tools


class Sound:
    def __init__(self, os: str):
        self.__os = os.lower()
        self.__cmd = tools.commands[self.__os]['sound']['cmd']

    def increase_volume(self, val: int):
        tools.run_term_command(self.__cmd.format(self.__get_val(val), tools.sound_control[self.__os]['incr']))

    def decrease_volume(self, val: int):
        tools.run_term_command(self.__cmd.format(self.__get_val(val), tools.sound_control[self.__os]['decr']))

    def set_volume(self, val: int):
        tools.run_term_command(self.__cmd.format(self.__get_val(val), tools.sound_control[self.__os]['set']))

    def mute(self, val: int):
        tools.run_term_command(self.__cmd.format('', tools.sound_control[self.__os]['mute']))

    def __get_val(self, val: int) -> str:
        return str(65535 // 100 * val) if self.__os == 'windows' else str(val)
