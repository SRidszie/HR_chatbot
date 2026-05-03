# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted , SlotSet
from rasa_sdk.forms import FormValidationAction


# class ActionGreetUser(Action):

#     def name(self) -> Text:
#         return "action_greet"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         # (Job, Collaboration, Support, Services, or Solutions)
#         button_data = [
#             {"title": "Candidate looking for Job", 
#              "payload": "/job_application{"PRODUCT":"job_application"}"},
#             {
#                 "title": "Partner looking to Collaborate",
#                 "payload": "/partner_collaboration{"PRODUCT":"partner_collaboration"}",
#             },
#             {
#                 "title": "Client looking for Support",
#                 "payload": "/client_support{"PRODUCT":"client_support"}",
#             },
#             {
#                 "title": "Services",
#                 "payload": "/services{"PRODUCT":"services"}",
#             },            
#             {
#                 "title": "Solutions",
#                 "payload": "/solutions{"PRODUCT":"solutions"}",
#             },    
#         ]

#         # message = {"payload": "quickReplies", "data": data}


#         dispatcher.utter_message(text="Hi there! I am Nityo Infotech virtual assistant. How can I help you today?")
#         # dispatcher.utter_message(text="Select a category below that best fits your needs (Job, Collaboration, Support, Services, or Solutions) to proceed:")
#         dispatcher.utter_message(
#             # text="Select a category below that best fits your needs to proceed:", json_message=message
#             text="Select a category below that best fits your needs to proceed:", buttons=button_data
#         )

#         return []


class ActionGreetUser(Action):

    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button_data = [
            {"title": "Candidate looking for Job", 
             "payload": "/job_application"},
            {
                "title": "Partner looking to Collaborate",
                "payload": "/partner_collaboration",
            },
            {
                "title": "Client looking for Support",
                "payload": "/client_support",
            },
            {
                "title": "Services",
                "payload": "/services",
            },            
            {
                "title": "Solutions",
                "payload": "/solutions",
            },    
        ]

        dispatcher.utter_message(text="Hi there! I am Nityo Infotech virtual assistant. How can I help you today?")
        dispatcher.utter_message(
            text="Select a category below that best fits your needs to proceed:", buttons=button_data
        )

        return []



class ActionServices(Action):

    def name(self) -> Text:
        return "action_services"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # (Job, Collaboration, Support, Services, or Solutions)
        button_data = [
        {"title": "AMS", "payload": "/ams"},
        {"title": "ERP & CRM", "payload": "/erp_crm"},
        {"title": "SAP", "payload": "/sap"},
        {"title": "ORACLE", "payload": "/oracle"},
        {"title": "SALESFORCE", "payload": "/salesforce"},
        {"title": "MUREX", "payload": "/murex"},
        {"title": "CLOUD SERVICES", "payload": "/cloud services"},
        {"title": "PROFESSIONAL & MANAGED SERVICES", "payload": "/professional_managed services"},
        {"title": "MOBILITY", "payload": "/mobility"},
        {"title": "EMERGING TECH & PROJECTS", "payload": "/emerging_tech_projects"},
        {"title": "DATA ANALYTICS", "payload": "/data_analytics"},
        {"title": "INFRASTRUCTURE MANAGEMENT SERVICES", "payload": "/infrastructure_management_services"},
        {"title": "GEOSPATIAL SERVICES", "payload": "/geospatial_services"},
        {"title": "COMMUNICATION SERVICES", "payload": "/communication_services"},
        {"title": "SITE RELIABILITY ENGINEERING & DEV OPS", "payload": "/site_reliability_eng_devops"},
        {"title": "CONSULTING SERVICES", "payload": "/consulting_services"},
        {"title": "BUSINESS PROCESS OUTSOURCING", "payload": "/business_process_outsourcing"},
        {"title": "TESTING SERVICES", "payload": "/testing_services"},
        {"title": "TRAINING SERVICES", "payload": "/training_services"},
        ]

        message = {"payload": "quickReplies", "data": button_data}
        # message = {"payload": "dropDown", "data": button_data}


        dispatcher.utter_message(
            text="Select a category below to view our offerings:", json_message=message
            # text="Select services from the list for more information:", buttons=button_data
        )

        return []


