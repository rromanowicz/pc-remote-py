import os


class MediaKeys:
    __cmd = "xdotool key "

    def __run_cmd(self, key: str):
        stream = os.popen(self.__cmd + key)
        return stream.read()

    def next_track(self):
        self.__run_cmd("XF86AudioNext")

    def prev_track(self):
        self.__run_cmd("XF86AudioPrev")

    def play_pause(self):
        self.__run_cmd("XF86AudioPlay")

    def right(self):
        self.__run_cmd("Right")

    def left(self):
        self.__run_cmd("Left")

    def up(self):
        self.__run_cmd("Up")

    def down(self):
        self.__run_cmd("Down")

    def spacebar(self):
        self.__run_cmd("space")

    def esc(self):
        self.__run_cmd("Escape")

    def enter(self):
        self.__run_cmd("KP_Enter")
