## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot



## New Story

* firstConversation
    - utter_firstgreet
    - utter_firstConversation
* deny
    - utter_comebacklater

## deny
* deny
    - utter_comebacklater

## interactive_story_1
* firstConversation
    - utter_firstgreet
    - utter_firstConversation
* deny
    - utter_comebacklater

## form test
* checkup
    - check_up_form
    - slot{"saignement": true}

## chatbotFirst
    - action_reminder

## premiere conversation OUI dowi
* firstConversation
    - utter_firstgreet
    - utter_firstConversation
* affirm
    - initialization_form
    - form{"name": "initialization_form"}
    - slot{"requested_slot": "name"}
* form: gavename{"name": "Léa"}
    - form: initialization_form
    - slot{"name": "Léa"}
    - slot{"requested_slot": "age"}
* form: give_age{"age": "23"}
    - form: initialization_form
    - slot{"age": "23"}
    - slot{"requested_slot": "pathologie"}
* form: Dents de sagesse{"pathologie": "Dents de sagesse"}
    - slot{"pathologie": "Dents de sagesse"}
    - form: initialization_form
    - slot{"pathologie": "Dents de sagesse"}
    - slot{"requested_slot": "type_intervention"}
* form: inter_local{"type_intervention": "local"}
    - slot{"type_intervention": "local"}
    - form: initialization_form
    - slot{"type_intervention": "local"}
    - slot{"requested_slot": "date"}
* form: give_date{"date": "12/10/20"}
    - form: initialization_form
    - slot{"date": "12/10/20"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_timer
    - utter_slot_values
    - action_reminder_pre

## change day
* next_day
    - action_change_day
    - slot{"timer": -20}

## options
* greet
    - action_PersoHello
    - utter_options

## options 2
* greet
    - action_PersoHello
    - utter_options

## ask conseil 2
* conseil_jour
    - action_conseils

## ask_preparation
* preparation
    - action_preparation

## ask_stresse
* stresse
    - action_stresse


## thanks
* thanks
    - utter_thanks

## blague:
* blague
    - action_blagues

## compliments:
* compliments
    - utter_compliments
    
## insultes
* insultes
    - utter_insultes

## interactive_story_1
* firstConversation
    - utter_firstgreet
    - utter_firstConversation
* affirm
    - initialization_form
    - form{"name": "initialization_form"}
    - slot{"requested_slot": "name"}
* form: gavename{"name": "henri"}
    - form: initialization_form
    - slot{"name": "henri"}
    - slot{"requested_slot": "age"}
* form: give_age{"age": "19"}
    - form: initialization_form
    - slot{"age": "19"}
    - slot{"requested_slot": "pathologie"}
* form: dents_sagesse{"pathologie": "dents de sagesse"}
    - slot{"pathologie": "dents de sagesse"}
    - form: initialization_form
    - slot{"pathologie": "dents de sagesse"}
    - slot{"requested_slot": "date"}
* form: give_date{"date": "12/12/19"}
    - form: initialization_form
    - slot{"date": "12/12/19"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slot_values
    - action_reminder_pre
    - reminder{"action": "action_J_1", "date_time": "2019-11-15T16:09:49.243304", "name": "f1a160e6-07b9-11ea-8d33-6003089d1d42", "kill_on_user_msg": false}
    - reminder{"action": "action_J_2", "date_time": "2019-11-15T16:09:59.243321", "name": "f1a1688e-07b9-11ea-8d33-6003089d1d42", "kill_on_user_msg": false}