class ActionServicedetails(Action):
    def name(self) -> Text:
        return "action_ams"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        Link = "https://nityo.com/ams"
        # response = f"Here's the link: {url_link}"
        # attachment = {
        #     "type": "button",
        #     "text": "Click here to open the link",
        #     "url": link
        # }
        
        # button_data = [
        #     {"title": "Click here to open the link", 
        #      "url": "https://nityo.com/ams"},]
        
        
        # dispatcher.utter_message(text=response, buttons=button_data)
        # dispatcher.utter_message(response="utter_ams", link=url_link)
        # Link="http://www.innovateyourself.in/"
        # dispatcher.utter_message(text="Hello World!")
        # print("Link: ",tracker.get_slot('LINK'))
        # text=tracker.latest_message['text']
        # print(text)
        # dispatcher.utter_template("utter_ams",tracker,link=Link)
        # return []
    
    
        dispatcher.utter_message(response="utter_ams", link=Link)
        return []


        
        # Link = "https://nityo.com/ams"

        # # msg = {
        # #     # "type": "pdf_attachment",
        # #     "payload": {
        # #         # "title": "AMS Details",
        # #         "src": "https://nityo.com/ams",
        # #     },
        # # }
        # dispatcher.utter_message(response="utter_ams", link=Link)
        # # dispatcher.utter_message(
        # #     text="Great, you can read more about AMS here...: ", 
        # #     attachment=msg
        # # )
        # return []


# https://forms.gle/nGXNjUJjGguBgR6N7


# class ActionContactDetails(Action):
#     def name(self) -> Text:
#         return "action_contact_details"

#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(
#             text="Plesae find the important contact details of the company 😉",
#             image="https://images.squarespace-cdn.com/content/v1/56d8237c2eeb81e53070507d/1523189122894-NRB0D0N6NYI5CT7MK26W/ke17ZwdGBToddI8pDm48kJ7fi-SkbQ8aGt3nngdz-At7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z4YTzHvnKhyp6Da-NYroOW3ZGjoBKy3azqku80C789l0lCYWGxfdB_uf1_ERfebHZ7WmhdMGqxpiTlRNDGsF8x3fHfoV6HuprcqilYNcCfQsg/Contact+details.jpg",
#         )

#         return []


### IMP -->


# class EnquiryForm(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_speak_with_expert_form"
    
#     @staticmethod
#     # def required_slots(tracker: Tracker) -> List[Text]:
#     def required_slots() -> List[Text]:
#         return ["user_name", "business_email", "phone_no", "enquiry_type"]

#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
#         return {
#             "user_name": [
#                 self.from_text(),
#             ],
#             "business_email": [
#                 self.from_text(),
#             ],
#             "phone_no": [
#                 self.from_text(),
#             ],
#             "enquiry_type": [
#                 self.from_text(),
#             ],
#         }

#     async def submit(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         # get the values of the slots
#         user_name = tracker.get_slot("user_name")
#         business_email = tracker.get_slot("business_email")
#         phone_no = tracker.get_slot("phone_no")
#         enquiry_type = tracker.get_slot("enquiry_type")

#         # send the submitted information back to the user
#         dispatcher.utter_message(
#             f"Thank you for your submission. Here is a summary of your information:\n"
#             f"- Name: {user_name}\n"
#             f"- Business Email: {business_email}\n"
#             f"- Phone Number: {phone_no}\n"
#             f"- Enquiry Type: {enquiry_type}"
#         )

#         # clear the slots
#         return [SlotSet("user_name", None), SlotSet("business_email", None), SlotSet("phone_no", None), SlotSet("enquiry_type", None)]





# class EnquiryForm(FormValidationAction):
#     def name(self) -> Text:
#         return "speak_with_expert_form"
    
#     @staticmethod
#     # def required_slots(tracker: Tracker) -> List[Text]:
#     def required_slots() -> List[Text]:    
#         return ["user_name", "business_email", "phone_no", "enquiry_type"]

