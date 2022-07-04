import json
from pathlib import Path
from typing import Any, Text, Dict, List


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase


class ActionCheckExistence(Action):
    # knowledge = Path("data/pokenames2s.txt").read_text().split("\n")
    knowledge1 = Path("data/companynames.txt").read_text().split("\n")
    knowledge2 = Path("data/ceonames.txt").read_text().split("\n")
    def name(self) -> Text:
        return "action_check_existence"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        for blob in tracker.latest_message['entities']:
            print(tracker.latest_message)
            if blob['entity'] == 'company_name':
                name = blob['value']
                if name in self.knowledge1:
                    dispatcher.utter_message(text=f"Yes, {name} is a Company.")
                else:
                    dispatcher.utter_message(
                        text=f"I do not recognize {name}, are you sure it is correctly spelled?")
            if blob['entity'] == 'ceo_name':
                name = blob['value']
                if name in self.knowledge2:
                    dispatcher.utter_message(text=f"Yes, {name} is a CEO.")
                else:
                    dispatcher.utter_message(
                        text=f"I do not recognize {name}, are you sure it is correctly spelled?")
        return []


class MyKnowledgeBaseAction(ActionQueryKnowledgeBase):
    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("data/ceosubset.json")
        knowledge_base.set_representation_function_of_object("company", lambda obj:obj["documentId"])
        super().__init__(knowledge_base)
