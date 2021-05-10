#Proiect Aplicatii multimedia 2021 
#Titul: Clipuri video in consola
#Autor: Mircea Hanghiuc 


#importam resursele necesare
import time, os, sys, cv2, shutil, math, io 
from PIL import Image,  ImageFont, ImageDraw

#variabile 

#aici am calculat cate caractere incap pe linie si cate coloane exista pentru rezolutia mea 

nr_linii = 24*2 #24*3
nr_coloane =102*2 #102*3

time.sleep(10)
nr_cadre = 50
fps = 30
#caractere = "@$B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
caractere = " .'`^,:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B$@"
Ascii_car = list(caractere)
interval =  len(Ascii_car)/256

#FUNCTII

#FUNCTIE CARE SALVEAZA UN ANUMIT NR DE CADRE CA IMAGINI 
def videoToPhoto(video, nrCadre):
    for i in range(nrCadre):
        # Capture frame-by-frame
        ret, frame = video.read()
        name = './cadre/frame' + str(i) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)
   

#functie care sterge tot continutul de pe ecran 
def curataEcran ():
    if os.name =='nt':
        os.system('cls')
    else:
        os.system("clear")


# functia care iti amintest sa maresti fereastra mareste fereastra 
def aiMarit():
    ans = "c"
    while ans != "y":
        print("Ai facut fereastra full cat tot ecranul y/n ?")
        ans = input()
        

#facem un dosar numit cadre
def facemFolder(nume):
    stergeFolder()
    try:
        if not os.path.exists(nume):
            os.makedirs(nume)
    except OSError:
        print ('Error: Creating directory of ' + nume)

# deshide clip 
def deschideClip (nume):
    try:
        cap = cv2.VideoCapture(nume)
        print ("am deschis clipul tau ")
        return cap
    except:
        print("eroare la deschidere")

# numara cadre 
def numaraCadre(cap):
    return int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) 
       

# getNumeClip

def getNumeClip():
    print ("intorduceti numele clipului cu tot tu extensie ")
    print ("Exemplu: video.mp4")
    nume = input() 
    return nume 

#redimensionarea pozelor si facerea lor alb_negru 

def modificaPoze( nr_poze):
    #deschid poza 
    
    for i in range(nr_poze):
        name = './cadre/frame' + str(i) + '.jpg'
        try:
           poza= Image.open(name)
        except:
          print("eroare la deschidere ")
        poza = poza.resize((nr_coloane, nr_linii), Image.NEAREST)
        poza = poza.convert("L") 
        poza.save(name)
        print("am prelucra " + name)
        

#sterge folderul 

def stergeFolder():
    try:
        shutil.rmtree("cadre")
    except:  
        print("eroare la stergera fisierului, probabil acesta nu a existat")

#creeaza si deschide fisierul text 
def textFile():
    try:
        os.remove("video.txt")
    except: 
        print("eroare la stergera fisierului \"video.txt\", probabil acesta nu a existat")     
    print("am creeat fisierul text in care vom salva clipul sub florma de caractere")
    return open("video.txt","w+")

#transforma o poza in text si pune-o in fisier 
def frameToText(calea):
     try:
        poza= Image.open(calea)
     except:
        print("eroare la deschidere " + calea)
        
     width,height = poza.size
     pix = poza.load()
     for i in range(height):
        for j in range(width):
            gray= pix[j,i]
            videoText.write(pix_to_car(gray))
#transforma taote pozele in caractere
def pozeToChar(nr_cadre):
    for i in range(nr_cadre):
        name = './cadre/frame' + str(i) + '.jpg'
        frameToText(name)
    
#pixel to caracter 
def pix_to_car( x  ):
    return Ascii_car[math.floor(x*interval)] 

#afisare o imagine pe ecran 
def afisarePoza(textDoc):
    for i in range(nr_linii):
        for j in range(nr_coloane):
            car = textDoc.read(1)
            #print(car, end="")
            sys.stdout.write(car)
        print("")

#reda video 
def redaVideo(nr_cadre,textDoc):
    mergiLaInceput(videoText)
    for i in range(nr_cadre):
        curataEcran()
        afisarePoza(textDoc)
        time.sleep(1/fps)



#mergi la inceputul fisieruluiu 
def mergiLaInceput(fisier):
    fisier.seek(0)




#main

nume = getNumeClip()
facemFolder("cadre")
video = deschideClip(nume)
nr_cadre = numaraCadre(video)
videoToPhoto(video, nr_cadre)
time.sleep(1)
modificaPoze(nr_cadre)
videoText = textFile()
pozeToChar(nr_cadre)
t1 = time.time()
redaVideo(nr_cadre,videoText)
t1 = time.time() - t1
print(t1)


