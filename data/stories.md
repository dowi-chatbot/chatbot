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
    - utter_slot_values


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

## ask_film
* ask_movie
    - action_find_movie

## ask_stresse
* stresse
    - action_stresse

## change_mail
* change_mail
    - utter_change_mail
* mail
    - slot{"mail": "o.dupain@gmail.com"}
    - utter_mail_updated

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





## interactive_story_1
* firstConversation
    - utter_firstgreet
    - utter_firstConversation
* affirm
    - initialization_form
    - form{"name": "initialization_form"}
    - slot{"requested_slot": "name"}
* form: gavename{"name": "olivier"}
    - form: initialization_form
    - slot{"name": "olivier"}
    - slot{"requested_slot": "age"}
* form: give_age{"age": "23"}
    - form: initialization_form
    - slot{"age": "23"}
    - slot{"requested_slot": "pathologie"}
* form: dents_sagesse{"pathologie": "Dents de sagesse"}
    - slot{"pathologie": "Dents de sagesse"}
    - form: initialization_form
    - slot{"pathologie": "Dents de sagesse"}
    - slot{"requested_slot": "type_intervention"}
* form: inter_local{"type_intervention": "Local"}
    - form: initialization_form
    - slot{"type_intervention": "Local"}
    - slot{"requested_slot": "date"}
* form: give_date{"date": "12/12/19"}
    - form: initialization_form
    - slot{"date": "12/12/19"}
    - slot{"requested_slot": "mail"}
* form: mail{"mail": "henri.monta@orange.fr"}
    - slot{"mail": "henri.monta@orange.fr"}
    - form: initialization_form
    - slot{"mail": "henri.monta@orange.fr"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slot_values
* greet
    - action_PersoHello
    - utter_options
* change_mail
    - utter_change_mail
* mail{"mail": "olivier@monmail.com"}
    - slot{"mail": "olivier@monmail.com"}
    - utter_mail_updated
