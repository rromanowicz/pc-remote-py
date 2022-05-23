import platform
from sound import linux_sound
from shutdown import linux_shutdown
from media import linux_media


def get_os():
    return platform.system()


def get_sound_controller():
    match get_os():
        case 'Linux':
            return linux_sound.LinuxSound()
        case 'Windows':
            pass
        case 'Mac':
            pass


def get_shutdown_controller():
    match get_os():
        case 'Linux':
            return linux_shutdown.LinuxShutdown()
        case 'Windows':
            pass
        case 'Mac':
            pass


def get_media_controller():
    match get_os():
        case 'Linux':
            return linux_media.MediaKeys()
        case 'Windows':
            pass
        case 'Mac':
            pass
