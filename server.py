import paho.mqtt.client as mqtt #import the client1
import time
import json


MQTT_HOST = "mqtt.eclipse.org"
MQTT_PORT = 1883
MQTT_TOPIC = "MQTTMult_SnakeReceived"

############
def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))

    print(" * message received: " ,msg)

    parsed_json = (json.loads(msg))
    print(json.dumps(parsed_json, indent=4, sort_keys=True))
    

########################################

def main():
    mqttc = mqtt.Client("P189506")

    # Callback Function
    mqttc.on_message = on_message

    print(" * Conectando ao broker: ", MQTT_HOST, ":", MQTT_PORT)
    mqttc.connect(MQTT_HOST, MQTT_PORT)
    mqttc.loop_start()

    print(" * Se inscrevendo no tópico: ", MQTT_TOPIC)
    mqttc.subscribe(MQTT_TOPIC)

    print(" * Publicando no tópico: ", MQTT_TOPIC)
    mqttc.publish(MQTT_TOPIC,"TESTE")

    while True:
        time.sleep(1) # wait

    mqttc.loop_stop() #stop the loop



if __name__ == "__main__":
    main()