#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
#         return {
#             "user_name": [self.from_entity(entity="user_name")],
#             "business_email": [self.from_entity(entity="business_email")],
#             "phone_no": [self.from_entity(entity="phone_no")],
#             "enquiry_type": [self.from_entity(entity="enquiry_type")]
#         }

#     async def submit(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         # get the values of the slots
#         user_name = tracker.get_slot("user_name")
#         business_email = tracker.get_slot("business_email")
#         phone_no = tracker.get_slot("phone_no")
#         enquiry_type = tracker.get_slot("enquiry_type")

#         # send the submitted information back to the user
#         dispatcher.utter_message(
#             f"Thank you for your submission. Here is a summary of your information:\n"
#             f"- Name: {user_name}\n"
#             f"- Business Email: {business_email}\n"
#             f"- Phone Number: {phone_no}\n"
#             f"- Enquiry Type: {enquiry_type}"
#         )

#         # clear the slots
#         return [SlotSet("user_name", None), SlotSet("business_email", None), SlotSet("phone_no", None), SlotSet("enquiry_type", None)]



# class EnquiryForm(FormValidationAction):
#     def name(self) -> Text:
#         return "speak_with_expert_form"
    
#     @staticmethod
#     # def required_slots(tracker: Tracker) -> List[Text]:
#     def required_slots() -> List[Text]:
#         return ["user_name", "business_email", "phone_no", "enquiry_type"]

#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
#         return {
#             "user_name": [
#                 self.from_intent(intent="expert_speak", value=self.extract_user_name),
#                 self.from_text()
#             ],
#             "business_email": [
#                 self.from_intent(intent="expert_speak", value=self.extract_business_email),
#                 self.from_text()
#             ],
#             "phone_no": [
#                 self.from_intent(intent="expert_speak", value=self.extract_phone_no),
#                 self.from_text()
#             ],
#             "enquiry_type": [
#                 self.from_intent(intent="expert_speak", value=self.extract_enquiry_type),
#                 self.from_text()
#             ]
#         }

#     def extract_user_name(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Optional[Text]:
#         return value if self.is_valid_name(value) else None

#     def extract_business_email(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Optional[Text]:
#         return value if self.is_valid_email(value) else None

#     def extract_phone_no(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Optional[Text]:
#         return value if self.is_valid_phone_no(value) else None

#     def extract_enquiry_type(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Optional[Text]:
#         return value if self.is_valid_enquiry_type(value) else None

#     # def is_valid_name(self, value: Text) -> bool:
#     #     # Implement logic to validate the user name
#     #     return True

#     # def is_valid_email(self, value: Text) -> bool:
#     #     # Implement logic to validate the email address
#     #     return True

#     # def is_valid_phone_no(self, value: Text) -> bool:
#     #     # Implement logic to validate the phone number
#     #     return True

#     # def is_valid_enquiry_type(self, value: Text) -> bool:
#     #     # Implement logic to validate the enquiry type
#     #     return True

#     async def submit(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         # get the values of the slots
#         user_name = tracker.get_slot("user_name")
#         business_email = tracker.get_slot("business_email")
#         phone_no = tracker.get_slot("phone_no")
#         enquiry_type = tracker.get_slot("enquiry_type")

#         # send the submitted information back to the user
#         dispatcher.utter_message(
#             f"Thank you for your submission. Here is a summary of your information:\n"
#             f"- Name: {user_name}\n"
#             f"- Business Email: {business_email}\n"
#             f"- Phone Number: {phone_no}\n"
#             f"- Enquiry Type: {enquiry_type}"
#         )

#         # clear the slots
#         return [SlotSet("user_name", None), SlotSet("business_email", None), SlotSet("phone_no", None), SlotSet("enquiry_type", None)]



# class EnquiryForm(FormValidationAction):

#     def name(self) -> Text:
#         return "speak_with_expert_form"

#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         return ["user_name", "business_email", "phone_no", "enquiry_type"]

#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
#         return {
#             "user_name": [self.from_entity(entity="name")],
#             "business_email": [self.from_entity(entity="business_email")],
#             "phone_no": [self.from_entity(entity="phone_no")],
#             "enquiry_type": [self.from_entity(entity="enquiry_type")]
#         }

