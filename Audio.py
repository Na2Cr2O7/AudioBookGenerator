import pyttsx3
from moviepy import *
count=0
def fetchAudio(text):
    pass

def getAudio(text):
    global count
    count+=1
    engine = pyttsx3.init()
    engine.save_to_file(text, f'{count}.wav')
    engine.runAndWait()
    engine.stop()
    return f'{count}.wav'

getAudioBackends=getAudio

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def getDuration(path)->tuple:
    
    try:
        clip = AudioFileClip(path)
        duration = clip.duration
    except Exception as e:
        print(path, e)
        duration = 0
        clip = None
    return clip,duration
def getAudioDuration(text):
    audio_path = getAudioBackends(text)
    cd = getDuration(audio_path)
    return cd
import tqdm
punctuation='.，。\n'
def getAudioDurationRaw(text):
    for i in punctuation:
        textS=text.replace(i,'[SPLIT]')
    textList=textS.split('[SPLIT]')
    returnList=[]
    for i in tqdm.tqdm(textList):
        audio_path = getAudioBackends(i)
        cd = getDuration(audio_path)
        returnList.append(cd)
    return returnList

