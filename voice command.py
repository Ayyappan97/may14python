import pyaudio
import speech_recognition as sr

r=sr.Recognizer()
r.energy_threshold=4000

with sr.Microphone() as source:
   audio=r.listen(source)

   while True:
       if  r.recognize_google(audio) == 'start':
           try:
               print('car started')
           except LookupError:
               print('invalid command')

       elif r.recognize_google(audio) == 'stop':
           try:
            print('car stopped')
           except LookupError:
            print("invalid command")


       elif r.recognize_google(audio) == 'help':
           try:
            print("""
   start - to start 
   stop - to stop
   quit - to quit
          """)
           except LookupError:
            print("invalid command")

       elif r.recognize_google(audio) == 'quit':
           print('quit')
           break
       else:
           print('no such command')

