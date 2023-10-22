import cohere
from cohere.responses.classify import Example
import os
from dotenv import load_dotenv


# Setup
load_dotenv()
api_is_active = False

co = cohere.Client('MkWTdmLb0BQaSxI9K0fN9PjbPUT1BKDPYN4WEN2b')

examples = [
    Example("Add that music", "queue"),
    Example("Insert this one next", "queue"),
    Example("I'll watch it later", "queue"),
    Example("Remind me of this one", "queue"),
    Example("Save it for me", "queue"),
    Example("Store that one", "queue"),
    Example("store", "queue"),
    Example("Queue", "queue"),
    Example("Rewind","previous"),
    Example("Return", "previous"),
    Example("Go back", "previous"),
    Example("Previous", "previous"),
    Example("Say again","previous"),
    Example("Before", "previous"),
    Example("Next one", "next"),
    Example("Further ahead", "next"),
    Example("Skip", "next"),
    Example("Play", "play"),
    Example("Hit it", "play"),
    Example("I want sonata", "play"),
    Example("Run the song", "play"),
    Example("Unpause","play"),
    Example("On","play"),
    Example("Start","play"),
    Example("Don't play","stop"),
    Example("Stop", "stop"),
    Example("One moment", "stop"),
    Example("Pause","stop"),
    Example("Freeze","stop"),
    Example("Off","stop"),
    Example("Wait","stop"),
    Example("I guess not","stop"),
    Example("Could you show me", "find"),
    Example("Find","find"),
    Example("Similar","find"),
    Example("Search for your mom", "find"),
    Example("Can I see", "find"),
    Example("Which are my options","find"),
    Example("List","find"),
    Example("Menu","find"),
    Example("Search","find"),
    Example("Error","error"),
    Example("iorjfnerlkmeakn","error"),
    Example("vopkpemqpeomvpoqekgpoqrkp","error"),
    Example("il,vwqwpok","error"),
    Example("pwdkp loiwmc sabfk","error"),
    Example("break","break"),
    Example("Breaker","break"),
]

inputs=[
  "Can I hear example",
  "End it",
  "Let's go",
  "Turn it",
  "Show me",
  "Halt",
  "Enough",
  "Volume up",
  "Let's see",
  "Margarret",
  "opjr2ef",
  "prejpqerjbmpeo",
  "vemknma elçonbqjpe",
]

twinput=[
    "Okay",
]

response = co.classify(
  inputs=inputs,
  examples=examples,
)
for _,j in enumerate(response):
    print(j.predictions[0])
    print(j.confidences[0])
    print()

response = co.classify(
  inputs=twinput,
  examples=examples,
)

print(response[0].predictions[0])