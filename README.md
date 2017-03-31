# CWPacman1d

A project that I see in the Game Science Center (http://www.gamesciencecenter.de/en/) at Berlin. So I decided do program my own one. 

## Requirements
* Raspberry Pi 2 with Raspbian
* WS2812 Led-Stripe
* External power supply

## Raspberry Pining
* Led-Stripe ground to Raspberry-Pin 9
* Led-Stripe Data to Raspberry-Pin 12
* Led-Stripe Plus 5V not connected (External power supply)

## Raspberry Pi installations
Neopixel Lib

```
git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons
cd python
sudo python setup.py install
```






