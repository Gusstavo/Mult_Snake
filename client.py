import paho.mqtt.client as mqtt #import the client1
import time
import json

MQTT_HOST = "mqtt.eclipse.org" 
MQTT_PORT = 1883
MQTT_TOPIC = "MQTTMult_SnakeReceived"
MQTT_MSG=json.dumps({"nick": "Player_1","x":  "10","y": "25"})


def on_publish(client, userdata, mid):
    print(" * Mensagem publicada...")

def on_connect(client, userdata, flags, rc):
    client.subscribe(MQTT_TOPIC)
    client.publish(MQTT_TOPIC, MQTT_MSG)

def on_message(client, userdata, msg):
    print(msg.topic)
    print(msg.payload) # <- do you mean this payload = {...} ?
    payload = json.loads(msg.payload) # you can use json.loads to convert string to json
    print(payload['sepalWidth']) # then you can check the value
    client.disconnect() # Got message then disconnect

mqttc = mqtt.Client("P1944210")

# Register publish callback function
mqttc.on_publish = on_publish
mqttc.on_connect = on_connect
mqttc.on_message = on_message

# Connect with MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT)

# Loop forever
mqttc.loop_start()

while True:
    time.sleep(2)
    mqttc.publish(MQTT_TOPIC, MQTT_MSG)
