# P1-HAN-port-RJ11-RJ12
Script to read data from P1 HAN and post on mqtt broker. Home Assistant subscribe on mqtt information
Used with Sagencom T211 from Ellevio
Cable FTDI FR232R USB TTL 5 V for RJ11/RJ12
https://www.amazon.se/Domoticz-Raspberry-FR232R-Kaifa-Kamstrup/dp/B07JGKJ6SM/ref=sr_1_2?crid=2DV0WUX4EYPMY&keywords=kamstrup+162+rj11&qid=1642949662&sprefix=kamstrup+162+rj11%2Caps%2C64&sr=8-2

Add hanporten.service to /lib/systemd/system/
Edit hanporten.py with your user/passw for the mqtt broker. Change mqtt topic according to your setup.
place python scrip hanporten.py in /usr/local/bin/
Activate service with 
sudo systemctl daemon-reload
sudo systemctl enable hanporten.service

Home Assistant configuration.yaml file.

sensor:
  - platform: mqtt
    name: EnergyNow
    state_topic: "hass/elmatare/totalnow"
    unit_of_measurement: 'Kw'
  - platform: mqtt
    name: EnergyP1
    state_topic: "hass/elmatare/p1"
    unit_of_measurement: 'kw'
  - platform: mqtt
    name: EnergyP2
    state_topic: "hass/elmatare/p2"
    unit_of_measurement: 'kw'
  - platform: mqtt
    name: EnergyP3
    state_topic: "hass/elmatare/p3"
    unit_of_measurement: 'kw'
  - platform: mqtt
    name: ElTotal
    state_topic: "hass/elmatare/counter"
    unit_of_measurement: 'kwh'

