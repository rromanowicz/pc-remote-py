import os

commands = {
    'linux': {
        'sound': {
            'cmd': "pactl -- set-sink-volume $(pactl list sinks | grep -B 1 RUNNING | grep -oP '(?<=#).*') {}{}%",
            'sink': "pactl list sinks | grep -B 1 RUNNING | grep -oP '(?<=#).*'"},
        'mediaKeys': {
            'cmd': "xdotool key {}"},
        'shutdown': {
            'cmd': "systemctl {} -i"}},
    'windows': {
        'sound': {
            'cmd': "C:\\nircmd.exe {} {}"},
        'mediaKeys': {
            'cmd': "C:\\nircmd.exe sendkey {} press"},
        'shutdown': {
            'cmd': "C:\\nircmd.exe {}"}},
    'mac': {
        'sound': {
            'cmd': "osascript -e 'set volume output volume {}'"},
        'mediaKeys': {
            'cmd': "osascript -e 'tell application \"System Events\" to key code {}'"},
        'shutdown': {
            'cmd': "osascript -e 'tell app \"System Events\" to {}'"}}
}

media_keys = {
    'linux': {
        'next_track': "XF86AudioNext",
        'prev_track': "XF86AudioPrev",
        'play_pause': "XF86AudioPlay",
        'right': "Right",
        'left': "Left",
        'up': "Up",
        'down': "Down",
        'spacebar': "space",
        'esc': "Escape",
        'enter': "KP_Enter"
    },
    'windows': {
        'next_track': "0xB0",
        'prev_track': "0xB1",
        'play_pause': "0xB3",
        'right': "0x27",
        'left': "0x25",
        'up': "0x26",
        'down': "0x28",
        'spacebar': "0x20",
        'esc': "0x1B",
        'enter': "0xB0"
    },
    'mac': {
        'next_track': "",
        'prev_track': "",
        'play_pause': "",
        'right': "124",
        'left': "123",
        'up': "126",
        'down': "125",
        'spacebar': "49",
        'esc': "53",
        'enter': "36"
    }
}

shutdown_types = {
    'linux': {
        'shutdown': "poweroff",
        'hibernate': "hibernate",
        'sleep': "suspend"
    },
    'windows': {
        'shutdown': "initshutdown",
        'hibernate': "hibernate",
        'sleep': "standby"
    },
    'mac': {
        'shutdown': "shut down",
        'hibernate': "",
        'sleep': "sleep"
    }
}

sound_control ={
    'linux': {
        'incr': "+",
        'decr': "-",
        'set': "",
        'mute': ""
    },
    'windows': {
        'incr': "changesysvolume",
        'decr': "changesysvolume -",
        'set': "setsysvolume",
        'mute': "mutesysvolume"
    },
    'mac': {
        'incr': "",
        'decr': "",
        'set': "",
        'mute': ""
    }
}


def run_term_command(cmd: str) -> str:
    stream = os.popen(cmd)
    return stream.read()
