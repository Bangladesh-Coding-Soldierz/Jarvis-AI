import pyttsx3 # pip install pyttsx3
import datetime 
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia # pip install wikipedia
import webbrowser as wb
import psutil #pip install psutil
import pyjokes # pip install pyjokes
import os
import smtplib
import pyautogui #pip install pyautogui
import wolframalpha # pip install wolframalpha
import turtle as tt # pip install turtle

wolframalpha_app_id = 'your_api' #get your api from https://products.wolframalpha.com/api/ 

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
        audio = r.listen(source, timeout=5)
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
    
def send_email():
    speak("who is the reciever sir?")
    TO = input("Please enter the reciever email: ")
    FROM = "your email here"
    passwd = 'your password hehe'
    speak('what is the subject sir?')
    SUBJECT = input('Subject: ')
    speak('enter the email body please!')
    text = input("Email body: ")

    BODY = "\r\n".join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT ,
        "",
        text
        ))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(FROM, passwd)
    server.sendmail(FROM, [TO], BODY)
    print('aeh')
    server.quit()

def scrnshot():
    speak('taken secreenshot sir!')
    img = pyautogui.screenshot()
    img.show()

def sqre():
    tt.title('Square Shape')
    speak('What should be the square color sir?')
    sqcolor = input('Please type the color name: ')
    tt.hideturtle()
    tt.fillcolor(sqcolor)
    tt.begin_fill()
    tt.color(sqcolor)
    tt.forward(200)
    tt.left(90)
    tt.forward(200)
    tt.left(90)
    tt.forward(200)
    tt.left(90)
    tt.forward(200)
    tt.left(90)
    tt.end_fill()
    tt.done()

def trng():
    speak('What should be the triangle color sir?')
    sqcolor = input('Please type the color sir: ')
    tt.hideturtle()
    tt.fillcolor(sqcolor)
    tt.begin_fill()
    tt.color(sqcolor)
    tt.forward(200)
    tt.left(120)
    tt.forward(200)
    tt.left(120)
    tt.forward(200)
    tt.left(120)
    tt.end_fill()
    tt.done()

def hrt():
    speak("What should be the heart color sir?")
    hrtcolor = input('Please type the color sir: ')
    speak('What should be the background color sir?')
    hrtbg = input('Please type the background color sir: ')
    tt.color(hrtcolor)
    tt.fillcolor(hrtcolor)
    tt.bgcolor(hrtbg)
    tt.begin_fill()
    tt.left(50)
    tt.forward(100)
    tt.circle(40, 180)
    tt.left(260)
    tt.circle(40, 180)
    tt.forward(100)
    tt.end_fill()
    tt.done()
    
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
            os.popen('cd /usr/bin ; vlc')

        elif 'terminal' in query:
            speak("opening terminal sir....")
            os.popen('cd /usr/bin/ ; termit')

        elif 'music player' in query:
            speak("opening music-player sir....")
            os.popen('cd /usr/bin ; deepin-music')

        elif 'pdf' in query:
            speak("opening pdf viewer sir....")
            os.popen('cd /usr/bin ; wpspdf')

        elif 'screen recorder' in query:
            speak("opening screen recorder sir....")
            os.popen('cd /usr/bin ; obs')

        elif 'calculator' in query:
            speak("opening calculator sir....")
            os.popen('cd /usr/bin ; gnome-calculator')

        elif 'notepad' in query:
            speak("opening notepad sir....")
            os.popen('cd /usr/bin ; pluma')

        elif 'virtual keyboard'  in query:
            speak("opening virtual keyboard sir....")
            os.popen('cd /usr/bin ; onboard')
            
        elif 'send email' in query:
            send_email()

        elif 'screenshot' in query:
            scrnshot()

        elif 'draw a square' in query:
            sqre()

        elif 'draw a triangle' in query:
            trng()

        elif 'draw a heart' in query:
            hrt()

        elif 'calculate' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

TakeCommand()