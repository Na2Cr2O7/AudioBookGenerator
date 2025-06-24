from sys import argv
if len(argv)<2:
    print(f'使用方法 {argv[0]} [文本文件或文本]')
    raise SystemExit
import os
import configparser


if os.path.exists('config.ini'):
    config = configparser.ConfigParser()
    config.read('config.ini')
    sizex=config['general']['frameX']
    sizey=config['general']['frameY']
    fontName=config['general']['fontName']
else:
    with open('config.ini','w',encoding='utf-8') as f:
        print('[general]',file=f)
        print(f'frameX={1080}',file=f)
        print(f'frameY={1920}',file=f)
        print(f'fontName=AlibabaPuHuiTi-3-55-Regular.ttf',file=f)
    sizex=1080
    sizey=1920

SIZE=(int(sizex),int(sizey))


DIRpunctuations=r':/\?*"<>|'
def cleanDir(dir:str):
    for i in DIRpunctuations:
        dir=dir.replace(i,'')
    return dir
punctuation=',，。\n'





from colorama import Fore  
import Audio
import stdcpp as std
import gc


import tqdm
import getVideo
import shutil

try:
    from moviepy import * # moviepy 2
except:
    from moviepy.editor import *  # type: ignore 


def splitArray(arr:list,n:int=1000):
    return [arr[i:i+n] for i in range(0,len(arr),n)]

def splitText(text:str):
    text=text.replace('\n\n','\n')
    for i in punctuation:
        text=text.replace(i,'[SPLIT]')
    text=text.replace(' ','')
    text=text.replace('[SPLIT]'*2,'[SPLIT]')
    text=text.split('[SPLIT]')
    return text

FolderstoDelete=[]
def getMovie(text:list):
    global FolderstoDelete
    fontPath=os.path.abspath(fontName)

    newDir=text[0][:50]
    newDir=cleanDir(newDir)
    FolderstoDelete.append(newDir)
    os.makedirs(newDir+'__',exist_ok=True)
    os.chdir(newDir+'__')



    print(Fore.RESET)

    audioList=[]





    for i in text:
        print(' '*(len(f'{i}')+30),end='\r',flush=True)
        print(Fore.GREEN,f'{i}',Fore.RESET,end='\r',flush=True)
        
        
        audioList.append(Audio.getAudioDuration(i))


    textbottom=['' for i in range(len(text))]
    getVideo.createVideo(
        textsCenter=text,
        textsBottom=textbottom,
        audioFiles=audioList,
        output=f'{newDir}.mp4',
        size=SIZE,
        fontPath=fontPath,
        )
    return os.path.abspath(f'{newDir}.mp4')
def concentrateVideo(videoFileList:list,output:str):
    with open('filelist.txt','w',encoding='utf-8') as f:    
        for i in videoFileList:
            f.write(f'file {i.replace("\\","/")}\n')
    os.system(f'ffmpeg -f concat -safe 0 -i filelist.txt -c copy "{output}"')
    #os.remove('filelist.txt')
if __name__ == '__main__':
    text=argv[1:]
    if os.path.exists(text[0]):
        with open(text[0],'r',encoding='utf-8') as f:
            text=f.read()
    else:
        text=' '.join(text)
    MAX_SPLIT = 1000
    text=splitText(text)
    if len(text)<MAX_SPLIT:
        
        filename=getMovie(text)
        shutil.move(filename,os.path.abspath(f'{cleanDir(argv[1])}.mp4'))
        raise SystemExit
    else:
        VideoList=[]
        for i in tqdm.tqdm(splitArray(text,MAX_SPLIT)):
            MoveiePath=getMovie(i)
            os.chdir('..')
            gc.collect()
            VideoList.append(MoveiePath)
        print(Fore.RESET,VideoList)
        concentrateVideo(VideoList,f'{cleanDir(argv[1])}.mp4')
        gc.collect()
        print(Fore.CYAN)
        for i in tqdm.tqdm(FolderstoDelete):   
            try:
                shutil.rmtree(i)
            except:
                pass    
        print(Fore.RESET)
            
    
