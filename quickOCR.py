import easyocr
from tqdm import tqdm,trange

reader=easyocr.Reader(['ch_sim','en'])


def getText(img):
    result=reader.readtext(img,detail=0)
    return ''.join(result).replace(' ','')

from sys import argv
if len(argv)<2:
    print('quickOCR.py image1.jpg image2.jpg...')
    raise SystemExit
print('结果将保存到result.txt中')
with open('result.txt','w',encoding='utf-8') as f:
    for i in trange(1,len(argv)):
        result=getText(argv[i])
        f.write(result+'\n')
        print(result)
