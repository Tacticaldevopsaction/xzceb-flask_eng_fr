"""
Translation package
Supported languages: English (en), French (fr)
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

VERSION = "2018-05-01"
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('apikey')
language_translator = LanguageTranslatorV3(
    version='version',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')

def english_to_french(englishtext):
    """
    This Function translates English (en) text to French (fr) text yo
    """
    if englishtext =="":
        return ""
    frenchtext = language_translator.translate(
        text=englishtext,
        model_id='en-fr').get_result()
    return frenchtext

def french_to_english(frenchtext):
    """
    This Function translates French (fr) text to English (en) text yo
    """
    if frenchtext == "":
        return ""
    englishtext = language_translator.translate(
        text=frenchtext,
        model_id='fr-en').get_result()
    return englishtext
    