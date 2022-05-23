import platform
from sound import linux_sound, windows_sound
from shutdown import linux_shutdown, windows_shutdown
from media import linux_media, windows_media


def get_os():
    return platform.system()


def get_sound_controller():
    match get_os():
        case 'Linux':
            return linux_sound.LinuxSound()
        case 'Windows':
            return windows_sound.WindowsSound()
        case 'Mac':
            pass


def get_shutdown_controller():
    match get_os():
        case 'Linux':
            return linux_shutdown.LinuxShutdown()
        case 'Windows':
            return windows_shutdown.WindowsShutdown()
        case 'Mac':
            pass


def get_media_controller():
    match get_os():
        case 'Linux':
            return linux_media.MediaKeys()
        case 'Windows':
            return windows_media.MediaKeys()
        case 'Mac':
            pass
