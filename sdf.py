import speech_recognition as sr #convert speech to text
import datetime #for fetching date and time
import wikipedia
import webbrowser
import requests
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
#import wolframalpha # to calculate strings into formula
from selenium import webdriver # to control browser operations
import time
import os.path
from os import path



def talk():
    input=sr.Recognizer()
    with sr.Microphone() as source:
        input.adjust_for_ambient_noise(source,duration=1)
        audio=input.listen(source)
        data=""
        try:
            data=input.recognize_google(audio)
            print("Response is: " + data)
            
        except sr.UnknownValueError:
            print("Sorry I did not hear your question, Please repeat again.")
            return talk().lower()
    return data


def respond(output):
    num=0
    print(output)
    num += 1
    response=gTTS(text=output, lang='en')
    file = str(num)+".mp3"
    response.save(file)
    playsound.playsound(file, True)
    os.remove(file)


if __name__=='__main__':
    
    respond("Hi Praneeth, I am your personal desktop assistant")
    #os.system('ls')
          
    while(1):
        respond("How can I help you?")
        text=talk().lower()
        
        if text==0:
            continue
            
        if "stop" in str(text) or "exit" in str(text) or "bye" in str(text):
            respond("Ok bye and take care")
            break
        elif "create" in text :
            print("create test :",text)
            text = text.replace('create ','')
            if("directory" in text):
                name=text.replace( 'directory ',"")
                print(name)
            elif("folder" in text):
                name=text.replace( 'folder ',"")
                print(name)
            elif("file" in text):
                name=text.replace( 'file ',"")
                print(name)

        elif 'youtube' in text:
            chrome_paths=["C:\Program Files\Google\Chrome\Application\chrome.exe","C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]
            for c_path in chrome_paths:
                if(path.exists(c_path)):
                    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(c_path))
                    break  
            query = text.replace("youtube","")
            if query!="":
                respond("Opening in youtube")
                query=query.replace(" ","")
                webbrowser.get('chrome').open_new_tab("http://www.youtube.com/results?search_query="+str(query))
                time.sleep(3)
            else:
                respond("Please say something to search in youtube")
                
        elif "show folder" in str(text):
            print(os.listdir())
        
        elif 'wikipedia' in text:
            respond('Searching Wikipedia')
            text =text.replace("wikipedia", "")
            results = wikipedia.summary(text, sentences=2)
            respond("According to Wikipedia")
            print(results)
            respond(results)
            time.sleep(3)
                  
        elif 'time' in text:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            respond(f"the time is {strTime}")
            
        elif 'open' in text:
            text=text.replace("open ","")
            if 'folder' in text:
                name=text.replace("folder ","")
                print(name)
                pass
            elif 'file' in text:
                name=text.replace("file ","")
                print(name)
                pass
            elif 'google' in text:
                urL='https://www.google.com/search?q='
                chrome_paths=["C:\Program Files\Google\Chrome\Application\chrome.exe","C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]
                for c_path in chrome_paths:
                    if(path.exists(c_path)):
                        webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(c_path))
                        break
                webbrowser.get('chrome').open_new_tab("https://www.google.com")
                respond("Google is open")
                time.sleep(3)
            elif 'word' in text:
                respond("Opening Microsoft Word") 
                os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
                time.sleep(3)
        elif 'rename' in text:
            text=text.replace("rename ","").replace("to","")
            ind=text.split()
            file1=ind[0]
            file2=ind[1]
            print(file1)
            print(file2)
            pass
        
        elif 'edit' in text:
            filename=text.replace("edit ","")
            respond("What to write in file "+filename)
            matter=talk().lower()
            print(matter)
            pass
        elif 'run' in text:
            text=text.replace("run ","")
            print(text)
            
        elif 'search'  in text:
            urL='https://www.google.com/search?q='
            chrome_paths=["C:\Program Files\Google\Chrome\Application\chrome.exe","C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]
            for c_path in chrome_paths:
                if(path.exists(c_path)):
                    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(c_path))
                    break
            text = text.replace("search ", "")
            webbrowser.get('chrome').open_new_tab(urL+text)
            time.sleep(5)

        else:
           respond("Application not available")
        time.sleep(2)
        """elif "calculate" or "what is" in text: 
            question=talk()
            app_id="Mention your API Key"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            respond("The answer is " + answer)"""
        
        """elif 'set' in text:
            text=text.replace("set ","")
            if 'alarm' in text:"""
