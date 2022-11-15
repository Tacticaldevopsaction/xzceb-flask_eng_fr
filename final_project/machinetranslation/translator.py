import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('apikey')
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')

def english_to_french(englishText):
    #write the code here to translate English to French
    frenchText = language_translator.translate(englishText)

    return frenchText

def french_to_english(frenchText):
    #write the code here to translate French to English
    englishText = language_translator.translate(frenchText)

    return englishText