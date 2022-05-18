import pyttsx3
import speech_recognition as sr 
import webbrowser
from bs4 import BeautifulSoup
import pywhatkit
import wikipedia
from googletrans import Translator
import os
import pyautogui
import requests
import psutil
import datetime
from playsound import playsound
import keyboard
import pyjokes


Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',190)


def Speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f": {audio}")
    print("   ")
    print("   ")
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print(": Listening....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print(": Recognizing.....")
            query = command.recognize_google(audio,language='en-in')
            print(f": You Said : {query}\n")

        except:
            return "none"

        return query.lower()

def TaskExe():

    def Music():
        Speak("Tell Me The Name Of The Song!")
        musicName = takecommand()

        if 'grateful' in musicName:
            os.startfile('C:\JarvisYt\Grateful(PaglaSongs).mp3')

        else:
           pywhatkit.playonyt(musicName)
        Speak("Your Song Has Been Started! , Enjoy Sir!")

    def Whatsapp():
        Speak("Tell Me The Name Of The Person")
        name = takecommand()

        if 'Sona' in name:
            Speak("Tell Me The Message!")
            msg = takecommand()
            Speak("Tell Me The Time Sir!")
            Speak("Time In Hour!")
            hour = int(takecommand())
            Speak("Time In Minutes!")
            min = int (takecommand())
            pywhatkit.sendwhatmsg("+919457028190",msg,hour,min,20)
            Speak("Ok Sir , Sending Whatsapp Message !")

        elif 'Dhananjay' in query:
              Speak("Tell Me The Message!")
              msg = takecommand()
              Speak("Tell Me The Time Sir!")
              Speak("Time In Hour!")
              hour = int(takecommand())
              Speak("Time In Minutes!")
              min = int(takecommand())
              pywhatkit.sendwhatmsg("+917086380791",msg,hour,min,20)
              Speak("Ok Sir , Sending Whatsapp Message !")

        elif 'Digvijay' in query:
              Speak("Tell Me The Message!")
              msg = takecommand()
              Speak("Tell Me The Time Sir!")
              Speak("Time In Hour!")
              hour = int(takecommand())
              Speak("Time In Minutes!")
              min = int(takecommand())
              pywhatkit.sendwhatmsg("+916003566820",msg,hour,min,20)
              Speak("Ok Sir , Sending Whatsapp Message !")

        else:
              Speak("Tell Me the Phone Number!")
              phone = int(takecommand())
              ph = '+91' + phone
              Speak("Tell Me The Message!")
              msg = takecommand()
              Speak("Tell Me The Time Sir!")
              Speak("Time In Hour!")
              hour = int(takecommand())
              Speak("Time In Minutes!")
              min = int(takecommand())
              pywhatkit.sendwhatmsg(ph,msg,hour,min,20)
              Speak("Ok Sir , Sending Whatsapp Message !")

    def OpenApps():
        Speak("Ok Sir , Wait A Second!")
        
        if 'code' in query:
            os.startfile("C:\\Applications\\Microsoft VS Code\\Code.exe")

        elif 'chrome' in query:
            os.startfile("C:\\Users\Vansh\AppData\Local\Google\Chrome\Application\chrome.exe")

        elif 'access' in query:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\MSACCESS.EXE")

        elif 'whatsapp' in query:
            webbrowser.open('https://web.whatsapp.com/')

        elif 'kite' in query:
            webbrowser.open('https://kite.zerodha.com/')

        elif 'maps' in query:
            webbrowser.open('https://www.google.co.in/maps/@26.1685248,91.7307392,12z?hl=en')

        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com/')
        
        Speak("Your Command Has Been Completed Sir!")
  
    def Temp():
        search = "temperature in digboi"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_="BNeawe").text
        Speak(f"The Temperature Outside Is {temperature} celcius")

    def CloseAPPS():
        Speak("Ok Sir , Wait A second!")

        if 'youtube' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'kite' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'code' in query:
            os.system("TASKKILL /F /im Code.exe")

        elif 'maps' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'access' in query:
            os.system("TASKKILL /F /im ACCESS.EXE")

        elif 'whatsapp' in query:
            os.system("TASKKILL /F /im chrome.exe")

        Speak("Your Command Has Been Successfully Completed!")

    def YoutubeAuto():
        Speak("Whats Your Command ?")
        comm = takecommand()
        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        Speak("Done Sir")

    def TakeHindi():
        command = sr.Recognizer()
        with sr.Microphone() as source:
             print("Listening....")
             command.pause_threshold = 1
             audio = command.listen(source)

             try:
                  print("Recognizing.....")
                  query = command.recognize_google(audio,language='hi')
                  print(f": You Said : {query}")

             except:
                 return "none"

             return query.lower()

    def Tran():
        Speak("Tell Me The Line!")
        line = TakeHindi()
        translate = Translator()
        result = translate.translate(line)
        Text = result.text
        Speak(Text)

    def ChromeAuto():
        Speak("Chrome Automation Started!")

        command = takecommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in command:
            keyboard.press_and_release('ctrl + h')

    def screenshot():
        Speak("Ok Boss , What Should I Name That File ?")
        path = takecommand()
        path1name = path + ".png"
        path1 = "E:\\ScreenShot By Jarvis\\"+ path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("E:\\ScreenShot By Jarvis")
        Speak("Here Is Your ScreenShot")
    
    while True:

        query = takecommand()

        if 'hello' in query:
            Speak("Hello Sir , I Am Jarvis .")
            Speak("You Personal AI Assistant!")
            Speak("How May I Help You?")

        elif 'how are you' in query:
            Speak("I Am Fine Sir!")
            Speak("What's About You?")

        elif 'you need a break' in query:
            Speak("Ok Sir, You Can Call Me Anytime!")
            break

        elif 'bye' in query:
            Speak("Bye Sir have a Great Time!")

        elif 'thank you for all jarvis' in query:
            Speak("My Pleasure Sir! that you liked my work!")

        elif 'youtube search' in query:
            Speak("Ok Sir , This is What I found For Your Search!")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Done Sir!")

        elif 'web search' in query:
            Speak("This Is What I found For Your Search Sir!")
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            pywhatkit.search(query)
            Speak("Done Sir!")

        elif 'website' in query:
            Speak("Ok Sir , Launching......")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Launched!")

        elif 'launch' in query:
            Speak("Tell Me The Name Of The Website!")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done Sir!")

        elif 'music' in query:
            Music()
        
        elif 'wikipedia' in query:
            Speak("Searching Wikipedia......")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According To Wikipedia : {wiki}")

        elif 'whatsapp message' in query:
            Whatsapp()

        elif 'screenshot' in query:
           screenshot()

        elif 'open whatsapp' in query:
            OpenApps()

        elif 'open kite' in query:
            OpenApps()    
        
        elif 'open maps' in query:
            OpenApps()

        elif 'open youtube' in query:
            OpenApps()

        elif 'open code' in query:
            OpenApps()

        elif 'open chrome' in query:
            OpenApps()
        
        elif 'open access' in query:
            OpenApps()

        elif 'close whatsapp' in query:
            CloseAPPS()
 
        elif 'close access' in query:
            CloseAPPS()

        elif 'close chrome' in query:
            CloseAPPS()

        elif 'close youtube' in query:
            CloseAPPS()

        elif 'close code' in query:
            CloseAPPS()

        elif 'close kite' in query:
            CloseAPPS()

        elif 'close maps' in query:
            CloseAPPS()

        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'youtube tool' in query:
            YoutubeAuto()

        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')

        elif 'chrome automation' in query:
            ChromeAuto()

        elif 'joke' in query:
            get = pyjokes.get_joke()
            Speak(get)

        elif 'repeat my words' in query:
            Speak("Speak Sir!")
            jj = takecommand()
            Speak(f"You Said : {jj}")

        elif 'my location' in query:
            Speak("Ok Sir , Wait A Second!")
            webbrowser.open('https://www.google.co.in/maps/place/Digboi,+Assam+786171/@27.3961643,95.5968806,13z/data=!3m1!4b1!4m5!3m4!1s0x373f224bedb2f695:0x98e34c5fbbcbff5e!8m2!3d27.395241!4d95.6301498?hl=en')

        elif 'alarm' in query:
           Speak("Enter The Time !") 
           time = input(": Enter The Time : ")

           while True:
               Time_Ac = datetime.datetime.now()
               now = Time_Ac.strftime("%H:%M:%S")

               if now == time:
                   Speak("Time To Wake Up Sir!")
                   playsound('C:\JarvisYt\Grateful(PaglaSongs).mp3')
                   Speak("Alarm Closed!")

               elif now>time:
                  break
     
        elif 'translator' in query:
            Tran() 

        elif 'remember that' in query:
            remeberMsg = query.replace("remember that","")
            remeberMsg = remeberMsg.replace("jarvis","")
            Speak("You Tell Me To Remind You That :"+remeberMsg)
            remeber = open('data.txt','w')
            remeber.write(remeberMsg)
            remeber.close()

        elif 'what do you remeber jarvis' in query:
            remeber = open('data.txt','r')
            Speak("You Tell Me That" + remeber.read())

        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            query = query.replace("google","")
            Speak("This Is What I Found On Web!")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,3) 
                Speak(result)

            except:
                Speak("No Speakable Data Available")

        elif 'temperature' in query:
            Temp()

TaskExe()















