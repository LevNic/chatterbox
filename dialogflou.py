import os
import logging
import dialogflow
from google.api_core.exceptions import InvalidArgument

from config import BOT_ID

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'chatterbox-s9ds-c426e39a3515.json'
DIALOGFLOW_PROJECT_ID = 'chatterbox-s9ds'
DIALOGFLOW_LANGUAGE_CODE = 'ru'
SESSION_ID = BOT_ID


class DialogFlow:

    def __init__(self):
        self.session_client = dialogflow.SessionsClient()
        self.session = self.session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

    def get_answer(self, message_text):
        text_input = dialogflow.types.TextInput(text=message_text, language_code=DIALOGFLOW_LANGUAGE_CODE)
        query_input = dialogflow.types.QueryInput(text=text_input)
        try:
            response = self.session_client.detect_intent(session=self.session, query_input=query_input)
        except InvalidArgument:
            raise

        answer = response.query_result.fulfillment_text
        if answer:
            return answer
        else:
            return 'Что?'
