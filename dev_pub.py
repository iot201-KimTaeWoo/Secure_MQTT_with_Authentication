import sys
import ssl
import paho.mqtt.client as mqtt
server = "54.160.217.20" 

client = mqtt.Client()
client.username_pw_set('tae', 'tae')
client.connect(server, 1883, 60)

if len(sys.argv) <= 1:
    print("Usage : "+sys.argv[0]+" message")
    exit()
else:
    client.publish("iot3/tae/evt/status/fmt/json", str(sys.argv[1]))
