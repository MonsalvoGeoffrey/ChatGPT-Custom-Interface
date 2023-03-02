import os
from dotenv import load_dotenv
load_dotenv()
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("pages/index.html")




# from conversation import Conversation



# def main():
#     conv = Conversation()
#     while True:
#         message = input("You: ")
#         response = conv.prompt(message)
#         print(f"Assistant: {response}")

# if __name__ == "__main__":
#     main()