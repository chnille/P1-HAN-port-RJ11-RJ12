#!/usr/bin/python3

import serial, array
import time
import paho.mqtt.client as mqtt
import re

broker_address="192.168.xxx.xxx"
broker_port=1883
client = mqtt.Client()
#client.on_connect = on_connect
client.username_pw_set(username="user", password="password")
client.connect(broker_address,broker_port, 60)

ser = serial.Serial("/dev/ttyUSB1", 115200, timeout=1, parity=serial.PARITY_NONE)

#start_time = datetime.now()
#time_delta = datetime.now()-start_time
a = array.array('B', [])


while(True):
   b = str(ser.readline())
   #print(b)
   if "1-0:1.7.0" in str(b):
      data = re.split('\(|\*', b)
      client.publish("hass/elmatare/totalnow",str(data[1]),0,True) #publish
      #print(data[1])
   if "1-0:21.7.0" in str(b):
      data = re.split('\(|\*', b)
      client.publish("hass/elmatare/p1",str(data[1]),0,True) #publish
      #print(data[1])
   if "1-0:41.7.0" in str(b):
      data = re.split('\(|\*', b)
      client.publish("hass/elmatare/p2",str(data[1]),0,True) #publish
      #print(data[1])
   if "1-0:61.7.0" in str(b):
      data = re.split('\(|\*', b)
      client.publish("hass/elmatare/p3",str(data[1]),0,True) #publish
   if "1-0:1.8.0" in str(b):
      data = re.split('\(|\*', b)
      client.publish("hass/elmatare/counter",str(data[1]),0,True) #publish
      #print(data[1])
   #if "1-0:71.7.0(" in str(b):
   #   time.sleep(5)
   time.sleep(0.1)

ser.close()
