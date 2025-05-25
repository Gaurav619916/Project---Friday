import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    # if c.lower() == "open google":
    if "open google" in c.lower():
       webbrowser.open("https://google.com")
    elif "open facbook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedln" in c.lower():
        webbrowser.open("https://linkedln.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song or playlist.")
        
if __name__ == "__main__":
    speak("friday Initializing...")
    while True:
        #Listen for the wake word "jarvis"
        #obtain audio form the microphone
        r = sr.Recognizer()
        
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout = 2, phrase_time_limit = 2)
            word = r.recognize_google(audio)
            #print(command)
            if(word.lower() == "friday"):
                speak("Yes,sir")
                #listen for command
                with sr.Microphone() as source:
                    print("friday Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("error; {0}".format(e))

