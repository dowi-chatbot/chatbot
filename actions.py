# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union, Optional
  
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, ReminderScheduled 
from rasa_sdk.executor import ActionExecutor, CollectingDispatcher
from rasa_sdk.forms import FormAction
from datetime import datetime, timedelta
import random
import requests
import json

import smtplib
from email.mime.text import MIMEText

import http.client

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


class ActionFindMovie(Action):
	def name(self) -> Text:
		return "action_find_movie"

	def run(self, dispatcher:CollectingDispatcher, tracker: Tracker, domain):
		conn = http.client.HTTPSConnection("api.themoviedb.org")

		date_gte = datetime.now() - timedelta(days=21)
		date_lte_string = datetime.now().strftime("%Y-%m-%d")
		date_gte_string = date_gte.strftime("%Y-%m-%d")

		url = "/3/discover/movie?primary_release_date.lte=" + date_lte_string + "&primary_release_date.gte=" + date_gte_string + "&page=1&include_video=false&include_adult=false&sort_by=popularity.desc&language=fr-FR&api_key=cf074dea94828cf86b340bef21e15941"

		payload = "{}"

		try:
			conn.request("GET", url, payload)
			res = conn.getresponse()
			data = res.read()
			data = json.loads(data)
			chosen = [_ for _ in data['results'] if _['vote_average']>4]
			rand = random.randint(0,len(chosen))
			chosen = chosen[rand]
			text = 'Je te conseille de regarder '+chosen['title']+'. Ce film a été noté '+str(chosen['vote_average'])+' et il est actuellement au cinéma :) !'
			dispatcher.utter_message(text)
		except: 
			dispatcher.utter_message("Désolé, j'ai eu un problème internet, vérifie ta connexion et demande moi de nouveau 😊")
		try:
			image = 'https://image.tmdb.org/t/p/w200/'+chosen['backdrop_path']
			dispatcher.utter_image_url(image)
		except:
			pass
		return []

class InitializationForm(FormAction):
	def name(self) -> Text:
		return "initialization_form"

	@staticmethod
	def required_slots(tracker: Tracker):
		return ["name", "age", "pathologie", "type_intervention", "date", "mail"]

	def submit(self, dispatcher,tracker:Tracker, domain: Dict[Text,Any]):
		nbr_j_avant_ope = datetime.strptime(tracker.get_slot("date"),'%d/%m/%y') - datetime(datetime.now().year, datetime.now().month, datetime.now().day)
		dispatcher.utter_message("Top ! J'ai tout ce qu'il me faut.")
		return[SlotSet("timer",-nbr_j_avant_ope.days)]

	def slot_mappings(self):
		return {
			"mail": [
				self.from_text()
				]}

class CheckUpForm(FormAction):
	def name(self) -> Text:
		return "check_up_form"

	@staticmethod
	def required_slots(tracker: Tracker):
		return ["saignement", "alveolite", "fil"]

	def submit(self, dispatcher,tracker:Tracker, domain: Dict[Text,Any]):
		dispatcher.utter_message('ok')
		mail = tracker.get_slot("mail")
		pict = "https://media.licdn.com/dms/image/C4D0BAQFrT0693_pBGg/company-logo_400_400/0?e=1583366400&v=beta&t=XK0XWV_Y4wKwulLx27XFckq-sf2lSICjHn2GRXdoe70&fbclid=IwAR1WDvTatYNNXHD0mcKRxuysuuzQ2PH96KZuT2lZEBt53Ufx6ILzvNMR5co"
		html = """
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  		<title>html title</title>
 		<div>
 		<h1 align="center"> Rapport de """+str(tracker.get_slot("name"))+""" du """+datetime.now().strftime("%d/%m/%Y")+"""</h1>

		<table align= "center" border="1">
		<tr><th>Parametres</th><th>Reponses</th></tr>
		<tr><th>Saignements</th><th>"""+str(tracker.get_slot("saignement"))+"""</th></tr>
		<tr><th>Alveolite</th><th>"""+str(tracker.get_slot("alveolite"))+"""</th></tr>
		<tr><th>Fil</th><th>"""+str(tracker.get_slot("fil"))+"""</th></tr>
		</table>
		<br>
		<div align="center">
		<img src="https://media.licdn.com/dms/image/C4D0BAQFrT0693_pBGg/company-logo_400_400/0?e=1583366400&v=beta&t=XK0XWV_Y4wKwulLx27XFckq-sf2lSICjHn2GRXdoe70&fbclid=IwAR1WDvTatYNNXHD0mcKRxuysuuzQ2PH96KZuT2lZEBt53Ufx6ILzvNMR5co"  width="150" height="150" > 
		</div>
		<br>
		<p align="center">Vous pouvez contacter le patient sur son numéro personnel.</p>
		</div>
		"""
		message = MIMEText(html,'html')
		message['Subject'] = 'Checkup Dowi '
		message['From'] = 'dowidowi930@gmail.com'
		message['To'] = mail

		try:
			server = smtplib.SMTP('smtp.gmail.com:587')
			server.starttls()
			server.login('dowidowi930@gmail.com','&dowidowi92!')
			server.send_message(message)
			server.quit()
			dispatcher.utter_message("Check up terminé !")
		
		except: 
			dispatcher.utter_message("Checkup terminé ! L'adresse du médecin n'étant pas renseigné ou non valide, nous n'avons pas envoyé de rapport mail.")
		
		
		return[SlotSet("saignement", None),SlotSet("alveolite", None), SlotSet("fil", None)]
	
	def slot_mappings(self):
		return {
			"saignement": [
				self.from_text()
				],
			"alveolite": [
				self.from_text()
				],
			"fil": [
				self.from_text()
				]
			}
	


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

class ActionReminderPre(Action):
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


class ActionChangeDay(Action):
	def name(self) -> Text:
		return "action_change_day"

	def run(self, dispatcher:CollectingDispatcher,tracker:Tracker,domain):
		jour = tracker.get_slot("timer") + 1
		dispatcher.utter_message("Tu as changé de jour, nous sommes maintenant le jour "+str(jour)+" ! :)")

		return[SlotSet("timer",jour)]

	def afaire(self):
		return []