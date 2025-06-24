import os
import shutil
import tqdm
if not os.path.exists(r'.\temp'):
    os.makedirs(r'.\temp')

fileExt=['.exe','.py','.ini','.argosmodel','.ttc','.U','.ttf','.jpg','.cpp','.ini']
for file in tqdm.tqdm(os.listdir()):
    try:
        print(os.path.splitext(file)[1])
        if os.path.isdir(file):
            print(f'>>{file}')
        if not os.path.splitext(file)[1] in fileExt:
            shutil.move(file,r'.\temp')
    except PermissionError:
        print(f'PermissionError: {file}')
    except shutil.Error as e    :
        print(f'Error: {file} {e}')
i=input('需要删除temp文件夹吗？(y/n)')
if i=='y':
    shutil.rmtree(r'.\temp')