#     def submit(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict]:
#         # get the values of the slots
#         user_name = tracker.get_slot("user_name")
#         business_email = tracker.get_slot("business_email")
#         phone_no = tracker.get_slot("phone_no")
#         enquiry_type = tracker.get_slot("enquiry_type")

#         # send the submitted information back to the user
#         dispatcher.utter_message(
#             f"Thank you for your submission. Here is a summary of your information:\n"
#             f"- Name: {user_name}\n"
#             f"- Business Email: {business_email}\n"
#             f"- Phone Number: {phone_no}\n"
#             f"- Enquiry Type: {enquiry_type}"
#         )

#         # clear the slots
#         return [SlotSet("user_name", None), SlotSet("business_email", None), SlotSet("phone_no", None), SlotSet("enquiry_type", None)]



# class ActionServiceCategory(Action):
#     def name(self) -> Text:
#         return "action_service_category"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[Dict[Text, Any]]:
#         category = tracker.get_slot("category")
#         if category:
#             if category == "Services":
#                 services = [    "1. AMS",    "2. ERP & CRM",    "3. SAP",    "4. ORACLE",    "5. SALESFORCE",    "6. MUREX",    "7. CLOUD SERVICES",    "8. PROFESSIONAL & MANAGED SERVICES",    "9. MOBILITY",    "10. EMERGING TECH & PROJECTS",    "11. DATA ANALYTICS",    "12. INFRASTRUCTURE MANAGEMENT SERVICES",    "13. GEOSPATIAL SERVICES",    "14. COMMUNICATION SERVICES",    "15. SITE RELIABILITY ENGINEERING & DEV OPS",    "16. CONSULTING SERVICES",    "17. BUSINESS PROCESS OUTSOURCING",    "18. TESTING SERVICES",    "19. TRAINING SERVICES"]
#                 # services = [
#                 #     "1. Service 1",
#                 #     "2. Service 2",
#                 #     "3. Service 3",
#                 #     "4. Service 4",
#                 #     "5. Service 5",
#                 #     "6. Service 6",
#                 #     "7. Service 7",
#                 #     "8. Service 8",
#                 #     "9. Service 9",
#                 #     "10. Service 10",
#                 #     "11. Service 11",
#                 #     "12. Service 12",
#                 #     "13. Service 13",
#                 #     "14. Service 14",
#                 #     "15. Service 15",
#                 #     "16. Service 16",
#                 #     "17. Service 17",
#                 #     "18. Service 18",
#                 #     "19. Service 19"
#                 # ]
#                 services_text = "\n".join(services)
#                 dispatcher.utter_message(text=f"Here are the services we offer:\n\n{services_text}")
#             else:
#                 dispatcher.utter_message(text="We can connect you with an expert in your selected category. Please provide your name, business email, phone number, and service type so we can connect you with an expert.")
#         return []





# class ActionFormSubmit(Action):
#     def name(self) -> Text:
#         return "action_form_submit"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[Dict[Text, Any]]:
#         name = tracker.get_slot("name")
#         email = tracker.get_slot("business_email")
#         phone = tracker.get_slot("phone")
#         service_type = tracker.get_slot("service_type")
#         # You can add your own logic here to submit the form data to a database or CRM
#         dispatcher.utter_message(text="Thank you for submitting the form. We will get in touch with you soon.")
#         return [SlotSet("name", None), SlotSet("business_email", None), SlotSet("phone", None), SlotSet("service_type", None)]



# class ActionServiceCategory(Action):

#     def name(self) -> Text:
#         return "action_service_category"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         service_categories = [
#             "1. AMS",
#             "2. ERP & CRM",
#             "3. SAP",
#             "4. ORACLE",
#             "5. SALESFORCE",
#             "6. MUREX",
#             "7. CLOUD SERVICES",
#             "8. PROFESSIONAL & MANAGED SERVICES",
#             "9. MOBILITY",
#             "10. EMERGING TECH & PROJECTS",
#             "11. DATA ANALYTICS",
#             "12. INFRASTRUCTURE MANAGEMENT SERVICES",
#             "13. GEOSPATIAL SERVICES",
#             "14. COMMUNICATION SERVICES",
#             "15. SITE RELIABILITY ENGINEERING & DEV OPS",
#             "16. CONSULTING SERVICES",
#             "17. BUSINESS PROCESS OUTSOURCING",
#             "18. TESTING SERVICES",
#             "19. TRAINING SERVICES"
#         ]

