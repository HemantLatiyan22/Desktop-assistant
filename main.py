import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Initializing Godfrey...")

MASTER = "Hemant"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

# Speak function will speak the string passed to it
def speak(text):
    # rate = engine.getProperty('rate')
    # engine.setProperty('rate', rate-10)
    engine.say(text)
    engine.runAndWait()

# Wishme wishes the user
def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<=12:
        speak("Good Morning"+ MASTER)
    elif hour>=12 and hour<=18:
        speak("Good Afternoon"+ MASTER)
    else:
        speak("Good Evening"+ MASTER)

    speak("I am Godfrey. How may i help you?")

# Takes commands from user through microphone
def commandInput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"you said: {query}\n")

    except Exception as e:
        print("Say that again please.")
        query = None

    return query.lower()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('dororobozo@gmail.com','hyakkimaru')
    server.sendmail('hemant.latiyan2208@gmail.com',to,content)
    server.close()

def main():
    # Main program starts here
    speak("Initializing Godfrey...")
    wishMe()
    query = commandInput()

    #logic for executing tasks as per query
    if 'wikipedia' in query:
        speak('searching wikipedia. . .')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences = 2)
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        webbrowser.get('firefox').open_new_tab('youtube.com')

    elif 'open google' in query:
        webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        webbrowser.get('firefox').open_new_tab('google.com')

    elif 'open reddit' in query:
        webbrowser.register('firefox',None,webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
        webbrowser.get('firefox').open_new_tab('reddit.com')

    elif 'play music' in query:
        songs_dir = "C://Users//heman//Downloads//Music"
        songs = os.listdir(songs_dir)
        # print(songs)
        os.startfile(os.path.join(songs_dir,songs[1]))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif 'email to hemant' in query:
        try:
            speak("What should i send?")
            content = commandInput()
            to = "tushar20254@iiitd.ac.in"
            sendEmail(to,content)
            speak("Your email has been sent successfully")
        except Exception as e:
            print(e)

main()


