# Halloweenicorn
Pimoroni Cosmic Unicorn Halloween themed, PIR enabled scarer.

<video src='https://github.com/mrglennjones/Halloweenicorn/blob/main/video_demo2.mp4' width=180/></video>

### What is it?
A micropython script for Pimoroni's Cosmic Unicorn that displays a randomly picked face anim from PNG spritesheet and play a sound (evil laugh) upon detection from the PIR sensor 


### Hardware requirements

* Pimoroni Cosmic Unicorn - 32x32 led https://shop.pimoroni.com/products/space-unicorns?variant=40842626596947

* PIR Sensor - any 3.3v one should be good https://thepihut.com/products/pir-motion-sensor-module

The PIR is connected via JST-SH Cable (Qwiic, STEMMA QT, QW/ST) – Male to DuPont socket header https://shop.pimoroni.com/products/jst-sh-cable-qwiic-stemma-qt-compatible?variant=40409136332883
Pinout

    Black - GND
    Red - V+ (3.3V for Qwiic, 3-5V for STEMMA QT)
    Yellow - SCL


### Dependencies

* You need to download chunk.py and wave.py from https://github.com/joeky888/awesome-micropython-lib/tree/master/Audio into the lib folder to read WAV files
* You need Version 1.20.4 of the Micropython firmware for the Raspberry Pi Pico W (Requires PNG support). Check https://github.com/pimoroni/pimoroni-pico/releases for Firmware updates
* wave_player.py taken from rafew's https://github.com/raphv/galactic-weather-clock/ weatherclock project [https://github.com/raphv/galactic-weather-clock/](https://github.com/raphv/galactic-weather-clock/blob/main/wave_player.py)
### Description of files

[laughs] Laughs directory with the 4 wav files (You can change these to your own m\king sure they are mono, 16-bit, 22050Hz)