#         services_text = "\n".join(service_categories)
#         dispatcher.utter_message(text=f"Here are the services we offer:\n\n{services_text}")
        
#         # message = "Here are our service categories:\n"
#         # for category in service_categories:
#         #     message += f"\n**{category}**"

#         # dispatcher.utter_message(text=message)

#         return []



# class ContactForm(FormAction):
#     def name(self) -> Text:
#         return "contact_form"

#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         return ["name", "business_email", "phone", "service_type"]

#     def slot_mappings(self) -> Dict[Text, Any]:
#         return {
#             "name": self.from_entity(entity="name"),
#             "business_email": self.from_entity(entity="business_email"),
#             "phone": self.from_entity(entity="phone"),
#             "service_type": self.from_entity(entity="service_type")
#         }

#     def submit(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict]:
#         # Send email to the team with user's details
#         name = tracker.get_slot("name")
#         business_email = tracker.get_slot("business_email")
#         phone = tracker.get_slot("phone")
#         service_type = tracker.get_slot("service_type")
#         email_body = f"Name: {name}, Email: {business_email}, Phone: {phone}, Service Type: {service_type}"
#         # You can add code here to send the email to the team
#         dispatcher.utter_message(text="Thanks for contacting us, our team will get back to you soon....")
#         return []

# class ActionExpert(Action):
#     def name(self) -> Text:
#         return "action_expert"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Ask user to fill out the contact form
#         dispatcher.utter_message(text="Please fill out this form so we can connect you with an expert: ")
#         return [SlotSet("category", None)]









# class LeadFormFirstPart(FormAction):
#     """Example of a custom form action"""

#     def name(self) -> Text:
#         """Unique identifier of the form"""

#         return "lead_form_p1"

#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots that the form has to fill"""
#         return ["requirement", "mockup"]

#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
#         """A dictionary to map required slots to
#             - an extracted entity
#             - intent: value pairs
#             - a whole message
#             or a list of them, where a first match will be picked"""
#         return {
#             "requirement": [
#                 self.from_text(),
#             ],
#             "mockup": [
#                 self.from_text(),
#             ],
#         }

#     def submit(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict]:
#         """Define what the form has to do
#             after all required slots are filled"""

#         # utter submit template
#         dispatcher.utter_template("utter_urlAvailable", tracker)
#         return []


# class LeadFormSecondPart(FormAction):
#     """Example of a custom form action"""

#     def name(self) -> Text:
#         """Unique identifier of the form"""

#         return "lead_form_p2"

#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots that the form has to fill"""
#         return ["url"]

#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
#         """A dictionary to map required slots to
#             - an extracted entity
#             - intent: value pairs
#             - a whole message
#             or a list of them, where a first match will be picked"""
#         return {
#             "url": [
#                 self.from_text(),
#             ],
#         }

#     def submit(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict]:
#         """Define what the form has to do
#             after all required slots are filled"""
            
#         return []


# class LeadFormThirdPart(FormAction):
#     """Example of a custom form action"""

#     def name(self) -> Text:
#         """Unique identifier of the form"""

#         return "lead_form_p3"

#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots that the form has to fill"""
#         return ["timeline", "budget", "name", "email", "phone"]

#     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
#         """A dictionary to map required slots to
#             - an extracted entity
#             - intent: value pairs
#             - a whole message
#             or a list of them, where a first match will be picked"""
#         return {
#             "timeline": [
#                 self.from_text(),
#             ],
#             "budget": [
#                 self.from_text(),
#             ],
#             "name": [
#                 self.from_text(),
#             ],
#             "email": [
#                 self.from_text(),
#             ],
#             "phone": [
#                 self.from_text(),
#             ],
#         }

#     def submit(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict]:
#         """Define what the form has to do
#             after all required slots are filled"""

#         # utter submit template
#         dispatcher.utter_template("utter_lead_q2", tracker)
#         return []