import paho.mqtt.client as mqtt
#pip3 install paho-mqtt

payload="Hello:
topic="IOT/test"
client = mqtt.Client()
client.connect('0.0.0.0',1883,60)
(rc,mid)=client.publish(topic,payload);
client.disconnect();
