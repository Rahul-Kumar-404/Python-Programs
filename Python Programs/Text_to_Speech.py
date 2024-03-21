import pyttsx3

engine = pyttsx3.init()

text = "Hey Guys! how are you doing"

engine.say(text)

engine.runAndWait()