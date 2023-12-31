# Halloweenicorn 💀🎃🧛‍♂️👻
Pimoroni Cosmic Unicorn Halloween themed, PIR enabled scarer.


https://github.com/mrglennjones/Halloweenicorn/assets/78789353/e368e2c6-0e17-4971-a348-8134fbac23ca


### What is it?
A micropython script for Pimoroni's Cosmic Unicorn that displays a randomly picked face anim from PNG spritesheet and play a sound (evil laugh) upon detection from the PIR sensor 

![facesxl](https://github.com/mrglennjones/Halloweenicorn/assets/78789353/cbd89b40-ef9f-43ce-b80e-cce592b40190)


### Dependencies

* You need to download chunk.py and wave.py from https://github.com/joeky888/awesome-micropython-lib/tree/master/Audio into the lib folder to read WAV files
* You need Version 1.20.4 of the Micropython firmware for the Raspberry Pi Pico W (Requires PNG support). Check https://github.com/pimoroni/pimoroni-pico/releases for Firmware updates
* wave_player.py taken from rafew's weatherclock project [https://github.com/raphv/galactic-weather-clock/](https://github.com/raphv/galactic-weather-clock/blob/main/wave_player.py)

### Description of files
* pir_pngandsound.py main micropython script
* [laughs] Laughs directory with the 4 wav files (You can change these to your own, make sure they are mono, 16-bit, 22050Hz)
* faces.png This the PNG spritesheet of four faces 32x32 pixels per frame

### Hardware requirements

* Pimoroni Cosmic Unicorn - 32x32 led https://shop.pimoroni.com/products/space-unicorns?variant=40842626596947

* PIR Sensor - any 3.3v one should be good https://thepihut.com/products/pir-motion-sensor-module

* The PIR is connected via JST-SH Cable (Qwiic, STEMMA QT, QW/ST) – Male to DuPont socket header https://shop.pimoroni.com/products/jst-sh-cable-qwiic-stemma-qt-compatible?variant=40409136332883
Pinout

    Black - GND
    Red - V+ (3.3V for Qwiic, 3-5V for STEMMA QT)
    Yellow - SCL
The blue cable is unused

![pir1](https://github.com/mrglennjones/Halloweenicorn/assets/78789353/a82b49ef-0f89-4cda-bd03-7e1e2479b833) | ![pir2](https://github.com/mrglennjones/Halloweenicorn/assets/78789353/0c714bd9-9862-4ca1-9e4b-a80628397e5e)


