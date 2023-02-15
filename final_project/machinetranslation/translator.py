import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

def translator_instance():
    ''' Defines instance of ibm watson translator '''

    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(url)

    return language_translator

def english_to_french(english_text):
    '''Takes text from english and translates to french '''

    if not english_text:
        return ""
    translator = translator_instance()
    french_text = translator.translate(
        text=english_text,
        model_id="en-fr").get_result()["translations"][0]["translation"]
    return french_text

def french_to_english(french_text):
    '''Takes text from french to english '''

    if not french_text:
        return ""
    translator = translator_instance()
    english_text = translator.translate(
        text=french_text,
        model_id="fr-en").get_result()["translations"][0]["translation"]

    return english_text
