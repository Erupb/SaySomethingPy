import pyttsx3
res = ""
# res = "Program ended correctly!" # When the program is ended correctly, we can add text to say about it,
# If the program doesnt work or anything else not correct due to plan - we don`t make a "ready" announce
eng = pyttsx3.init()
eng.say("Hello, there is some info about program execute:")
if res:
    eng.say(res)
else:
    eng.say("The program seems to be not ready to end work or there is an issue :(")
eng.runAndWait()
