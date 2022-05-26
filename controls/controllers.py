import platform

from controls import media_control, sound_control, shutdown_control


def get_os():
    return platform.system()


def get_controllers():
    os = get_os()
    return sound_control.Sound(os), media_control.MediaKeys(os), shutdown_control.Shutdown(os)
