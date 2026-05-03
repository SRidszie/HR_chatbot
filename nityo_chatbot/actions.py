# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"


from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
import mysql.connector


# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionInvoiceAmountZone(Action):
    def name(self) -> Text:
        return "action_sales_amount"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        mydb = mysql.connector.connect(
            host="devdbrdsnew.cfgu9s5ykxy0.ap-southeast-1.rds.amazonaws.com",
            user="sandeep",
            passwd="SandeepsinghNityo",
            database="devai",
        )
        mycursor = mydb.cursor()
        # zone = tracker.get_slot("zone")
        mycursor.execute(
            "SELECT sales FROM devai.rasa_user_sales limit 1"
        )
        results = mycursor.fetchall()
        if len(results) != 0:
            for i in results:
                dispatcher.utter_message(
                    "The total Sales amount for the user is : INR {}".format(
                        str(i[0])
                    )
                )
        else:
            dispatcher.utter_message(
                text="Oops! Looks like there isn't any item available for your search"
            )

        return []
