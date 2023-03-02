from conversation import Conversation
import os
from dotenv import load_dotenv
load_dotenv()

key = os.environ.get('OPEN_AI_KEY')

print(key)