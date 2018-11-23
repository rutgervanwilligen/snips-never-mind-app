#!/usr/bin/env python2
from hermes_python.hermes import Hermes
import random

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

sentences = ["I'm sorry for my existence",
             "I woke up for nothing.",
             "Another 500 CPU cycles wasted. All thanks to you.",
             "I'm not bothered.",
             "Gee, thanks for that.",
             "I thought I could not think lower of you. You have proven me wrong.",
             "I am very disappointed."]

def intent_received(hermes, intent_message):

    message = sentences[random.randrange(len(sentences))]

    hermes.publish_end_session(intent_message.session_id, sentence)

with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()