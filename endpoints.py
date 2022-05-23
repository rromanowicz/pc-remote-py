from flask import request, Response
import controllers

from __main__ import app

sound = controllers.get_sound_controller()
shutdown = controllers.get_shutdown_controller()
media = controllers.get_media_controller()


@app.route('/vol', methods=['GET'])
def volume():
    key = str(request.args.get('key'))
    val = int(request.args.get('val'))

    match key:
        case 'increase':
            sound.increase_volume(val)
        case 'decrease':
            sound.decrease_volume(val)
        case 'set':
            sound.set_volume(val)
        case 'mute':
            sound.mute()
        case _:
            return Response('Invalid input.', status=200, mimetype='application/json')

    return Response(None, status=200, mimetype='application/json')


@app.route('/mediaKey', methods=['GET'])
def media_key():
    key = str(request.args.get('key'))

    match key:
        case "nextTrack":
            media.next_track()
        case "prevTrack":
            media.prev_track()
        case "playPause":
            media.play_pause()
        case "keyEscape":
            media.esc()
        case "keySpacebar":
            media.spacebar()
        case "keyReturn":
            media.enter()
        case "arrowUp":
            media.up()
        case "arrowDown":
            media.down()
        case "arrowLeft":
            media.left()
        case "arrowRight":
            media.right()
        case _:
            return Response('Invalid input.', status=200, mimetype='application/json')

    return Response(None, status=200, mimetype='application/json')


@app.route('/shut', methods=['GET'])
def shut():
    key = str(request.args.get('key'))
    schedule_type = str(request.args.get('type'))
    val = int(request.args.get('val'))

    match key:
        case 'confirm':
            if not shutdown.is_scheduled():
                match schedule_type:
                    case 'shut':
                        shutdown.schedule_shutdown(val)
                    case 'hibernate':
                        shutdown.schedule_hibernate(val)
                    case 'sleep':
                        shutdown.schedule_sleep(val)
        case 'cancel':
            shutdown.schedule_cancel()
            return "Shutdown canceled."
        case 'check':
            return shutdown.get_status()

    return shutdown.get_status()
