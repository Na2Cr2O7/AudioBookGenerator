import pyttsx3
from moviepy import *
import configparser
from time import sleep
config=configparser.ConfigParser()
config.read('config.ini')
count=0
def fetchAudio(text):
    pass

def getAudio(text):
    global count
    count+=1
    engine = pyttsx3.init()
    rate= int(config['general']['rate'])
    engine.setProperty('rate',rate)
    engine.save_to_file(text, f'{count}.wav')
    engine.runAndWait()
    engine.stop()
    return f'{count}.wav'
try:
    import requests
except:
    pass


def getAudio2(text):
    global count
    count += 1
    print(count)
    port = config['general']['server']
    url = f'http://{port}/{text}'
    print(url)
    p = requests.post(url, json={'text': text})
    if p.status_code == 200:
        with open(f'{count}.wav', 'wb') as f:
            f.write(p.content)
        return f'{count}.wav'

getAudioBackends=getAudio

def speak(text):
    engine = pyttsx3.init()
    try:
        rate= int(config['general']['rate'])
    except Exception as e:
        print(e)
        rate=150
    engine.setProperty('rate',rate)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def getDuration(path)->tuple:
    tries=0
    while tries<3:
        try:
            clip = AudioFileClip(path)
            duration = clip.duration
        except Exception as e:
            print(path, e)
            duration = 0
            clip = None
            tries+=1
            sleep(1)
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

if __name__ == '__main__':
    text='你好，我是机器人。'
    getAudio2(text)