import speech_recognition as sr
import webbrowser
from time import ctime
import os
import random
from gtts import gTTS
import time

r = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            morag_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            morag_speak('Sorry I did not get that')
        except sr.RequestError:
            morag_speak('Sorry my speech service is down')
        return voice_data

def morag_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        morag_speak('My name is Callum')
    if 'what time is it' in voice_data:
        morag_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        morag_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        morag_speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()

time.sleep(1)
morag_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
