import os

commands = {
    'linux': {
        'sound': {
            'cmd': "pactl -- set-sink-volume {} {}{}%",
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


def run_term_command(cmd: str) -> str:
    stream = os.popen(cmd)
    return stream.read()
