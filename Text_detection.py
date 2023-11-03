import os
import cv2
import pytesseract
import shutil

pytesseract.pytesseract.tesseract_cmd ="/usr/local/Cellar/tesseract/5.3.2_1/bin/tesseract"

mot =('', '') # mot(s) clé à trouver

dossier = "/Users/macbookair/PycharmProjects/Projet_en_cours/TexteDetection/img"

finale = []

for i in os.listdir(dossier):
    if i =='.DS_Store':
        pass
    else:
        try :
            img = cv2.imread(f'img/{i}')
            result = pytesseract.image_to_string(img)
            result = result.split()

            if mot[0] in result \
            or mot[1] in result :
                finale.append(i)

        except Exception:
            pass

if len(finale)>=1 :
    os.mkdir('/Users/macbookair/PycharmProjects/Projet_en_cours/TexteDetection/img/Return')
    for i in finale :
        shutil.move(f'/Users/macbookair/PycharmProjects/Projet_en_cours/TexteDetection/img/{i}',
                    f'/Users/macbookair/PycharmProjects/Projet_en_cours/TexteDetection/img/Return/{i}')
    print('Founded !')
    print(len(finale))
else :
    finale = "Aucun résultat"
    print(finale)
print('Fin')