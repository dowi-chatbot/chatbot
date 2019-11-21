# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union, Optional
#  
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, ReminderScheduled 
from rasa_sdk.executor import ActionExecutor, CollectingDispatcher
from rasa_sdk.forms import FormAction
from datetime import datetime, timedelta
import random
import requests
import json

class ActionGetName(Action):
	def name(self) -> Text:
		return "action_get_name"

	def run(self, dispatcher:CollectingDispatcher, tracker: Tracker, domain):

		return [SlotSet("name", "Albert")]

class ActionReminder(Action):
	def name(self) -> Text:
		return "action_reminder"

	def run(self, dispatcher, tracker, domain):
		return [ReminderScheduled("action_test", datetime.now()+timedelta(seconds=20), kill_on_user_message=False)]


class ActionReminder(Action):
	def name(self) -> Text:
		return "action_test"

	def run(self, dispatcher,tracker,domain):
		dispatcher.utter_message("Action test programmée")
		return [SlotSet("name", "Gérard")]

class InitializationForm(FormAction):
	def name(self) -> Text:
		return "initialization_form"

	@staticmethod
	def required_slots(tracker: Tracker):
		return ["name", "age", "pathologie", "type_intervention", "date"]

	def submit(self, dispatcher,tracker:Tracker, domain: Dict[Text,Any]):
		dispatcher.utter_message("Top ! J'ai tout ce qu'il me faut.")
		return[]

class ActionPersoHello(Action):
	def name(self) -> Text:
		return "action_PersoHello"

	def run(self, dispatcher:CollectingDispatcher, tracker:Tracker, domain):
		
		name = tracker.get_slot("name")
		monR = ""
		if name == None:
			maListe = ["Hey ! Comment vas tu ?","Salut, tu vas bien ?","Tout va bien pour toi ?"]
			monR = maListe[random.randint(0,2)]
		else:
			maListe = ["Hey "+name+" ! Comment vas tu ?","Salut "+name+", tu vas bien ?","De retour "+name+"  ! Tout va bien pour toi ?"]
			monR = maListe[random.randint(0,2)]
		dispatcher.utter_message(monR)
		
		return[] 


class ActionReminder(Action):
	def name(self) -> Text:
		return "action_reminder_pre"

	def run(self, dispatcher, tracker, domain):
		date = datetime.strptime(tracker.get_slot("date"),'%d/%m/%y')
		eventJ_1 = date - timedelta(days=1)
		eventJ_2 = date - timedelta(days=2)
		dispatcher.utter_message("Vous allez recevoir des messages le "+eventJ_2.strftime("%d/%m/%y")+" et le "+eventJ_1.strftime("%d/%m/%y")+" pour vous aider à vous préparer juste avant votre hospitalisation :)")
		return [ReminderScheduled("action_J_1", datetime.now()+timedelta(seconds=20), kill_on_user_message=False),
				ReminderScheduled("action_J_2", datetime.now()+timedelta(seconds=40), kill_on_user_message=False)]

class ActionReminderJ_1(Action):
	def name(self) -> Text:
		return "action_J_1"

	def run(self, dispatcher,tracker,domain):
		dispatcher.utter_message("J-2 avant ton opération ! Il faut que tu arretes de consommer d'anti-inflammatoires")
		return []

class ActionReminderJ_2(Action):
	def name(self) -> Text:
		return "action_J_2"

	def run(self, dispatcher,tracker,domain):
		dispatcher.utter_message("J-1 avant ton opération ! Voici les ...")
		return []

class ActionBlagues(Action):
	def name(self) -> Text:
		return "action_blagues"

	def run(self, dispatcher:CollectingDispatcher, tracker:Tracker, domain):
		
		r = requests.get("https://www.chucknorrisfacts.fr/api/get?data=tri:alea;nb:1")
		r = r.text.replace('[','').replace(']','')
		rj = json.loads(r)
		dispatcher.utter_message(rj["fact"])
		return[] 

class ActionConseils(Action):
	def name(self) -> Text:
		return "action_conseils"

	def run(self, dispatcher:CollectingDispatcher, tracker:Tracker, domain):
		
		
		db = open('data/db.json')
		db_str = db.read()
		monJ = json.loads(db_str)
		mesC = []
		for var in monJ["Conseils"]:
		    if var["time"] in (0,2):
		        mesC.append(var["text"])
		monUtt = mesC[random.randint(0,len(mesC)-1)]
		dispatcher.utter_message(monUtt)
		return[] 



class ActionPreparation(Action):
	def name(self) -> Text:
		return "action_preparation"

	def run(self, dispatcher:CollectingDispatcher, tracker:Tracker, domain):
		
		
		db = open('data/db.json')
		db_str = db.read()
		monJ = json.loads(db_str)
		mesC = []
		for var in monJ["Preparation"]:
		    mesC.append(var["text"])
		monUtt = mesC[random.randint(0,len(mesC)-1)]
		dispatcher.utter_message(monUtt)
		return[] 


class ActionStresse(Action):
	def name(self) -> Text:
		return "action_stresse"

	def run(self, dispatcher:CollectingDispatcher, tracker:Tracker, domain):
		
		
		db = open('data/db.json')
		db_str = db.read()
		monJ = json.loads(db_str)
		mesC = []
		for var in monJ["Stresse"]:
		    mesC.append(var["text"])
		monUtt = mesC[random.randint(0,len(mesC)-1)]
		dispatcher.utter_message(monUtt)
		return[] 

class ActionDefineTimer(Action):
	def name(self) -> Text:
		return "action_timer"

	def run(self, dispatcher:CollectingDispatcher,tracker:Tracker,domain):
		nbr_j_avant_ope = datetime.strptime(tracker.get_slot("date"),'%d/%m/%y') - datetime(datetime.now().year, datetime.now().month, datetime.now().day)
		return[SlotSet("timer",-nbr_j_avant_ope.days)]

class ActionChangeDay(Action):
	def name(self) -> Text:
		return "action_change_day"

	def run(self, dispatcher:CollectingDispatcher,tracker:Tracker,domain):
		jour = tracker.get_slot("timer") + 1
		dispatcher.utter_message("Tu as changé de jour, nous sommes maintenant le jour "+str(jour)+" ! :)")
		return[SlotSet("timer",jour)]



















