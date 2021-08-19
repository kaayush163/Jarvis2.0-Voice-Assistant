import pyttsx3  # pip install pyttsx3 for text-speech conversation
import datetime
import speech_recognition as sr
import wikipedia
import smtplib  #for email
import webbrowser as wb  # for chrome
import os  # for shutting down restating computer sytem and for playing song
import pyautogui #use for screenshot
import psutil  #use for summary of cpu uttage and battery of system
import pyjokes
import wolframalpha #Alpha is a unique engine for computing answers and providing knowledge. It works by using its vast store of expert-level knowledge and algorithms to automatically answer questions, do analysis and generate reports.

engine = pyttsx3.init()  # to provide voiice
#voices=engine.getProperty('voices')
#engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back BOSS ")

    time()

    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Boss!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Boss")
    elif hour >= 18 and hour < 24:
        speak("Good evening Boss")
    else:
        speak("good night boss")

    speak("Jarvis at your serice ,Please tell me how can i help you ?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Go ahead,I'm Listening....")
        r.pause_threshod = 1  # wait for one second
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please... ")

        return "Sorry Boss no idea"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()  # check with gmail is valid or not
    server.starttls()  #ascend email
    server.login('youremail@gmail.com', '123')
    server.sendmail('youremail@gmail.com', to, content) #to whom and content passed
    server.close()


def screenshot():
    img=pyautogui.screenshot()
    img.save("C:\\Users\\asus\\Desktop\\Desktop\\MY RESUME\\MINOR PROJECT 3rd year\\ss.png")


def cpu():
    usage=str(psutil.cpu_percent())  #tell about cpu usage
    speak('CPU is at'+usage)
    battery=psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())  
    print(speak(pyjokes.get_joke()))  

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("Wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "aayush.cs.18@nitj.ac.in"
                # sendEmail(to,content)

                speak(content)
            except Exception as e:
                print(e)
                speak("Unable to send the email")

        elif 'search in chrome' in query:
            speak("What should i search?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')

        elif 'how are you' in query:
            speak("I am fine , Thank you")
            speak("How are you?")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by AAYUSH . Thanks you for giving me life!")

        elif "tell me about me" in query:
            speak("Aayush is a b tech final year student and he likes to do web development .")


        elif 'logout' in query:
            os.system("shutdown -l") #logout whole computer systempy

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        #elif 'open google' in query:
            #webbrowser.open("google.com")

        elif 'play songs' in query:
            songs_dir='D:\songs'
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0])) #at 0 index mean the first song played

        elif 'remember that' in query:
            speak("What should i remember")
            data=takeCommand() #take command from user
            speak("you said me to remember that"+data)
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you remember anything' in query:
            remember=open('data.txt','r')
            speak("Yeah ,I remeber that "+remember.read())

        elif 'screenshot'  in query:
            screenshot()
            speak("Done!")
        
        elif 'cpu' in query:
            cpu()
 
        elif 'joke' in query:
            print(joke())
        

        elif 'open youtube' in query:
            wb.open("youtube.com")

        elif 'open google' in query:
            wb.open("google.com")

        elif 'open stackoverflow' in query:
            wb.open("stackoverflow.com")   

        
        elif 'offline' in query:
            speak("Thank you AAYUSH and All of you for giving me your time. have a nice day")
            quit()