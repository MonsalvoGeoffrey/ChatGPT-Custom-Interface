import openai
from message import Message

class Conversation():
    def __init__(self, system_message="You are a helpful assistant."):
        self.messages = [Message("system", system_message)]

    def add_message(self, role, content):
        self.messages.append(Message(role, content))

    def __repr__(self):
        return f"Conversation({self.messages})"
    
    def prompt(self, message):
        self.add_message("user", message)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[message.asdict() for message in self.messages]
        )
        res = response.choices[0].message.content # type: ignore
        self.add_message("assistant", res)
        return res