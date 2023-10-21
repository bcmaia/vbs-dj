import cohere
from cohere.responses.classify import Example
import os
from dotenv import load_dotenv


# Setup
load_dotenv()
api_is_active = False
token = os.environ.get('COHERE_TOKEN')

co = cohere.Client(token)

examples = [
    Example("Please, play", "play"),
    Example("Hit it", "play"),
    Example("Stop now", "stop"),
    Example("You can stop", "stop"),
    Example("Could you show me", "find"),
    Example("List this", "find"),
    Example("Search for your mom", "find"),
    Example("I want sonata", "play"),
    Example("Can I see", "find"),
    Example("One moment", "stop"),
    Example("Run the song", "play"),
    Example("Unpause","play"),
    Example("Pause","stop"),
    Example("On","play"),
    Example("Freeze","stop"),
    Example("Off","stop"),
    Example("Start","play"),
    Example("Which are my options","find"),
    Example("Menu","find"),
    Example("Search","find"),
    Example("Margarret","error"),
    Example("bohemian rapsody")
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
  "Susan",
  "Bohemian Rapsody",
]

response = co.classify(
  inputs=inputs,
  examples=examples,
)
for _,j in enumerate(response):
    print(j.predictions)
    print(j.confidences)
    print()
