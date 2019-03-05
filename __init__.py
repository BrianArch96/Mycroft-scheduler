# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
from mycroft.util.parse import extract_datetime
import json 
import re
from websocket import create_connection

URL_TEMPLATE = "{scheme}://{host}:{port}{path}"
NEXT_LESSON = "What is my next lesson"
UPCOMING_APPOINTMENT = "Upcoming appointment"
DUE_ASSIGNMENT = " next assignment due"

def send_request(msg, host = "localhost", port=8181, path="/core", scheme="ws"):
    payload = json.dumps({
        "type": "recognizer_loop:utterance",
        "context": "",
        "data": {
            "utterances": [msg]
        }
    })
    url = URL_TEMPLATE.format(scheme=scheme, host=host, port=str(port), path=path)
    ws = create_connection(url)
    ws.send(payload)
    ws.close()

class SchedulerSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(SchedulerSkill, self).__init__(name="SchedulerSkill")
        print("Hello world")
    
    @intent_handler(IntentBuilder("Scheduler").require("Scheduler"))
    def schedule_handler(self, message):
        send_request(NEXT_LESSON)
        send_request(DUE_ASSIGNMENT)
        send_request(UPCOMING_APPOINTMENT)

def create_skill():
    return SchedulerSkill()
