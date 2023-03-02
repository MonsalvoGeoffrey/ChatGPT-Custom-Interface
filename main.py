import os
from dotenv import load_dotenv
load_dotenv()
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
from conversation import Conversation



def main():
    conv = Conversation()
    while True:
        message = input("You: ")
        response = conv.prompt(message)
        print(f"Assistant: {response}")

if __name__ == "__main__":
    main()