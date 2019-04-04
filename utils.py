from wit import Wit
from gnewsclient import gnewsclient

access_token = "VUUDTV5DMUZQGVA66ANKETHB7BCSQ26U"

client = Wit(access_token = access_token)

message_text = "I live in canada"

resp = client.message(message_text)

print(resp)
