# pc-remote-py

Allows simplified control over pc. \
For those who don't want do get out of bed to turn the volume down ;-)

Navigate to directory and run command:
> python main.py



#DEPENDENCIES:
>**1. Requires one of the following apps (connected to the same network):**
>>- [pc-remote-web](https://github.com/rromanowicz/pc-remote-web)
>>- [pc-remote-android](https://github.com/rromanowicz/pc-remote-android)
>>- [pc-remote-ios](https://github.com/rromanowicz/pc-remote-ios)
>>- [pc-remote-garmin](https://github.com/rromanowicz/pc-remote-garmin)
> 
>**2. LINUX Host**
>>- [xdotool](http://manpages.ubuntu.com/manpages/trusty/man1/xdotool.1.html)
>
>**2. WINDOWS Host**
>>- [nircmd.exe](http://www.nirsoft.net/utils/nircmd.html) @C:\ \
    (Running application with admin privileges automatically copies required file.)



#ENDPOINTS:
> - `/vol?key={}&val={}`
>> - key:
>>> - increase
>>> - decrease
>>> - mute
>>> - set
>> - value
>>> - Integer
> 
> - `/mediaKey?key={}`
>> - key:
>>> - nextTrack
>>> - prevTrack
>>> - playPause
>>> - keyEscape
>>> - keySpacebar
>>> - keyReturn
>>> - arrowUp
>>> - arrowDown
>>> - arrowLeft
>>> - arrowRight
> 
> - `/shut=key={}&type={}&val={}`
>> - key:
>>> - confirm
>>> - cancel
>>> - check
>> - type:
>>> - shut
>>> - hibernate
>>> - sleep
>> - val:
>>> - Integer
>
