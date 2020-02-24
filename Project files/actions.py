from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions import Action
# from rasa_core_sdk import Action
# from rasa_core_sdk.events import SlotSet

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
#from rasa_core_sdk import Tracker
#from WeatherAPIXU.client

class ActionWeather(Action):
    def name(self):
        return 'action_weather'

    def run(self, dispatcher, tracker, domain):
        from apixu.client import ApixuClient
        api_key = 'f7d8a7805fb74e22bff182510192804'  # your apixu key
        client = ApixuClient(api_key)

        loc = tracker.get_slot('location')
        #current = client.getcurrent(q=loc)
        current = client.current(q=loc)

        country = current['location']['country']
        city = current['location']['name']
        condition = current['current']['condition']['text']
        temperature_c = current['current']['temp_c']
        humidity = current['current']['humidity']
        wind_mph = current['current']['wind_mph']

        response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(
            condition, city, temperature_c, humidity, wind_mph)

        dispatcher.utter_message(response)
        #dispatcher.utter_message('test test')
        return [SlotSet('location', loc)]
        #return []

class ActionShowMeeting(Action):
    def name(self):
        return 'action_show_meeting'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Here is the meeting information!')
        return []

class ActionScheduleMeeting(Action):
    def name(self):
        return 'action_schedule_meeting'

    def run(self, dispatcher, tracker, domain):
        print('scheduling meeting is completed! ')
        pass


