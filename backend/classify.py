import cohere
from cohere.responses.classify import Example
import os
from dotenv import load_dotenv

#pip install dotenv
#pip install cohere

# Setup
load_dotenv()
api_is_active = False
token = os.environ.get('COHERE_TOKEN')

co = cohere.Client(token)

#examples and their matching classification for the cohere classify
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

#receives a string as input
def classify(input):
    user_text = [input] #stores the string as a string vector

    #forces the user_text to never be empty to avoid an error response with the API
    if(len(user_text[0])<1):
        user_text = ["error"]   

    #calls the classifier to classify according to the examples
    response = co.classify(
    inputs=user_text,
    examples=examples,
    )
    command_text = response[0].predictions[0]
    command_confidence = response[0].confidences[0]

    return command_text, command_confidence #returns a string and a float (a command and a confidence)