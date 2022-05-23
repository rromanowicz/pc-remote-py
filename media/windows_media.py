import os


class MediaKeys:
    __path_to_file = "C:\\nircmd.exe"
    __cmd = "{} sendkey {} press"

    def __run_cmd(self, key: str):
        stream = os.popen(self.__cmd.format(self.__path_to_file, key))
        return stream.read()

    def next_track(self):
        self.__run_cmd("0xB0")

    def prev_track(self):
        self.__run_cmd("0xB1")

    def play_pause(self):
        self.__run_cmd("0xB3")

    def right(self):
        self.__run_cmd("0x27")

    def left(self):
        self.__run_cmd("0x25")

    def up(self):
        self.__run_cmd("0x26")

    def down(self):
        self.__run_cmd("0x28")

    def spacebar(self):
        self.__run_cmd("0x20")

    def esc(self):
        self.__run_cmd("0x1B")

    def enter(self):
        self.__run_cmd("0x0D")



if __name__ == '__main__':
    media = MediaKeys()
    media.next_track()
