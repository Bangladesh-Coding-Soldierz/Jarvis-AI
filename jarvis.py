import pyttsx3 # pip install pyttsx3
import datetime 
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia # pip install wikipedia
import webbrowser as wb
import psutil #pip install psutil
import pyjokes
import os

engine = pyttsx3.init()

def speak(audio): #deifning the speak function
    engine.say(audio)
    engine.runAndWait()

def time_(): #defining the time function 
    speak("the current time is")
    Time=datetime.datetime.now().strftime("%I:%M:%S") # for 12-hour clock
    speak(Time)

def date(): # defining the date function
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme(): # defining the wish function
    speak("Welcome back Tahsin!")
    time_()
    date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning Sir")
    elif hour >=12 and hour<18:
        speak("Good Afternoon Sir!")
    elif hour >=18 and hour <24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")
    speak("Jarvis at your service. Please tell me how can I help you?")

def TakeCommand(): # defining the main function for taking commands
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=8)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
        
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def cpu(): # defining the cpu function for cpu info
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)
    
def battery(): # defining the battery function for battery info
    battery = psutil.sensors_battery()
    speak("Batter is at")
    speak(battery.percent)

def joke(): 
    speak(pyjokes.get_joke)
    
if __name__ == "__main__":

    wishme()

    while True:
        query = TakeCommand().lower()

        if 'time' in query:
            time_()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak('Searching...')
            query = query.replace('wikipedia', 'wikipedia')
            result = wikipedia.summary(query, sentences=3)
            speak("according to wikipedia")
            print(result)
            speak(result)
            
        elif 'search in firefox' in query:
            speak("what should I search in firefox?")
            firefox = '/usr/bin/firefox %s'
            search = TakeCommand().lower()
            wb.get(firefox).open_new_tab(search+'.com')
            
        elif 'search in google' in query:
            speak("what should I search?")
            search_Term = TakeCommand().lower()
            speak("searching...")
            wb.open('https://www.google.com/search?q=' + search_Term)
            
        elif 'cpu' in query:
            cpu()
            
        elif 'battery' in query:
            battery()
        
        elif 'joke' in query:
            joke()
            
        elif 'go offline' in query:
            speak("Going offline sir.....")
            quit()
            
        elif 'spotify' in query:
            speak("opening spotify sir....")
            os.popen('cd /usr/usr/bin/ ; spotify')

        elif 'discord' in query:
            speak("opening discord sir....")
            os.popen('cd /usr/bin ; discord')

        elif 'vlc' in query:
            speak("opening vlc player sir....")

TakeCommand()