import tkinter as tk
import nltk
from nltk.chat.util import Chat, reflections

pattern = [
    (r"hi|hello|hey", ["Hello"]),
    (r"What is your name? ", ["My name is Hospital Enquiry Bot.","I'm Hosptital assistant"]),
    (r"What services do you offer? ", ["We offer a range of medical services. Please specify your enquiry."]),
    (r"(.*) (hour|open|close)",["We are open 24/7. How can we assist you"]),
    (r"(.*) (appointment|schedule|book)",["To book an appointment, please call our reception supreet birajdar at 123-456-789 "]),
    (r"(.*) (emergency|noraml checking)",["For energency please call at 911 or go to nearest hospital"]),
    (r"(.*) (payment|insurance|cost)",["Please conatct our billing department at 111-111-222-222 for any question related to payment"]),
   
    (r"(.*) (thanks|thank you)",["thank you for your Enquiry."])
]

#chatbot = Chat(pattern, reflections)
#chatbot.converse()


def chat():
    print("Hello, I am Hospital Enquiry chatbot, Hope you are well and fine..")
    chat = Chat(pattern,reflections)
    chat.converse()

if __name__ == "__main__":
    chat()